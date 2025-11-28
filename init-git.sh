#!/bin/bash

# Script d'initialisation Git pour le projet

echo "🚀 Initialisation du repository Git..."

# Vérifier si Git est installé
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé. Veuillez installer Git d'abord."
    exit 1
fi

# Vérifier si on est dans le bon dossier
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Erreur: Exécutez ce script depuis la racine du projet"
    exit 1
fi

# Initialiser Git
if [ ! -d ".git" ]; then
    echo "📝 Initialisation du repository Git..."
    git init
    echo "✅ Repository Git créé"
else
    echo "ℹ️  Repository Git déjà existant"
fi

# Ajouter tous les fichiers
echo "📦 Ajout des fichiers..."
git add .

# Créer le commit initial
echo "💾 Création du commit initial..."
git commit -m "Initial commit: User Management System with Admin, Employer, Client roles"

# Instructions pour l'utilisateur
echo ""
echo "✅ Repository Git initialisé avec succès!"
echo ""
echo "📋 Prochaines étapes:"
echo ""
echo "1️⃣  Créer un repository sur GitHub (https://github.com/new)"
echo ""
echo "2️⃣  Ajouter l'URL distante:"
echo "   git remote add origin https://github.com/votre-username/nom-repo.git"
echo ""
echo "3️⃣  Pousser le code:"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4️⃣  Suivre le guide de déploiement:"
echo "   📖 Voir GUIDE_DEPLOIEMENT.md"
echo ""
