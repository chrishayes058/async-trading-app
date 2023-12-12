import pytest

from src.trading import buy_stock
from src.models import Stock

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_buy_stock(mock_create_client):
    mock_trading_client = mock_create_client()

    mock_stock_data = Stock(name="SPY", quantity=1.0)

    mock_trading_client.submit_order.return_value = (
        mock_stock_data.model_dump_json()
    )

    result = await buy_stock(mock_trading_client, mock_stock_data)
    assert result == mock_stock_data.model_dump_json()
