# Configuration des Variables d'Environnement

## 🔐 Backend sur Railway

Ajouter ces variables dans le dashboard Railway (Variables tab):

```env
# Base de données (Auto-généré par Railway quand vous ajoutez PostgreSQL)
DATABASE_URL=postgresql://user:password@host:port/railway

# Sécurité - Générer une clé secrète aléatoire de min 32 caractères
SECRET_KEY=votre-clé-super-secrète-très-longue-aléatoire-min-32-chars

# Configuration JWT
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# URLs
FRONTEND_URL=https://votre-app.vercel.app
BACKEND_URL=https://votre-backend-railway.up.railway.app

# Debug
DEBUG=False
```

### Générer une clé secrète sécurisée:

```bash
# Méthode 1: Python
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# Méthode 2: OpenSSL
openssl rand -hex 32

# Méthode 3: Linux
head -c 32 /dev/urandom | base64
```

---

## 🌐 Frontend sur Vercel

Ajouter ces variables dans le dashboard Vercel (Settings → Environment Variables):

```env
VITE_API_URL=https://votre-backend-railway.up.railway.app
```

⚠️ **Important**: Cette variable doit être disponible au moment du build.

---

## 📧 Variables Email (Optionnel)

Si vous voulez utiliser l'envoi d'emails:

```env
# Gmail SMTP
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=votre-app-password  # Générer une app password depuis Gmail
MAIL_FROM=votre-email@gmail.com

# Ou un autre service SMTP
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_TLS=True
```

### Générer une App Password Gmail:

1. Aller à myaccount.google.com
2. Sécurité
3. Activer la vérification 2FA si nécessaire
4. Rechercher "App passwords"
5. Sélectionner "Mail" et "Windows Computer"
6. Copier le mot de passe généré

---

## ✅ Checklist

### Avant de déployer sur Railway:

- [ ] Base de données PostgreSQL créée sur Railway
- [ ] DATABASE_URL copié automatiquement
- [ ] SECRET_KEY générée et sécurisée
- [ ] FRONTEND_URL définie (votre domaine Vercel)
- [ ] Root Directory = `backend/api_gateway`
- [ ] Port = $PORT (variable d'environnement Railway)

### Avant de déployer sur Vercel:

- [ ] VITE_API_URL définie avec l'URL du backend Railway
- [ ] Root Directory = `frontend`
- [ ] Pas de build command pour HTML statique
- [ ] Framework = None (site statique)

### Avant le premier push:

- [ ] `.env` est dans `.gitignore` ✓
- [ ] `.env.example` a les bons champs
- [ ] `requirements.txt` est à jour
- [ ] Tous les fichiers sont committés

---

## 🧪 Test des Variables

Pour vérifier que les variables sont bien configurées:

### Backend:

```bash
# Aller dans le terminal Railway
cd backend/api_gateway
python -c "import os; print('DATABASE_URL:', os.getenv('DATABASE_URL')[:50] + '...')"
python -c "import os; print('SECRET_KEY OK' if len(os.getenv('SECRET_KEY', '')) > 30 else 'SECRET_KEY VIDE')"
```

### Frontend:

```bash
# Dans les logs Vercel Build
# Vous verrez les variables d'environnement
```

---

## 🆘 Problèmes Courants

### "MODULE NOT FOUND: fastapi"

- [ ] Vérifier que `requirements.txt` est complet
- [ ] Vérifier que Railway exécute `pip install -r requirements.txt`

### "CONNECTION REFUSED: postgres"

- [ ] Vérifier que PostgreSQL est déployé sur Railway
- [ ] Vérifier DATABASE_URL est correct
- [ ] Attendre que le conteneur PostgreSQL soit prêt

### "CORS ERROR: origin not allowed"

- [ ] Vérifier FRONTEND_URL sur Railway (doit être votre domaine Vercel)
- [ ] Vérifier les origins CORS dans main.py

### "TOKEN VERIFICATION FAILED"

- [ ] Vérifier que SECRET_KEY est identique partout
- [ ] Ne pas changer SECRET_KEY après déploiement (les tokens existants deviennent invalides)

---

## 🚀 Redéployer Après Changements

Pour redéployer avec de nouvelles variables:

1. **Railway**: Va automatiquement redéployer quand vous push sur GitHub
2. **Vercel**: Va automatiquement redéployer quand vous push sur GitHub

```bash
# Après modifier les variables ou le code:
git add .
git commit -m "Update configuration"
git push origin main

# Railway et Vercel vont déployer automatiquement
```

---

## 📊 Structure des Variables

```
Railway (Backend):
├── DATABASE_URL (Auto)
├── SECRET_KEY (Manuel - critique!)
├── ALGORITHM
├── ACCESS_TOKEN_EXPIRE_MINUTES
├── FRONTEND_URL
├── BACKEND_URL
└── DEBUG

Vercel (Frontend):
├── VITE_API_URL (Manuel - pointeur vers Railway)
└── Autres optionnels...
```

---

## 🔒 Sécurité

⚠️ **Règles Importantes**:

1. **JAMAIS** commiter `.env` sur GitHub
2. **TOUJOURS** mettre `.env` dans `.gitignore`
3. **JAMAIS** partager SECRET_KEY publiquement
4. **CHANGER** SECRET_KEY entre développement et production
5. **UTILISER** des variables différentes par environnement

---

**Besoin d'aide?** Consultez GUIDE_DEPLOIEMENT.md
