#!/bin/bash

echo "================================"
echo "🚀 Démarrage du Système de Gestion"
echo "================================"

# Naviguer au répertoire backend
cd backend

# Activer l'environnement virtuel
echo "📦 Activation de l'environnement virtuel..."
source christ/bin/activate

# Initialiser la base de données (optionnel - une seule fois)
echo "🔧 Initialisation de la base de données..."
python api_gateway/init_db.py

# Démarrer le serveur
echo ""
echo "🌐 Démarrage du serveur FastAPI..."
echo "📡 Le serveur sera disponible à: http://localhost:8000"
echo "📚 Documentation Swagger: http://localhost:8000/docs"
echo ""
echo "Pour accéder au frontend, ouvrez:"
echo "🖥️  file:///$(pwd)/../frontend/index.html"
echo ""
echo "Ou utilisez un serveur local:"
echo "cd ../frontend && python -m http.server 8080"
echo ""

cd api_gateway
python main.py
