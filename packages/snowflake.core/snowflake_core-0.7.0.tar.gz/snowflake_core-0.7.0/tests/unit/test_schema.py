from contextlib import suppress
from unittest import mock

from snowflake.core.database import DatabaseCollection
from snowflake.core.schema import Schema


def test_fetch(fake_root):
    dbs = DatabaseCollection(fake_root)
    db = dbs["my_db"]
    schemas = db.schemas
    with suppress(Exception):
        with mock.patch(
            "snowflake.core.schema._generated.api_client.ApiClient.request"
        ) as mocked_request:
            schemas["schema"].fetch()
    mocked_request.assert_called_once_with(
        'GET',
        'http://localhost:80/api/v2/databases/my_db/schemas/schema',
        query_params=[],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )

def test_delete(fake_root):
    dbs = DatabaseCollection(fake_root)
    db = dbs["my_db"]
    schemas = db.schemas
    with mock.patch(
        "snowflake.core.schema._generated.api_client.ApiClient.request"
    ) as mocked_request:
        schemas["schema"].delete()
    mocked_request.assert_called_once_with(
        'DELETE',
        'http://localhost:80/api/v2/databases/my_db/schemas/schema',
        query_params=[],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )

def test_create(fake_root):
    dbs = DatabaseCollection(fake_root)
    db = dbs["my_db"]
    schemas = db.schemas
    with mock.patch(
        "snowflake.core.schema._generated.api_client.ApiClient.request"
    ) as mocked_request:
        schemas.create(
            Schema(
                name="schema",
                comment="my schema",
                trace_level="always",
            ),
            kind="transient",
        )
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db/schemas?createMode=errorIfExists&kind=transient&with_managed_access=False',
        query_params=[
            ('createMode', 'errorIfExists'),
            ('kind', 'transient'),
            ('with_managed_access', False),
        ],
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
        },
        post_params=[],
        body={'name': 'schema', 'comment': "my schema", 'trace_level': 'always', 'dropped_on': None},
        _preload_content=True,
        _request_timeout=None,
    )
