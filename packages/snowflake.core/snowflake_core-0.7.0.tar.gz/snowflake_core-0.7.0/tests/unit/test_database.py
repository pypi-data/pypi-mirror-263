from contextlib import suppress
from unittest import mock

from snowflake.core.database import Database, DatabaseCollection


def test_fetch(fake_root):
    dbs = DatabaseCollection(fake_root)
    with suppress(Exception):
        with mock.patch(
            "snowflake.core.database._generated.api_client.ApiClient.request"
        ) as mocked_request:
            dbs["my_db"].fetch()
    mocked_request.assert_called_once_with(
        'GET',
        'http://localhost:80/api/v2/databases/my_db',
        query_params=[],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )

def test_delete(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db"].delete()
    mocked_request.assert_called_once_with(
        'DELETE',
        'http://localhost:80/api/v2/databases/my_db',
        query_params=[],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )

def test_create(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs.create(
            Database(
                name="sophie_db",
                comment="This is Sophie's database",
                trace_level="always",
            ),
            kind="transient",
        )
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases?createMode=errorIfExists&kind=transient',
        query_params=[
            ('createMode', 'errorIfExists'),
            ('kind', 'transient'),
        ],
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
        },
        post_params=[],
        body={'name': 'sophie_db', 'comment': "This is Sophie's database", 'trace_level': 'always', 'dropped_on': None},
        _preload_content=True,
        _request_timeout=None,
    )

def test_create_from_share(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs._create_from_share(
            name="name",
            share="share",
        )
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/from_share?createMode=errorIfExists&name=name&share=share&kind=',
        query_params=[
            ('createMode', 'errorIfExists'),
            ('name', 'name'),
            ('share', 'share'),
            ('kind', ''),
        ],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )

def test_enable_replication(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db2"].enable_replication(
            ["fake_identifier1", "fake_identifier2"]
        )
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db2/replication:enable?ignore_edition_check=False',
        query_params=[
            ('ignore_edition_check', False),
        ],
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
        },
        post_params=[],
        body={'accounts': ['fake_identifier1', 'fake_identifier2']},
        _preload_content=True,
        _request_timeout=None,
    )

def test_disable_replication(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db2"].disable_replication()
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db2/replication:disable',
        query_params=[],
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
        },
        post_params=[],
        body={'accounts': []},
        _preload_content=True,
        _request_timeout=None,
    )

def test_refresh_replication(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db2"].refresh_replication()
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db2/replication:refresh',
        query_params=[],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )

def test_enable_failover(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db2"].enable_failover(
            ["fake_identifier1", "fake_identifier2"]
        )
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db2/failover:enable',
        query_params=[],
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
        },
        post_params=[],
        body={'accounts': ['fake_identifier1', 'fake_identifier2']},
        _preload_content=True,
        _request_timeout=None,
    )

def test_disable_failover(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db2"].disable_failover()
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db2/failover:disable',
        query_params=[],
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
        },
        post_params=[],
        body={'accounts': []},
        _preload_content=True,
        _request_timeout=None,
    )

def test_promote_to_primary_failover(fake_root):
    dbs = DatabaseCollection(fake_root)
    with mock.patch(
        "snowflake.core.database._generated.api_client.ApiClient.request"
    ) as mocked_request:
        dbs["my_db2"].promote_to_primary_failover()
    mocked_request.assert_called_once_with(
        'POST',
        'http://localhost:80/api/v2/databases/my_db2/failover:primary',
        query_params=[],
        headers={'Accept': 'application/json', 'User-Agent': 'OpenAPI-Generator/1.0.0/python'},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )
