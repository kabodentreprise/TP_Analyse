# 🎯 Système de Gestion des Utilisateurs

Un projet complet avec Backend FastAPI et Frontend HTML/CSS/JavaScript pour la gestion des utilisateurs avec système de rôles (Admin, Employé, Client).

## 📋 Fonctionnalités

✅ **Authentification & Inscription**
- Page d'inscription avec validation
- Page de connexion avec JWT
- Gestion des tokens d'accès

✅ **Gestion des Rôles**
- 3 rôles disponibles : Admin, Employé, Client
- Système de permissions basé sur les rôles
- Interface admin pour modifier les rôles

✅ **Tableaux de bord personnalisés**
- Dashboard Admin : Statistiques et gestion des utilisateurs
- Dashboard Employé : Interface dédiée
- Dashboard Client : Interface client
- Redirection automatique selon le rôle

✅ **Interface Admin (usermanager.html)**
- Liste complète des utilisateurs
- Recherche en temps réel
- Modification des rôles via modal
- Désactivation des comptes
- Filtrage par état et rôles

## 🏗️ Architecture du Projet

```
backend/
├── api_gateway/
│   ├── models.py              # Modèle SQLAlchemy User
│   ├── schemas.py             # Schémas Pydantic
│   ├── auth_routes.py         # Routes d'authentification
│   ├── database.py            # Configuration base de données
│   ├── main.py                # Application FastAPI
│   ├── requirements.txt        # Dépendances Python
│   └── .env                   # Variables d'environnement

frontend/
├── index.html                 # Page d'accueil
├── register.html              # Inscription
├── login.html                 # Connexion
├── dashboard.html             # Tableaux de bord
├── usermanager.html           # Gestion des utilisateurs (Admin)
├── styles.css                 # Feuilles de style
└── app.js                     # Logique commune JavaScript
```

## 🗄️ Schéma de la Base de Données

### Table `users`
```sql
id              INTEGER PRIMARY KEY
username        VARCHAR(50) UNIQUE NOT NULL
email           VARCHAR(100) UNIQUE NOT NULL
password_hash   VARCHAR(255) NOT NULL
first_name      VARCHAR(50)
last_name       VARCHAR(50)
phone           VARCHAR(20)
is_admin        BOOLEAN DEFAULT FALSE
is_employer     BOOLEAN DEFAULT FALSE
is_client       BOOLEAN DEFAULT FALSE
is_active       BOOLEAN DEFAULT TRUE
created_at      DATETIME DEFAULT NOW()
updated_at      DATETIME DEFAULT NOW()
```

## 🚀 Installation et Démarrage

### 1️⃣ Configuration du Backend

```bash
# Accéder au dossier backend
cd backend/

# Activer l'environnement virtuel (Linux/Mac)
source christ/bin/activate

# Ou sur Windows
christ\Scripts\activate

# Installer les dépendances
pip install -r api_gateway/requirements.txt
```

### 2️⃣ Configuration de la Base de Données

Assurez-vous que PostgreSQL est installé et en cours d'exécution.

```bash
# Créer une base de données
createdb user_management

# Mettre à jour le fichier .env avec vos identifiants
```

### 3️⃣ Lancer le Backend

```bash
cd backend/api_gateway/
python main.py
```

Le serveur démarrera sur : `http://localhost:8000`

### 4️⃣ Lancer le Frontend

Ouvrez le fichier `frontend/index.html` dans votre navigateur, ou utilisez un serveur local :

```bash
# Avec Python
cd frontend/
python -m http.server 8080

# Ou avec Node.js
npx http-server -p 8080
```

Accédez à : `http://localhost:8080`

## 👥 Cas d'Usage

### 1. **Inscription d'un nouvel utilisateur**
- Aller sur `/register.html`
- Remplir le formulaire
- Choisir le type de compte (Client/Employé)
- Soumettre

### 2. **Connexion**
- Aller sur `/login.html`
- Entrer identifiants
- Token JWT stocké automatiquement
- Redirection vers le dashboard approprié

### 3. **Gestion des utilisateurs (Admin)**
- Se connecter avec un compte admin
- Accéder à `/usermanager.html`
- Rechercher les utilisateurs
- Modifier les rôles via le modal
- Désactiver les comptes si nécessaire

## 🔐 Sécurité

- Passwords hashés avec bcrypt
- JWT pour l'authentification
- CORS configuré
- Validation des entrées avec Pydantic
- Permissions basées sur les rôles

## 📡 API Endpoints

### Authentification
```
POST /api/auth/register          # Inscription
POST /api/auth/login             # Connexion
GET  /api/auth/me                # Infos utilisateur actuel
```

### Gestion des Utilisateurs (Admin)
```
GET    /api/users                # Tous les utilisateurs
GET    /api/users/{id}           # Détails utilisateur
PUT    /api/users/{id}/roles     # Modifier les rôles
DELETE /api/users/{id}           # Désactiver un utilisateur
```

## 🎨 Design & Responsive

- CSS moderne et responsive
- Layouts flexibles
- Thème cohérent avec couleurs primaires
- Support mobile

## 🛠️ Technologies Utilisées

**Backend:**
- FastAPI
- SQLAlchemy
- PostgreSQL
- PyJWT
- Passlib

**Frontend:**
- HTML5
- CSS3
- JavaScript (Vanilla)
- LocalStorage pour les tokens

## 📝 Variables d'Environnement (.env)

```env
ENV=Dev
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=user_management
SECRET_KEY=your-secret-key
```

## ⚠️ Notes Importantes

1. **Créer un compte admin**: 
   - Inscrivez-vous d'abord
   - Accédez à la base de données et modifiez `is_admin = TRUE` pour le premier compte

2. **CORS**: Actuellement permissif (`*`). À restreindre en production.

3. **Secret Key**: Changez la valeur en production !

4. **Base de données**: Adapter les identifiants dans `.env`

## 🐛 Troubleshooting

**Erreur: `Impossible de résoudre l'importation`**
- Les imports affichent des erreurs, mais c'est normal si l'environnement virtuel n'est pas activé dans VS Code

**Erreur: `CORS error`**
- Vérifier que le backend est en cours d'exécution
- Vérifier les URLs dans `app.js`

**Erreur: `Connection refused`**
- Vérifier que PostgreSQL est en cours d'exécution
- Vérifier les identifiants en `.env`

## 📚 Prochaines Étapes

- [ ] Ajouter des roles supplémentaires
- [ ] Implémenter un système d'audit
- [ ] Ajouter des notifications par email
- [ ] Implémenter un système de permission plus granulaire
- [ ] Tests unitaires
- [ ] Documentation Swagger (automatique avec FastAPI)

## 📞 Support

Pour des questions, consultez la documentation de:
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- JWT: https://python-jose.readthedocs.io/

---
**Auteur:** Système de Gestion  
**Version:** 1.0.0  
**Date:** 28 Novembre 2025
