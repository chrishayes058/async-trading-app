import uvicorn
from fastapi import FastAPI

from trading import create_client, buy_stock
from models import Stock

app = FastAPI()
trading_client = create_client()


@app.post("/buy")
async def buy_stock_endpoint(stock: Stock):
    result = await buy_stock(trading_client, stock)
    return {"status": result}


@app.post("/sell")
async def sell_stock_endpoint(stock: Stock):
    return {"status": "OK"}


@app.post("/close_position")
async def close_position_endpoint(stock: Stock):
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
