import uvicorn
from fastapi import FastAPI

from models import Stock

app = FastAPI()

@app.post("/buy")
async def buy_stock(stock: Stock):
    print(stock)
    return {"status": "OK"}

@app.post("/sell")
async def sell_stock(stock: Stock):
    return {"status": "OK"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)