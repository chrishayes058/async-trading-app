import os
import functools

import asyncio
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")


def create_client():
    trading_client = TradingClient(API_KEY, API_SECRET, paper=True)
    return trading_client


async def buy_stock(trading_client: TradingClient):
    loop = asyncio.get_event_loop()
    market_order_data = MarketOrderRequest(
        symbol="SPY",
        qty=0.023,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
    )
    result = await loop.run_in_executor(
        None,
        functools.partial(
            trading_client.submit_order, order_data=market_order_data
        ),
    )
    return result
