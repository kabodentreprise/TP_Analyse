# 🚀 COMMANDES RAPIDES - DÉPLOIEMENT

## 📝 RÉSUMÉ COMPLET - TOUTES LES COMMANDES

### Phase 1: Préparation Locale (5 min)

```bash
# Aller dans le dossier du projet
cd /home/otcbot/Bureau/TP_projet

# Activez l'environnement virtuel
cd backend
source christ/bin/activate

# Installez les dépendances
pip install -r api_gateway/requirements.txt

# Retour à la racine
cd ..
```

### Phase 2: Tests Locaux avec Docker (2 min)

```bash
# Lancer tous les services (Frontend + Backend + PostgreSQL)
docker-compose up

# Accès:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# PostgreSQL: localhost:5432
```

### Phase 3: Initialiser Git (2 min)

```bash
# Initialiser le repository
bash init-git.sh

# Créer un repository sur GitHub (https://github.com/new)
# Puis exécuter:
git remote add origin https://github.com/votre-username/repo-name.git
git branch -M main
git push -u origin main
```

### Phase 4: Déployer Backend sur Railway (5 min)

Via https://railway.app:

1. Créer un compte Railway
2. New Project → Deploy from GitHub repo
3. Ajouter PostgreSQL
4. Configurer variables (voir ci-dessous)
5. Root Directory: `backend/api_gateway`
6. Déployer ✓

**Variables Railway:**
```env
DATABASE_URL=postgresql://user:pass@host:5432/railway (auto-généré)
SECRET_KEY=<générer avec: python3 -c "import secrets; print(secrets.token_urlsafe(32))">
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
FRONTEND_URL=https://votre-app.vercel.app
DEBUG=False
```

### Phase 5: Déployer Frontend sur Vercel (5 min)

Via https://vercel.com:

1. Créer un compte Vercel
2. Import Project → GitHub repo
3. Root Directory: `frontend`
4. Ajouter variable: `VITE_API_URL=https://votre-backend-railway.up.railway.app`
5. Deploy ✓

### Phase 6: Tester

```bash
# Ouvrir votre application
https://votre-app.vercel.app

# Tests:
- S'inscrire (Register)
- Se connecter (Login)
- Vérifier le dashboard
```

---

## 🔑 GÉNÉRER UNE CLÉ SECRÈTE

```bash
# Python
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# OpenSSL
openssl rand -hex 32

# Linux
head -c 32 /dev/urandom | base64
```

---

## 📊 COMMANDES GIT COURANTES

```bash
# Vérifier le status
git status

# Voir l'historique
git log --oneline -10

# Faire un commit
git add .
git commit -m "Description du changement"
git push origin main

# Voir les branches
git branch -a

# Créer une nouvelle branche
git checkout -b feature/nouvelle-feature
```

---

## 🐳 COMMANDES DOCKER

```bash
# Lancer les services
docker-compose up

# Arrêter les services
docker-compose down

# Voir les logs
docker-compose logs backend
docker-compose logs postgres
docker-compose logs frontend

# Reconstruire les images
docker-compose build

# Lancer en arrière-plan
docker-compose up -d

# Accéder au conteneur
docker-compose exec backend bash
```

---

## 📚 DOCUMENTATION COMPLÈTE

- **START_HERE.md** - Plan complet (⭐ commencez ici)
- **GUIDE_DEPLOIEMENT.md** - Guide étape par étape
- **VARIABLES_ENVIRONNEMENT.md** - Configuration des variables
- **DEPLOYMENT_CHECKLIST.md** - Checklist de vérification
- **README_DEPLOYMENT.md** - Vue d'ensemble du projet

---

## ✅ CHECKLIST RAPIDE

Avant de déployer:
    └─→ [Connexion] login.html
         └─→ Se connecter avec JWT
              ↓
              ├─→ [Dashboard Admin] → Voir stats + Gérer utilisateurs
              │    └─→ usermanager.html (Modifier les rôles)
              │
              ├─→ [Dashboard Employé] → Interface employé
              │
              └─→ [Dashboard Client] → Interface client
```

## 🗂️ Structure des fichiers créés

```
TP_projet/
├── backend/
│   └── api_gateway/
│       ├── models.py           ✨ Modèle User SQLAlchemy
│       ├── schemas.py          ✨ Schémas Pydantic
│       ├── auth_routes.py      ✨ Routes d'authentification
│       ├── init_db.py          ✨ Script d'initialisation BD
│       ├── database.py         (existant)
│       ├── main.py             (modifié)
│       ├── requirements.txt    (modifié)
│       └── .env                (modifié)
│
├── frontend/
│   ├── index.html              ✨ Page d'accueil
│   ├── register.html           ✨ Inscription
│   ├── login.html              ✨ Connexion
│   ├── dashboard.html          ✨ Tableaux de bord
│   ├── usermanager.html        ✨ Gestion des utilisateurs
│   ├── styles.css              ✨ Styles globaux
│   └── app.js                  ✨ Logique partagée
│
├── start.sh                    ✨ Script de démarrage
├── Dockerfile                  ✨ Pour Docker
├── docker-compose.yml          ✨ Pour Docker Compose
├── README.md                   (modifié)
└── QUICKSTART.md               ✨ Ce fichier

✨ = Fichiers créés/modifiés pour ce projet
```

## 🚀 Avec Docker (optionnel)

```bash
docker-compose up -d
```

Alors accédez à :
- API: http://localhost:8000
- Frontend: http://localhost:80

## 📝 Caractéristiques principales

| Fonctionnalité | Description |
|---|---|
| 🔐 JWT Authentication | Tokens sécurisés avec expiration |
| 👥 Rôles Multi-niveaux | Admin, Employé, Client |
| 🗄️ PostgreSQL | Base de données relationnelle |
| 🔒 Password Hashing | Bcrypt pour sécuriser les mots de passe |
| 📱 Responsive Design | Fonctionne sur tous les appareils |
| 🔍 Recherche temps réel | Filtrer les utilisateurs instantanément |
| 🎨 UI Modern | Interface utilisateur propre et intuitive |

## 🔧 Configuration importante

**Fichier `.env`:**
```env
ENV=Dev
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=user_management
SECRET_KEY=your-secret-key-change-in-production
```

⚠️ **Changez la clé SECRET_KEY en production !**

## 📚 API Documentation

Une fois le serveur démarré, consultez:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🆘 Dépannage

### ❌ "Impossible de résoudre l'importation sqlalchemy"
**Solution**: C'est normal si l'environnement virtuel n'est pas activé dans VS Code. Utilisez le terminal du projet pour exécuter.

### ❌ "Connection refused"
**Solution**: Vérifiez que:
- PostgreSQL est en cours d'exécution
- Les identifiants en `.env` sont corrects
- Le port 5432 n'est pas utilisé

### ❌ "CORS error"
**Solution**: 
- Vérifiez que le backend est en cours d'exécution
- Vérifiez que les URLs dans `app.js` sont correctes

## 📞 Besoin d'aide?

1. Consultez le `README.md` pour plus de détails
2. Vérifiez les logs du serveur
3. Assurez-vous que PostgreSQL est installé et en cours d'exécution

---

**Prêt à démarrer? C'est parti! 🚀**
