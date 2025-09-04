#!/bin/bash

echo "🚀 Setting up Stock Prices Application..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create environment files if they don't exist
echo "📝 Setting up environment files..."

if [ ! -f frontend/.env ]; then
    echo "Creating frontend/.env from template..."
    cp frontend/.env.example frontend/.env
    echo "⚠️  Please edit frontend/.env and set your SECRET_KEY"
fi

if [ ! -f backend/.env ]; then
    echo "Creating backend/.env from template..."
    cp backend/.env.example backend/.env
    echo "⚠️  Please edit backend/.env and set your API keys"
fi

echo "✅ Environment files created!"
echo "📋 To start the application:"
echo "   docker-compose up --build"
echo ""
echo "🌐 Application will be available at:"
echo "   Frontend: http://localhost:5000"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"