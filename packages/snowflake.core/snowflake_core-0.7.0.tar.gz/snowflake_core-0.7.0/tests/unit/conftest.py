import logging

from unittest import mock

import pytest


@pytest.fixture(scope="session")
def fake_root():
    """Mock for Root.

    Usage of this central definition is necessary since the underlying
    generated Configuration class is handled as a singleton, so we treat
    the unit test root as a singleton as well.
    """
    return mock.MagicMock(
        _connection=mock.MagicMock(
            _rest=mock.MagicMock(
                _host="localhost",
                _protocol="http",
                _port="80",
            )
        )
    )

@pytest.fixture()
def logger_level_info(caplog):
    # Default logger level to info

    with caplog.at_level(logging.INFO):
        yield
