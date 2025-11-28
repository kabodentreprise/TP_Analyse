# ✅ CHECKLIST DE DÉPLOIEMENT

## Avant de commencer

- [ ] Vous avez une connexion Internet stable
- [ ] Git est installé sur votre machine
- [ ] Python 3.10+ est installé
- [ ] Docker est installé (optionnel mais recommandé)

## Phase 1: Préparation GitHub (5 min)

- [ ] Créer un compte GitHub: https://github.com/signup
- [ ] Créer un nouveau repository public ou privé
- [ ] Copier l'URL du repository (format: https://github.com/username/repo.git)
- [ ] Initialiser Git localement: `bash init-git.sh`
- [ ] Pousser le code: `git push -u origin main`

## Phase 2: Configuration Backend (5 min)

### Sur Railway:

- [ ] Créer un compte Railway: https://railway.app
- [ ] Créer un nouveau projet
- [ ] Connecter votre repository GitHub
- [ ] Ajouter le service PostgreSQL
- [ ] Vérifier que DATABASE_URL est auto-généré
- [ ] Ajouter les variables d'environnement:
  - [ ] SECRET_KEY (clé secrète aléatoire >32 chars)
  - [ ] ALGORITHM: HS256
  - [ ] ACCESS_TOKEN_EXPIRE_MINUTES: 30
  - [ ] FRONTEND_URL: https://votre-app.vercel.app (sera complété plus tard)
  - [ ] DEBUG: False

### Configuration Railway:

- [ ] Root Directory: `backend/api_gateway`
- [ ] Build Command: Automatique
- [ ] Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Attendre que le déploiement soit ✓ (vert)

### Après déploiement:

- [ ] Copier l'URL du backend (format: https://votre-projet-xxx.railway.app)
- [ ] Tester: Visiter https://votre-projet-xxx.railway.app/docs
- [ ] Vérifier que la documentation Swagger s'affiche

## Phase 3: Configuration Frontend (5 min)

### Sur Vercel:

- [ ] Créer un compte Vercel: https://vercel.com
- [ ] Importer votre repository GitHub
- [ ] Définir Root Directory: `frontend`
- [ ] S'assurer que Build Command est vide (site statique)
- [ ] Ajouter la variable d'environnement:
  - [ ] VITE_API_URL = https://votre-projet-xxx.railway.app
- [ ] Déployer

### Après déploiement:

- [ ] Copier l'URL du frontend (format: https://votre-app.vercel.app)
- [ ] Visiter https://votre-app.vercel.app
- [ ] Vérifier que le site s'affiche

## Phase 4: Mise à jour des URLs croisées (2 min)

### Mettre à jour Railway:

- [ ] Aller dans Settings → Variables
- [ ] Éditer FRONTEND_URL: https://votre-app.vercel.app
- [ ] Sauvegarder (redéploiement automatique)
- [ ] Attendre que le déploiement soit complété

### Vérifier:

- [ ] Les deux services sont maintenant reliés
- [ ] CORS devrait fonctionner

## Phase 5: Tests Complets (5 min)

### Test d'authentification:

- [ ] Aller sur https://votre-app.vercel.app
- [ ] Cliquer sur "Register" ou "S'inscrire"
- [ ] Créer un compte:
  - [ ] Username: testuser
  - [ ] Email: test@example.com
  - [ ] Password: TestPassword123!
  - [ ] Soumettre
- [ ] Vérifier que vous êtes redirigé vers la page de connexion
- [ ] Vous connecter avec les identifiants créés
- [ ] Vérifier que vous êtes redirigé vers le dashboard

### Test des fonctionnalités:

- [ ] (Client) Voir votre profil dans le dashboard
- [ ] (Employer) Voir votre tableau de bord employé
- [ ] (Admin) Accéder à la page de gestion des utilisateurs

### Tests des API:

- [ ] Visiter https://votre-projet-xxx.railway.app/docs
- [ ] Tester les endpoints:
  - [ ] POST /api/register
  - [ ] POST /api/login
  - [ ] GET /api/me (après login)
  - [ ] GET /api/admin/users (si admin)

## Phase 6: Monitoring (2 min)

### Vérifier les logs:

- [ ] Railway Dashboard → Deployments → Logs
  - [ ] Pas d'erreurs?
  - [ ] Application running?
- [ ] Vercel Dashboard → Deployments → Logs
  - [ ] Build réussi?
  - [ ] Pas d'erreurs?

### Vérifier les variables:

- [ ] Railway: Toutes les variables sont défini
- [ ] Vercel: VITE_API_URL pointe vers Railway
- [ ] Pas de secrets dans le code

## Phase 7: Sécurité (Avant de partager)

- [ ] `.env` est dans `.gitignore` ✓
- [ ] Pas de SECRET_KEY en dur dans le code ✓
- [ ] DATABASE_URL ne contient pas le mot de passe visible ✓
- [ ] HTTPS activé (automatique) ✓
- [ ] CORS configurés correctement ✓

## Phase 8: Documentation (2 min)

- [ ] Mettre à jour README.md avec les URLs de déploiement
- [ ] Ajouter les instructions d'installation locale
- [ ] Documenter les variables d'environnement utilisées
- [ ] Ajouter les endpoints API disponibles

## Phase 9: Déploiement Futurs (Optionnel)

- [ ] Comprendre que les futurs déploiements se font automatiquement
- [ ] À chaque `git push`:
  - [ ] GitHub reçoit le code
  - [ ] Railway redéploie le backend (5-10 min)
  - [ ] Vercel redéploie le frontend (1-2 min)
  - [ ] Les changements sont en live

## Phase 10: Performance & Optimisation (Optionnel)

- [ ] Vérifier le temps de réponse de l'API
- [ ] Activer les caches si nécessaire
- [ ] Ajouter des limits de rate sur les endpoints sensibles
- [ ] Monitorer l'usage PostgreSQL

## 🆘 Troubleshooting

Si le backend ne démarre pas:
- [ ] Vérifier les logs Railway
- [ ] Vérifier que DATABASE_URL est défini
- [ ] Vérifier que Secret_KEY est défini
- [ ] Tester localement: `docker-compose up`

Si le frontend ne se connecte pas:
- [ ] Vérifier la console du navigateur (F12)
- [ ] Vérifier VITE_API_URL sur Vercel
- [ ] Vérifier CORS sur Railway
- [ ] Vérifier que Railroad est opérationnel

Si les logs montrent des erreurs:
- [ ] Lire complètement le message d'erreur
- [ ] Chercher le message sur StackOverflow
- [ ] Consulter la documentation FastAPI/PostgreSQL
- [ ] Tester localement avec `docker-compose`

## ✅ Signaux que tout fonctionne

- ✓ Frontend s'affiche correctement
- ✓ Vous pouvez vous inscrire
- ✓ Vous pouvez vous connecter
- ✓ Vous voyez votre profil
- ✓ Admin peut voir tous les utilisateurs
- ✓ Pas d'erreurs 500 dans les logs

## 🎉 Félicitations!

Si vous avez coché toutes les cases, votre application est prête à être utilisée!

Pour les mises à jour futures, c'est aussi simple que:

```bash
git add .
git commit -m "Description du changement"
git push origin main
```

Et Railway/Vercel se chargent du reste! 🚀

---

**Questions?** Consultez GUIDE_DEPLOIEMENT.md ou VARIABLES_ENVIRONNEMENT.md
