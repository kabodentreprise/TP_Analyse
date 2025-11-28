#!/bin/bash
# Script d'installation complète du projet

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🚀 Installation du Système de Gestion des Utilisateurs  ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 n'est pas installé${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Python 3 trouvé${NC}"
echo ""

# Naviguer au répertoire backend
cd backend

# Vérifier si l'environnement virtuel existe
if [ ! -d "christ" ]; then
    echo -e "${YELLOW}📦 Création de l'environnement virtuel...${NC}"
    python3 -m venv christ
    echo -e "${GREEN}✅ Environnement virtuel créé${NC}"
else
    echo -e "${GREEN}✅ Environnement virtuel existant trouvé${NC}"
fi

echo ""

# Activer l'environnement virtuel
echo -e "${YELLOW}🔧 Activation de l'environnement virtuel...${NC}"
source christ/bin/activate

echo -e "${GREEN}✅ Environnement virtuel activé${NC}"
echo ""

# Installer les dépendances
echo -e "${YELLOW}📦 Installation des dépendances Python...${NC}"
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r api_gateway/requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erreur lors de l'installation des dépendances${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Dépendances installées avec succès${NC}"
echo ""

# Initialiser la base de données
echo -e "${YELLOW}🗄️  Initialisation de la base de données...${NC}"
cd api_gateway

# Vérifier si PostgreSQL est accessible
if command -v psql &> /dev/null; then
    echo -e "${GREEN}✅ PostgreSQL trouvé${NC}"
else
    echo -e "${YELLOW}⚠️  PostgreSQL n'est pas installé ou n'est pas dans le PATH${NC}"
    echo -e "${YELLOW}   Assurez-vous que PostgreSQL est installé et en cours d'exécution${NC}"
fi

echo ""

# Créer la base de données (optionnel)
read -p "Voulez-vous créer/réinitialiser la base de données? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python init_db.py
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ Erreur lors de l'initialisation de la base de données${NC}"
        echo -e "${YELLOW}⚠️  Vérifiez que PostgreSQL est en cours d'exécution${NC}"
    else
        echo -e "${GREEN}✅ Base de données initialisée avec succès${NC}"
    fi
else
    echo -e "${YELLOW}⏭️  Initialisation de la base de données ignorée${NC}"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo -e "${GREEN}║  ✨ Installation terminée avec succès!            ║${NC}"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${YELLOW}📋 Prochaines étapes:${NC}"
echo ""
echo -e "${GREEN}1. Démarrer le serveur FastAPI:${NC}"
echo "   cd backend/api_gateway"
echo "   python main.py"
echo ""
echo -e "${GREEN}2. Accéder au frontend (dans un autre terminal):${NC}"
echo "   cd frontend"
echo "   python -m http.server 8080"
echo ""
echo -e "${GREEN}3. Ouvrir votre navigateur:${NC}"
echo "   http://localhost:8080"
echo ""
echo -e "${YELLOW}🔐 Identifiants par défaut:${NC}"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo -e "${YELLOW}📚 Documentation API:${NC}"
echo "   http://localhost:8000/docs"
echo ""
