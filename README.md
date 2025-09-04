# Stock Prices Application

A full-stack stock prices application with Flask frontend and FastAPI backend, deployed using Docker.

## Architecture

### Monorepo Structure
```
stock-prices-app/
├── frontend/               # Flask web application
│   ├── Dockerfile
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── templates/
│   ├── static/
│   ├── utils/
│   └── tests/
├── backend/                # FastAPI REST API
│   ├── Dockerfile
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── models/
│   ├── routers/
│   ├── services/
│   └── tests/
├── shared/                 # Shared utilities/types
├── docs/                   # Documentation
│   ├── plan.md
│   └── devlog.md
├── scripts/                # Development scripts
├── docker-compose.yml      # Development environment
├── docker-compose.prod.yml # Production environment
└── README.md
```

### Services
- **Frontend (Flask):** User interface on port 5000
- **Backend (FastAPI):** REST API on port 8000
- **Redis:** Caching layer on port 6379

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd stock-prices-app
   ```

2. **Environment configuration**
   ```bash
   # Copy and configure environment files
   cp frontend/.env.example frontend/.env
   cp backend/.env.example backend/.env
   ```

3. **Start the application**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:5000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Individual Service Development

#### Frontend Development (Flask)
1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Dependencies installed:
   - Flask==3.0.3 (web framework)
   - requests==2.31.0 (HTTP client)
   - python-dotenv==1.0.1 (environment variables)
   - gunicorn==21.2.0 (WSGI server)
   - Werkzeug==3.0.3 (WSGI utilities)

4. **Run the application**
   ```bash
   python app.py
   ```
   
   The frontend will be available at:
   - http://127.0.0.1:5000 (localhost)
   - http://localhost:5000

#### Backend Development (FastAPI)
*Instructions to be provided by backend team*

#### Notes
- Frontend runs in debug/development mode by default
- Virtual environments keep dependencies isolated  
- Make sure to activate the virtual environment each time you work on the project

## API Endpoints

### Backend (FastAPI)
- `GET /api/price?symbol={symbol}` - Current stock price
- `GET /api/company?symbol={symbol}` - Company information
- `GET /api/historical?symbol={symbol}&start={date}&end={date}` - Historical data
- `GET /api/search?query={query}` - Search stocks
- `GET /api/trending` - Top movers
- `GET /health` - Health check

### Frontend (Flask)
- `GET /` - Main dashboard
- `GET /company/<symbol>` - Company detail page
- `GET /trending` - Top movers page

## Features

- **Real-time stock prices** with live updates
- **Interactive charts** using Chart.js
- **Company information** and financial data
- **Stock search** with autocomplete
- **Top movers** (gainers/losers)
- **Responsive design** for mobile/desktop
- **Docker deployment** for easy scaling

## Development Commands

### Docker Commands
```bash
# Development environment
docker-compose up --build

# Production environment
docker-compose -f docker-compose.prod.yml up --build

# Stop services
docker-compose down

# View logs
docker-compose logs -f [service-name]
```

### Testing
```bash
# Frontend tests
cd frontend && python -m pytest tests/

# Backend tests
cd backend && python -m pytest tests/

# Full test suite
docker-compose run frontend python -m pytest
docker-compose run backend python -m pytest
```

## Configuration

### Environment Variables

#### Frontend (.env)
```env
SECRET_KEY=your-secret-key
FLASK_DEBUG=True
STOCK_API_URL=http://localhost:8000
```

#### Backend (.env)
```env
API_DEBUG=True
ALPHA_VANTAGE_API_KEY=your-api-key
REDIS_URL=redis://localhost:6379
```

## Performance Requirements
- **Frontend load time:** <4s cached, <6s uncached (p95)
- **API response time:** <2s cached, <5s fresh data
- **Browser support:** Chrome, Edge, Firefox, Safari
- **Accessibility:** WCAG 2.1 AA compliance

## Deployment

### Production Deployment
```bash
# Deploy with production configuration
docker-compose -f docker-compose.prod.yml up -d

# Scale services
docker-compose -f docker-compose.prod.yml up -d --scale backend=3
```

### Health Monitoring
- Frontend health: http://localhost:5000/health
- Backend health: http://localhost:8000/health
- Redis health: `docker-compose exec redis redis-cli ping`

## Contributing

1. Create a feature branch from `main`
2. Make changes to frontend/ or backend/ as needed
3. Run tests locally
4. Submit a pull request

## License

This project is for educational purposes.