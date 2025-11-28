# Configuration de déploiement du Backend

## 🚀 Options de déploiement du Backend

### Option 1 : Railway.app (RECOMMANDÉ - Simple et gratuit)
1. Créer un compte sur https://railway.app
2. Connecter votre GitHub
3. Créer un nouveau projet Railway
4. Ajouter PostgreSQL comme service
5. Déployer depuis votre repo GitHub
6. Railway crée automatiquement les variables d'environnement

### Option 2 : Render.com
1. Créer un compte sur https://render.com
2. Connecter GitHub
3. Créer une Web Service
4. Ajouter PostgreSQL Database
5. Variables d'environnement configurées automatiquement

### Option 3 : Heroku (ancien gratuit, maintenant payant)
1. `heroku login`
2. `heroku create votre-app-name`
3. `heroku addons:create heroku-postgresql:standard-0`
4. `git push heroku main`

## 📋 Variables d'environnement requises

```
DATABASE_URL=postgresql://user:password@host:port/dbname
SECRET_KEY=votre_clé_secrète_très_longue
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MAIL_USERNAME=votre_email@gmail.com
MAIL_PASSWORD=votre_app_password
MAIL_FROM=votre_email@gmail.com
FRONTEND_URL=https://votre-frontend-vercel.vercel.app
```

## 🔗 Intégration avec le Frontend

Sur Vercel, ajouter la variable d'environnement :
```
VITE_API_URL=https://votre-backend-railway.up.railway.app
```

## 📝 Structure des fichiers de déploiement

- `Dockerfile` : Pour containerisation
- `docker-compose.yml` : Pour développement local
- `requirements.txt` : Dépendances Python
- `.env.example` : Template des variables d'environnement
