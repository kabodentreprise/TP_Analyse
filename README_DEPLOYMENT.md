# 👥 Système de Gestion des Utilisateurs

Un application complète de gestion des utilisateurs avec rôles (Admin, Employés, Clients) développée avec **FastAPI**, **PostgreSQL** et **HTML/CSS**.

![Badge Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/fastapi-latest-blue)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue)

---

## 🎯 Fonctionnalités

✅ **Authentification & Autorisation**
- Inscription et connexion sécurisées
- JWT tokens pour les sessions
- Contrôle d'accès par rôles

✅ **Gestion des Utilisateurs**
- 3 rôles : Admin, Employé, Client
- Interface de gestion pour admin
- Changement de rôle

✅ **Interface Utilisateur**
- Pages : Login, Register, Dashboard, User Manager
- Responsive et intuitive
- Styles modernes CSS

✅ **Base de Données**
- PostgreSQL avec SQLAlchemy ORM
- Migrations Alembic
- Schema sécurisé

---

## 🚀 Déploiement

### Frontend (Vercel)
```bash
# Automatiquement déployé depuis le dossier `/frontend`
https://votre-app.vercel.app
```

### Backend (Railway + PostgreSQL)
```bash
# Automatiquement déployé depuis le dossier `/backend/api_gateway`
https://votre-projet-random.railway.app
```

**[📖 Guide de déploiement complet](./GUIDE_DEPLOIEMENT.md)**

---

## 🏗️ Architecture du Projet

```
TP_projet/
├── frontend/                 # Application web statique
│   ├── index.html           # Page d'accueil
│   ├── login.html           # Connexion
│   ├── register.html        # Inscription
│   ├── dashboard.html       # Tableau de bord personnel
│   ├── usermanager.html     # Gestion des utilisateurs
│   └── styles.css           # Styles globaux
│
├── backend/
│   └── api_gateway/         # API FastAPI
│       ├── main.py          # Application principale
│       ├── models.py        # Modèles SQLAlchemy
│       ├── schemas.py       # Schémas Pydantic
│       ├── database.py      # Configuration BD
│       ├── auth_routes.py   # Routes authentification
│       ├── admin_routes.py  # Routes admin
│       ├── client_route.py  # Routes client
│       ├── employer_route.py # Routes employé
│       ├── security.py      # Fonctions de sécurité
│       ├── init_db.py       # Initialisation BD
│       └── requirements.txt # Dépendances Python
│
├── docker-compose.yml        # Développement local
├── Dockerfile.backend        # Image Docker backend
├── Procfile                  # Pour Heroku/Render
├── railway.json             # Configuration Railway
└── GUIDE_DEPLOIEMENT.md     # Guide complet
```

---

## 🛠️ Installation Locale

### Prérequis
- Python 3.10+
- PostgreSQL 15+
- Git

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/tp-projet.git
cd tp-projet
```

2. **Configurer le backend**
```bash
cd backend
python3 -m venv christ
source christ/bin/activate  # Linux/Mac
# ou : christ\Scripts\activate  # Windows

pip install -r api_gateway/requirements.txt
```

3. **Configurer la base de données**
```bash
cp api_gateway/.env.example api_gateway/.env
# Éditer .env avec vos paramètres
cd api_gateway
python init_db.py
```

4. **Lancer le backend**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

5. **Accéder au frontend**
```bash
# Terminal 2
cd frontend
python -m http.server 3000
# Ouvrir http://localhost:3000
```

---

## 🐳 Avec Docker Compose

```bash
# Démarrer tous les services
docker-compose up

# Arrêter les services
docker-compose down
```

Services disponibles :
- Frontend : http://localhost:3000
- Backend : http://localhost:8000
- PostgreSQL : localhost:5432
- Docs API : http://localhost:8000/docs

---

## 📊 Modèle de Données

### Table Utilisateurs

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100),
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    is_employer BOOLEAN DEFAULT FALSE,
    is_client BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🔑 Variables d'Environnement

Créer un fichier `.env` dans `backend/api_gateway/` :

```env
# Base de données
DATABASE_URL=postgresql://user:password@localhost:5432/gestion_users

# Sécurité
SECRET_KEY=your-secret-key-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Emails (optionnel)
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_FROM=your-email@gmail.com

# URLs
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000

# Mode
DEBUG=True
```

---

## 📡 Endpoints API

### Authentification
- `POST /api/register` - Créer un compte
- `POST /api/login` - Se connecter
- `GET /api/me` - Récupérer l'utilisateur actuel

### Admin
- `GET /api/admin/users` - Lister tous les utilisateurs
- `PUT /api/admin/users/{id}/role` - Changer le rôle d'un utilisateur
- `DELETE /api/admin/users/{id}` - Supprimer un utilisateur

### Utilisateurs
- `GET /api/users/profile` - Profil personnel
- `PUT /api/users/profile` - Mettre à jour le profil

---

## 🧪 Tests

```bash
# Lancer les tests
pytest

# Avec coverage
pytest --cov=.
```

---

## 📝 Contribuer

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 📧 Support

Pour toute question ou problème, créer une [issue](https://github.com/votre-username/tp-projet/issues).

---

## 🎓 Ressources Utiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Vercel Docs](https://vercel.com/docs)
- [Railway Documentation](https://docs.railway.app/)
- [PostgreSQL](https://www.postgresql.org/docs/)

---

**Fait avec ❤️ par ton équipe de développement**
