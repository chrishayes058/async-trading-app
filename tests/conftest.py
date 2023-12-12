import pytest
from unittest.mock import Mock

from alpaca.trading.client import TradingClient


@pytest.fixture
def mock_create_client(mocker):
    mock = Mock(spec=TradingClient("API_KEY", "API_SECRET", paper=True))
    mocker.patch("alpaca.trading.client.TradingClient", return_value=mock)
    return mock
