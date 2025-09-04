document.addEventListener('DOMContentLoaded', function() {
    const stockForm = document.getElementById('stock-search-form');
    const stockResults = document.getElementById('stock-results');

    if (stockForm) {
        stockForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const symbol = document.getElementById('stock-symbol').value.trim().toUpperCase();
            if (symbol) {
                fetchStockData(symbol);
            }
        });
    }
});

function fetchStockData(symbol) {
    const resultsDiv = document.getElementById('stock-results');
    const detailCard = document.getElementById('stock-detail-card');
    
    if (resultsDiv) {
        resultsDiv.style.display = 'block';
        document.getElementById('stock-name').textContent = `Loading ${symbol}...`;
    }

    fetch(`/api/stock/${symbol}`)
        .then(response => response.json())
        .then(data => {
            updateStockDisplay(data);
        })
        .catch(error => {
            console.error('Error fetching stock data:', error);
            if (resultsDiv) {
                document.getElementById('stock-name').textContent = 'Error loading stock data';
                document.getElementById('stock-price').textContent = 'N/A';
                document.getElementById('stock-change').textContent = 'Error';
                document.getElementById('stock-change').className = 'badge bg-secondary';
            }
        });
}

function updateStockDisplay(data) {
    const isPositive = data.change >= 0;
    const changeClass = isPositive ? 'badge bg-success' : 'badge bg-danger';
    const changeText = `${data.change.toFixed(2)} (${data.change_percent.toFixed(2)}%)`;
    
    // Update main page elements
    const stockName = document.getElementById('stock-name');
    const stockPrice = document.getElementById('stock-price');
    const stockChange = document.getElementById('stock-change');
    
    if (stockName) stockName.textContent = data.symbol;
    if (stockPrice) stockPrice.textContent = `$${data.price.toFixed(2)}`;
    if (stockChange) {
        stockChange.textContent = changeText;
        stockChange.className = changeClass;
    }
    
    // Update detail page elements
    const detailStockName = document.getElementById('detail-stock-name');
    const detailStockPrice = document.getElementById('detail-stock-price');
    const detailStockChange = document.getElementById('detail-stock-change');
    const lastUpdated = document.getElementById('last-updated');
    
    if (detailStockName) detailStockName.textContent = data.symbol;
    if (detailStockPrice) detailStockPrice.textContent = `$${data.price.toFixed(2)}`;
    if (detailStockChange) {
        detailStockChange.textContent = changeText;
        detailStockChange.className = changeClass;
    }
    if (lastUpdated) lastUpdated.textContent = new Date().toLocaleString();
}