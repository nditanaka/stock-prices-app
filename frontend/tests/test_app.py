import unittest
from app import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_health_route(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.get_json())
    
    def test_stock_detail_route(self):
        response = self.client.get('/stock/AAPL')
        self.assertEqual(response.status_code, 200)
    
    def test_api_stock_route(self):
        response = self.client.get('/api/stock/AAPL')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('symbol', data)
        self.assertIn('price', data)

if __name__ == '__main__':
    unittest.main()