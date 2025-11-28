# 🚀 PLAN DE DÉPLOIEMENT COMPLET

## 📋 Vue d'ensemble

Votre projet va être déployé de cette manière :

```
GitHub Repository
    ↓
    ├─→ Frontend (HTML/CSS) → VERCEL
    │   URL: https://votre-app.vercel.app
    │
    └─→ Backend (FastAPI) → RAILWAY
        URL: https://votre-backend.railway.app
        DB: PostgreSQL (Railway)
```

---

## ⏱️ Estimé: 30 minutes de configuration

### Phase 1: Préparation (5 min)

```bash
# 1. Aller dans le dossier du projet
cd /home/otcbot/Bureau/TP_projet

# 2. Rendre les scripts exécutables
chmod +x init-git.sh deploy.sh SETUP.sh

# 3. Afficher le guide d'installation
bash SETUP.sh
```

### Phase 2: GitHub Setup (5 min)

1. Créer un compte GitHub (gratuit)
2. Créer un nouveau repository (privé ou public)
3. Noter l'URL: `https://github.com/votre-username/nom-repo.git`

### Phase 3: Initialiser Git Localement (5 min)

```bash
# Depuis la racine du projet
bash init-git.sh

# Configurer l'URL GitHub
git remote add origin https://github.com/votre-username/nom-repo.git
git branch -M main
git push -u origin main
```

### Phase 4: Déployer Backend sur Railway (5 min)

1. Créer un compte Railway (https://railway.app)
2. Créer un nouveau projet
3. Connecter votre repository GitHub
4. Ajouter PostgreSQL
5. Configurer les variables (voir VARIABLES_ENVIRONNEMENT.md)
6. Laisser Railway déployer
7. Copier l'URL du backend

### Phase 5: Déployer Frontend sur Vercel (5 min)

1. Créer un compte Vercel (https://vercel.com)
2. Importer votre repository GitHub
3. Définir Root Directory: `frontend`
4. Ajouter variable `VITE_API_URL` = URL du backend Railway
5. Cliquer Deploy
6. Copier l'URL du frontend

### Phase 6: Test & Finalisation (5 min)

1. Tester login/register sur votre app Vercel
2. Vérifier les logs sur Railway en cas de problème
3. Célébrer ! 🎉

---

## 📂 Fichiers de Configuration

| Fichier | Utilité | Pour qui |
|---------|---------|----------|
| `.gitignore` | Ignorer les fichiers sensibles | Git |
| `docker-compose.yml` | Développement local | Développeur |
| `Dockerfile.backend` | Container backend | Docker/Railway |
| `Procfile` | Instructions de lancement | Heroku/Render |
| `railway.json` | Configuration Railway | Railway |
| `.env.example` | Template variables | Référence |
| `.github/workflows/tests.yml` | CI/CD automatique | GitHub Actions |
| `VARIABLES_ENVIRONNEMENT.md` | Guide des variables | Admin |
| `GUIDE_DEPLOIEMENT.md` | Guide détaillé | Tous |

---

## 🔧 Architecture du Déploiement

### Base de Données
```
Railway PostgreSQL (Cloud Database)
↑
│ DATABASE_URL
│
Backend FastAPI (Railway Container)
```

### Frontend
```
Vercel Static Files (Optimisé pour frontend)
↓
Index.html, styles.css, login.html, etc.
```

### Communication
```
Frontend (Vercel)
    │
    ├─→ Requêtes API
    │
    Backend (Railway)
        │
        ├─→ Requêtes DB
        │
        PostgreSQL (Railway)
```

---

## 🔐 Sécurité

✅ Checklist de sécurité:

- [ ] `.env` est dans `.gitignore`
- [ ] Pas de SECRET_KEY en dur dans le code
- [ ] DATABASE_URL ne contient pas le mot de passe en clair (optionnel)
- [ ] CORS configurés correctement
- [ ] HTTPS activé (automatique sur Vercel et Railway)
- [ ] SECRET_KEY est unique et longue (>32 caractères)
- [ ] Variables sensibles stockées uniquement dans Railway/Vercel

---

## 📈 Coûts Estimés

| Service | Plan | Coût/mois |
|---------|------|-----------|
| Railway | Starter | $5-10 |
| Vercel | Hobby | $0 (gratuit) |
| Domaine personnalisé | Optional | $12+ |
| **Total** | | **$5-10** |

💡 Les deux services offrent un tier gratuit pour commencer !

---

## ✅ Tests Avant Déploiement

### Localement

```bash
# Terminal 1 - Backend
cd backend/api_gateway
source ../christ/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
python -m http.server 3000

# Terminal 3 - Tester
curl http://localhost:8000/docs  # API OK?
open http://localhost:3000       # Frontend OK?
```

### Avec Docker

```bash
docker-compose up

# Attendre que tout soit prêt
# Visiter:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:8000
# - Docs: http://localhost:8000/docs
```

---

## 🎯 Objectifs à Atteindre

Après le déploiement, vous devriez pouvoir:

✅ S'inscrire sur l'app publique  
✅ Se connecter avec vos identifiants  
✅ Voir votre tableau de bord personnel  
✅ (Admin) Gérer les rôles des utilisateurs  
✅ (Développeur) Modifier le code et redéployer automatiquement  

---

## 📞 Support & Dépannage

### En cas de problème:

1. **Vérifier les logs:**
   - Railway: Dashboard → Deployment → Logs
   - Vercel: Dashboard → Deployments → Logs

2. **Vérifier les variables d'environnement:**
   - Voir `VARIABLES_ENVIRONNEMENT.md`

3. **Consulter les ressources:**
   - GUIDE_DEPLOIEMENT.md (complet)
   - README_DEPLOYMENT.md (vue d'ensemble)

4. **Tester localement:**
   ```bash
   docker-compose up
   # Reproduire le problème en local
   ```

---

## 🎓 Ressources

- [Railway Documentation](https://docs.railway.app/)
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [PostgreSQL Best Practices](https://www.postgresql.org/docs/)

---

## 🎉 Résumé Rapide

```
1. bash init-git.sh                    # Initialiser Git
2. Créer repository GitHub             # Créer repo
3. git push origin main                # Pousser le code
4. Créer compte Railway                # DB + Backend
5. Créer compte Vercel                 # Frontend
6. Configurer variables                # Secrets
7. Attendre les déploiements           # Auto
8. Tester sur votre app !              # Fonctionnel
```

---

**Prêt à déployer ? Commencez par: `bash SETUP.sh`** 🚀
