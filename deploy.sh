#!/bin/bash

# Script de déploiement du projet

echo "🚀 Script de Déploiement"
echo "======================="
echo ""

# Menu
echo "Sélectionnez une option:"
echo "1) Initialiser le repository Git"
echo "2) Déployer le backend sur Railway"
echo "3) Déployer le frontend sur Vercel"
echo "4) Tester localement avec Docker"
echo "5) Pousser les changements sur GitHub"
echo ""

read -p "Entrez votre choix (1-5): " choice

case $choice in
    1)
        echo ""
        echo "📝 Initialisation Git..."
        bash init-git.sh
        ;;
    2)
        echo ""
        echo "🚀 Instructions pour Railway:"
        echo "1. Aller sur https://railway.app"
        echo "2. Créer un nouveau projet"
        echo "3. Sélectionner 'Deploy from GitHub repo'"
        echo "4. Ajouter PostgreSQL comme service"
        echo "5. Configurer les variables d'environnement"
        echo "6. Root Directory: backend/api_gateway"
        echo "7. Start Command: uvicorn main:app --host 0.0.0.0 --port \$PORT"
        echo ""
        read -p "Appuyez sur Entrée une fois déployé..."
        ;;
    3)
        echo ""
        echo "💎 Instructions pour Vercel:"
        echo "1. Aller sur https://vercel.com"
        echo "2. Importer votre repository GitHub"
        echo "3. Root Directory: frontend"
        echo "4. Ajouter la variable VITE_API_URL"
        echo "5. Cliquer sur Deploy"
        echo ""
        read -p "Appuyez sur Entrée une fois déployé..."
        ;;
    4)
        echo ""
        echo "🐳 Démarrage avec Docker Compose..."
        docker-compose up
        ;;
    5)
        echo ""
        echo "📤 Poussage sur GitHub..."
        read -p "Message de commit: " message
        git add .
        git commit -m "$message"
        git push origin main
        echo "✅ Changements poussés!"
        ;;
    *)
        echo "❌ Option invalide"
        exit 1
        ;;
esac
