import json
import os
import re
from pathlib import Path

import pytest
import requests
from awslambdaric.lambda_context import LambdaContext

from pydantic_lambda_handler.gen_open_api_inspect import gen_open_api_inspect


def pytest_addoption(parser):
    parser.addoption("--live", action="store_true", help="Also test against real AWS")


class Response:
    def __init__(self, response):
        self._response = response

    @property
    def status_code(self):
        return self._response["statusCode"]

    def json(self):
        return json.loads(self._response["body"])

    @property
    def text(self):
        return self._response["body"]

    @property
    def content(self):
        return bytes(self._response["body"])


class RequestClient:
    def __init__(self):
        path = Path(__file__).parents[1].joinpath("demo_app/src")
        self._spec, self._cdk_stuff, self._test = gen_open_api_inspect(path)

    def get(self, url, *args, **kwargs):
        try:
            return self._mock_request(url, "get", *args, **kwargs)
        except Exception:
            return Response({"statusCode": 502, "body": json.dumps({"message": "Internal server error"})})

    def post(self, url, *args, **kwargs):
        try:
            return self._mock_request(url, "post", *args, **kwargs)
        except Exception:
            return Response({"statusCode": 502, "body": json.dumps({"message": "Internal server error"})})

    def _mock_request(self, url, method, *args, **kwargs):
        event = self.generate_event(kwargs, url)

        for comp_url, info in self._test["paths"].items():
            try:
                match = re.fullmatch(comp_url, url)
            except Exception as e:
                print(e)
                # None breaking here
                continue

            if match:
                decorated_function_ = info[method]["handler"]["decorated_function"]
                break
        else:  # No break
            raise ValueError

        context = LambdaContext(
            invoke_id="abd",
            client_context=None,
            cognito_identity=None,
            epoch_deadline_time_in_ms=1660605740936,
            invoked_function_arn="abd",
        )

        function_ = self._test["paths"][comp_url][method]["handler"]["function"]
        response = decorated_function_(function_)(event, context)
        return Response(response)

    def generate_event(self, kwargs, url):
        if "data" in kwargs:
            body = kwargs["data"]
        elif "json" in kwargs:
            body = json.dumps(kwargs["json"])
        else:
            body = None
        for comp_url, info in self._test["paths"].items():
            try:
                match = re.fullmatch(comp_url, url)
            except Exception:
                # None breaking here
                continue

            if match:
                break
        else:  # No break
            raise ValueError

        qs_params = {}
        mult_qs_params = {}

        for key, values in kwargs.get("params", {}).items():
            if isinstance(values, list):
                for value in values:
                    qs_params[key] = value
                mult_qs_params[key] = values
            else:
                qs_params[key] = values
                mult_qs_params[key] = [values]

        event = {
            "body": body,
            "queryStringParameters": qs_params or None,
            "multiValueQueryStringParameters": mult_qs_params or None,
            "pathParameters": match.groupdict(),
            "headers": kwargs.get("headers"),
        }
        return event


@pytest.fixture(scope="function")
def base_url(requests_client_type):
    return os.environ["BASE_URL"] if requests_client_type == "real" else ""


@pytest.fixture(scope="function")
def requests_client(requests_client_type):
    return requests if requests_client_type == "real" else RequestClient()


def pytest_generate_tests(metafunc):
    if "requests_client_type" in metafunc.fixturenames:
        types = ["mock"]
        if metafunc.config.getoption("live"):
            types.append("real")
        metafunc.parametrize("requests_client_type", types)


@pytest.fixture
def _gen():
    path = Path(__file__).parents[1].joinpath("demo_app/src")
    schema, cdk_stuff, _ = gen_open_api_inspect(path)
    return schema, cdk_stuff


@pytest.fixture
def schema(_gen):
    schema, *_ = _gen
    return json.loads(schema)


@pytest.fixture
def cdk_config(_gen):
    _, cdk_config = _gen
    return cdk_config


@pytest.fixture
def mock_lambda_context():
    return LambdaContext(
        invoke_id="abd",
        client_context=None,
        cognito_identity=None,
        epoch_deadline_time_in_ms=1660605740936,
        invoked_function_arn="abd",
    )
