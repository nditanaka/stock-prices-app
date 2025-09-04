from flask import Flask, render_template, request, jsonify
import os
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/stock/<symbol>')
    def stock_detail(symbol):
        return render_template('stock_detail.html', symbol=symbol.upper())
    
    @app.route('/api/stock/<symbol>')
    def api_stock_data(symbol):
        # This would integrate with your stock price service
        return jsonify({
            'symbol': symbol.upper(),
            'price': 0.0,
            'change': 0.0,
            'change_percent': 0.0
        })
    
    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=app.config.get('HOST', '0.0.0.0'),
        port=app.config.get('PORT', 5000),
        debug=app.config.get('DEBUG', True)
    )