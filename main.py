from fastapi import FastAPI

from models import Stock

app = FastAPI()

@app.post("/buy")
async def buy_stock(stock: Stock):
    print(stock)

@app.post("/sell")
async def sell_stock(stock: Stock):
    print(stock)