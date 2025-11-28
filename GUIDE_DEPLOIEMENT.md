# 🚀 Guide de Déploiement Complet

## Architecture du projet

```
┌─────────────────────────────────────────────────────────────┐
│                     GitHub Repository                        │
│  (Code source - Frontend + Backend + Configuration)          │
└─────────────────────────────────────────────────────────────┘
         │                              │
         ↓                              ↓
┌──────────────────┐        ┌──────────────────────┐
│  VERCEL (Front)  │        │  RAILWAY/RENDER      │
│  - HTML/CSS/JS   │        │  - FastAPI Backend   │
│  - Auto deploy   │        │  - PostgreSQL DB     │
│  - HTTPS         │        │  - Auto deploy       │
└──────────────────┘        └──────────────────────┘
```

## 📝 Étape 1 : Initialiser le Repository GitHub

```bash
# Dans le dossier racine du projet
cd /home/otcbot/Bureau/TP_projet

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Faire un commit initial
git commit -m "Initial commit: User Management System"

# Ajouter l'URL du repository
git remote add origin https://github.com/votre-username/nom-repo.git

# Pousser sur GitHub
git branch -M main
git push -u origin main
```

## 🌐 Étape 2 : Déployer le Backend sur Railway.app

### 2.1 Créer un compte Railway
1. Aller sur [railway.app](https://railway.app)
2. S'inscrire avec GitHub

### 2.2 Créer un nouveau projet
1. Cliquer sur "New Project"
2. Sélectionner "Deploy from GitHub repo"
3. Autoriser Railway à accéder à vos repositories
4. Sélectionner votre repository

### 2.3 Ajouter PostgreSQL
1. Cliquer sur "Add Service"
2. Choisir "PostgreSQL"
3. Railway crée automatiquement la base de données

### 2.4 Configurer les variables d'environnement
1. Aller à l'onglet "Variables"
2. Ajouter ces variables :

```env
DATABASE_URL=postgresql://username:password@host:5432/railway
SECRET_KEY=your-super-secret-key-min-32-characters-random
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
FRONTEND_URL=https://votre-app-vercel.vercel.app
DEBUG=False
```

### 2.5 Configurer le serveur
1. Aller à l'onglet "Settings"
2. Définir "Root Directory" : `backend/api_gateway`
3. Définir "Start Command" : `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Cliquer sur "Deploy"

**URL du backend** : `https://votre-projet-random.railway.app`

---

## 💎 Étape 3 : Déployer le Frontend sur Vercel

### 3.1 Créer un compte Vercel
1. Aller sur [vercel.com](https://vercel.com)
2. S'inscrire avec GitHub

### 3.2 Importer le projet
1. Cliquer sur "Import Project"
2. Sélectionner "Import Git Repository"
3. Entrer l'URL de votre repo GitHub
4. Vercel détecte automatiquement que c'est un projet statique

### 3.3 Configurer l'environnement
1. Dans "Environment Variables", ajouter :

```env
VITE_API_URL=https://votre-projet-random.railway.app
```

### 3.4 Configuration du projet
1. Root Directory : `frontend`
2. Build Command : (laisser vide pour HTML statique)
3. Install Command : `npm install` (optionnel)
4. Cliquer sur "Deploy"

**URL du frontend** : `https://votre-app.vercel.app`

---

## 🔄 Étape 4 : Activer le déploiement automatique

### GitHub Actions (CI/CD automatique)

Créez un fichier `.github/workflows/deploy.yml` :

```yaml
name: Deploy on Push

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy notification
        run: echo "Deployment triggered on push to main"
```

---

## 📋 Checklist avant le déploiement

- [ ] Repository GitHub créé et configuré
- [ ] Fichier `.env.example` complété
- [ ] `requirements.txt` à jour
- [ ] Tests locaux réussis (Docker)
- [ ] Base de données migrée
- [ ] URL CORS configurée sur le backend
- [ ] Variables d'environnement définies sur Railway
- [ ] Variables d'environnement définies sur Vercel
- [ ] Test du déploiement du backend
- [ ] Test du déploiement du frontend
- [ ] Test complet d'authentification entre front et back

---

## 🧪 Tests locaux avant déploiement

```bash
# Démarrer avec Docker Compose
docker-compose up

# Tester le backend
curl http://localhost:8000/docs

# Tester le frontend
open http://localhost:3000
```

---

## 🔧 Mise à jour après déploiement

Pour mettre à jour l'application :

```bash
# Faire vos modifications
git add .
git commit -m "Description des changements"
git push origin main

# Railway et Vercel redéploient automatiquement !
```

---

## 🆘 Dépannage

### Backend ne démarre pas sur Railway
- Vérifier les logs : Rail > Settings > Logs
- Vérifier DATABASE_URL est correctement défini
- Vérifier que `requirements.txt` contient toutes les dépendances

### Frontend ne se connecte pas au backend
- Vérifier VITE_API_URL sur Vercel
- Vérifier CORS sur le backend
- Vérifier la console du navigateur pour les erreurs

### Erreur de base de données
- Vérifier que PostgreSQL est déployé sur Railway
- Vérifier les identifiants dans DATABASE_URL
- Tester la connexion localement d'abord

---

## 📊 Coûts mensuels estimés

| Service | Plan | Coût |
|---------|------|------|
| Railway | Starter | $5-20 |
| Vercel | Hobby | $0 (gratuit) |
| PostgreSQL (Railway) | Inclus | Inclus |
| **Total** | | **$5-20/mois** |

---

## 🎯 Prochaines étapes

1. [ ] Configurer un domaine personnalisé
2. [ ] Ajouter SSL/HTTPS (automatique sur Vercel)
3. [ ] Configurer les backups de base de données
4. [ ] Mettre en place le monitoring (Sentry)
5. [ ] Ajouter les tests automatiques
