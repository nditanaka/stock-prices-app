#!/bin/bash

# Development helper script

case "$1" in
    "start")
        echo "🚀 Starting development environment..."
        docker-compose up --build
        ;;
    "stop")
        echo "🛑 Stopping all services..."
        docker-compose down
        ;;
    "logs")
        if [ -z "$2" ]; then
            echo "📋 Showing logs for all services..."
            docker-compose logs -f
        else
            echo "📋 Showing logs for $2..."
            docker-compose logs -f "$2"
        fi
        ;;
    "test")
        if [ "$2" = "frontend" ]; then
            echo "🧪 Running frontend tests..."
            docker-compose run frontend python -m pytest tests/
        elif [ "$2" = "backend" ]; then
            echo "🧪 Running backend tests..."
            docker-compose run backend python -m pytest tests/
        else
            echo "🧪 Running all tests..."
            docker-compose run frontend python -m pytest tests/
            docker-compose run backend python -m pytest tests/
        fi
        ;;
    "shell")
        if [ "$2" = "frontend" ]; then
            echo "🐚 Opening frontend shell..."
            docker-compose exec frontend /bin/bash
        elif [ "$2" = "backend" ]; then
            echo "🐚 Opening backend shell..."
            docker-compose exec backend /bin/bash
        else
            echo "❌ Please specify service: frontend or backend"
            echo "Usage: ./scripts/dev.sh shell [frontend|backend]"
        fi
        ;;
    "clean")
        echo "🧹 Cleaning up Docker resources..."
        docker-compose down -v
        docker system prune -f
        ;;
    *)
        echo "Stock Prices App - Development Helper"
        echo ""
        echo "Usage: ./scripts/dev.sh [command]"
        echo ""
        echo "Commands:"
        echo "  start              Start development environment"
        echo "  stop               Stop all services"
        echo "  logs [service]     Show logs (all or specific service)"
        echo "  test [service]     Run tests (all, frontend, or backend)"
        echo "  shell [service]    Open shell in service container"
        echo "  clean              Clean up Docker resources"
        echo ""
        echo "Examples:"
        echo "  ./scripts/dev.sh start"
        echo "  ./scripts/dev.sh logs frontend"
        echo "  ./scripts/dev.sh test backend"
        echo "  ./scripts/dev.sh shell frontend"
        ;;
esac