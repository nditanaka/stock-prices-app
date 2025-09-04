import requests
from typing import Dict, Optional
from flask import current_app

class StockAPIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def get_stock_price(self, symbol: str) -> Dict:
        try:
            url = f"{self.base_url}/api/stock/{symbol}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Error fetching stock data for {symbol}: {e}")
            return {
                'symbol': symbol.upper(),
                'price': 0.0,
                'change': 0.0,
                'change_percent': 0.0,
                'error': str(e)
            }
    
    def health_check(self) -> bool:
        try:
            url = f"{self.base_url}/health"
            response = self.session.get(url, timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False