import json
from http import client

import pytest
from openapi_spec_validator import validate_spec

from pydantic_lambda_handler.hooks.open_api_gen_hook import APIGenerationHook
from pydantic_lambda_handler.main import PydanticLambdaHandler
from pydantic_lambda_handler.params import Header


def test_generate_open_api_version(schema):
    assert schema["openapi"] == "3.1.0"


@pytest.mark.xfail(reason="Partial upgrade to pydantic v2")
def test_valid_open_api_spc(schema):
    validate_spec(schema)


@pytest.mark.xfail(reason="Partial upgrade to pydantic v2")
def test_valid_open_api_spc_missing_key():
    app = PydanticLambdaHandler(title="PydanticLambdaHandler")
    app.add_hook(APIGenerationHook)

    @app.get("/sources/{key}/data")
    def data_links(key: str):
        return {"key": key}

    schema = next(h for h in app._hooks if issubclass(h, APIGenerationHook)).generate()  # type: ignore
    schema = json.loads(schema)
    validate_spec(schema)


@pytest.mark.xfail(reason="Partial upgrade to pydantic v2")
def test_valid_open_api_spc_missing_key_with_header():
    app = PydanticLambdaHandler(title="PydanticLambdaHandler")
    app.add_hook(APIGenerationHook)
    header_host = Header("", alias="Host", include_in_schema=False)

    @app.get("/sources/{key}/data")
    def data_links(key: str, host: str = header_host):
        return {"key": key}

    schema = next(h for h in app._hooks if issubclass(h, APIGenerationHook)).generate()  # type: ignore
    schema = json.loads(schema)
    validate_spec(schema)


def test_generate_open_api_info(schema):
    assert schema["info"] == {"title": "PydanticLambdaHandler", "version": "0.0.0"}


def test_generate_open_api_info_path_get(schema):
    item_path = schema["paths"]["/hello"]["get"]["responses"]["200"]["content"]
    assert item_path == {"application/json": {}}


def test_generate_open_api_info_path_post(schema):
    item_path = schema["paths"]["/hello"]["post"]["responses"]["201"]["content"]
    assert item_path == {"application/json": {}}


def test_generate_open_api_list_response_model(schema):
    item_path = schema["paths"]["/list_response_model"]["get"]["responses"]["200"]["content"]
    assert item_path == {"application/json": {"schema": {"$ref": "#/components/schemas/ListFunModel"}}}
    assert schema["components"]["schemas"]["ListFunModel"] == {
        "items": {"$ref": "#/components/schemas/FunModel"},
        "title": "ListFunModel",
        "type": "array",
    }


def test_query_body(schema):
    request_schema = schema["paths"]["/hello"]["post"]["requestBody"]["content"]["application/json"]["schema"]
    assert request_schema == {"$ref": "#/components/schemas/Item"}
    assert schema["components"]["schemas"]["Item"] == {
        "properties": {
            "description": {"anyOf": [{"type": "string"}, {"type": "null"}], "title": "Description"},
            "name": {"title": "Name", "type": "string"},
            "price": {"title": "Price", "type": "number"},
            "tax": {"anyOf": [{"type": "number"}, {"type": "null"}], "title": "Tax"},
        },
        "required": ["name", "price"],
        "title": "Item",
        "type": "object",
    }


def test_generate_open_api_status_code_int(schema):
    """Can accept an in or an Enum status code"""
    assert "418" in schema["paths"]["/teapot"]["get"]["responses"]


def test_generate_open_api_path(schema):
    assert "/pets/{petId}" in schema["paths"]
    assert schema["paths"]["/pets/{petId}"]["get"].get("parameters") == [
        {"name": "petId", "in": "path", "required": True, "schema": {"title": "Petid", "type": "string"}}
    ]


def test_generate_open_operation_id(schema):
    assert schema["paths"]["/pets/{petId}"]["get"].get("operationId") == "Create Pet"


def test_query_options(schema):
    assert "/query" in schema["paths"]
    assert schema["paths"]["/query"]["get"].get("parameters") == [
        {"in": "query", "name": "skip", "schema": {"default": 0, "title": "Skip", "type": "integer"}},
        {"in": "query", "name": "limit", "schema": {"default": 10, "title": "Limit", "type": "integer"}},
    ]


def test_response_body(schema):
    assert "/response_model" in schema["paths"]
    response_schema = schema["paths"]["/response_model"]["get"]["responses"]["200"]["content"]["application/json"][
        "schema"
    ]
    assert response_schema == {"$ref": "#/components/schemas/FunModel"}
    assert schema["components"]["schemas"]["FunModel"] == {
        "properties": {
            "item_name": {"title": "Item Name", "type": "string"},
            "item_value": {"anyOf": [{"type": "integer"}, {"type": "null"}], "title": "Item Value"},
        },
        "required": ["item_name"],
        "title": "FunModel",
        "type": "object",
    }


def test_header_options(schema):
    assert "/with_headers" in schema["paths"]
    assert schema["paths"]["/with_headers"]["get"].get("parameters") == [
        {
            "in": "header",
            "name": "user_agent",
            "schema": {"anyOf": [{"type": "string"}, {"type": "null"}], "default": None, "title": "User Agent"},
        }
    ]


def test_header_options_not_in_schema(schema):
    assert "/with_headers_not_in_schema" in schema["paths"]
    headers = [
        i["name"] for i in schema["paths"]["/with_headers_not_in_schema"]["get"]["parameters"] if i["in"] == "header"
    ]
    assert "user_agent" not in headers


@pytest.mark.xfail(reason="Partial upgrade to pydantic v2")
def test_header_options_uses_alias(schema):
    assert "/with_headers_alias" in schema["paths"]
    assert schema["paths"]["/with_headers_alias"]["get"].get("parameters") == [
        {"in": "header", "name": "UserId", "schema": {"title": "Userid", "type": "string"}}
    ]


def test_errors(schema):
    assert "/error" in schema["paths"]
    assert schema["paths"]["/error"]["get"]["responses"]["418"] == {
        "content": {"application/json": {}},
        "description": "Inappropriate argument value (of correct type).",
    }


def test_multiple_errors_description(schema):
    assert "/multiple_errors" in schema["paths"]
    description = schema["paths"]["/multiple_errors"]["get"]["responses"]["422"]["description"]
    assert description == client.responses[422]


def test_query_union(schema):
    assert "/query_union" in schema["paths"]
    parameters = schema["paths"]["/query_union"]["get"]["parameters"]
    assert parameters == [
        {
            "in": "query",
            "name": "param",
            "schema": {
                "anyOf": [
                    {"type": "number"},
                    {"type": "string"},
                    {"format": "date-time", "type": "string"},
                    {"type": "null"},
                ],
                "default": None,
                "title": "Param",
            },
        }
    ]
