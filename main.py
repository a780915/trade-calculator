from fastapi import FastAPI
from pydantic import BaseModel
from risk_engine import calculate_trade

app = FastAPI()

class TradeInput(BaseModel):
    direction: str
    capital: float
    risk_pct: float
    entry: float
    stop: float

@app.post("/calculate")
def calculate(data: TradeInput):
    result = calculate_trade(
        capital=data.capital,
        risk_pct=data.risk_pct,
        entry=data.entry,
        stop=data.stop,
    )

    return {
        "direction": data.direction,
        "entry": data.entry,
        "stop": data.stop,
        "take_profit": result["take_profit"],
        "lot_size": result["lot_size"],
        "actual_loss": result["actual_loss"],
        "actual_profit": result["actual_profit"],
    }
