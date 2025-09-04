from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class StockPrice(BaseModel):
    symbol: str
    price: float
    change: float
    change_percent: float
    timestamp: datetime

class CompanyInfo(BaseModel):
    symbol: str
    name: str
    sector: Optional[str] = None
    description: Optional[str] = None
    market_cap: Optional[int] = None
    employees: Optional[int] = None

class HistoricalDataPoint(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int

class HistoricalData(BaseModel):
    symbol: str
    data: List[HistoricalDataPoint]

class SearchResult(BaseModel):
    symbol: str
    name: str

class TopMoversResponse(BaseModel):
    gainers: List[StockPrice]
    losers: List[StockPrice]
    most_active: List[StockPrice]