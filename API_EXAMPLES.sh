"""
EXEMPLES DE REQUÊTES API - SYSTÈME DE GESTION DES UTILISATEURS

Ce fichier contient des exemples de requêtes cURL et fetch()
pour tester l'API directement.
"""

# ═══════════════════════════════════════════════════════════════
# 1. AUTHENTIFICATION
# ═══════════════════════════════════════════════════════════════

# 1.1 INSCRIPTION - Créer un nouveau compte
echo "▶️  POST /api/auth/register"
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "06 12 34 56 78",
    "is_client": true,
    "is_employer": false
  }'

# Réponse attendue:
# {
#   "id": 1,
#   "username": "johndoe",
#   "email": "john@example.com",
#   "first_name": "John",
#   "last_name": "Doe",
#   "phone": "06 12 34 56 78",
#   "is_admin": false,
#   "is_employer": false,
#   "is_client": true,
#   "is_active": true,
#   "created_at": "2025-11-28T03:30:00"
# }


# 1.2 CONNEXION - Obtenir un token JWT
echo "▶️  POST /api/auth/login"
TOKEN=$(curl -s -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }' | jq -r '.access_token')

echo "Token obtenu: $TOKEN"

# Réponse attendue:
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "token_type": "bearer",
#   "user": {
#     "id": 1,
#     "username": "johndoe",
#     "email": "john@example.com",
#     ...
#   }
# }


# 1.3 OBTENIR MES INFOS - Récupérer mes informations
echo "▶️  GET /api/auth/me"
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer $TOKEN"

# Réponse attendue: Les informations du l'utilisateur connecté


# ═══════════════════════════════════════════════════════════════
# 2. GESTION DES UTILISATEURS (ADMIN)
# ═══════════════════════════════════════════════════════════════

# 2.1 LISTER TOUS LES UTILISATEURS
echo "▶️  GET /api/users"
curl -X GET "http://localhost:8000/api/users" \
  -H "Authorization: Bearer $ADMIN_TOKEN"

# Réponse attendue:
# [
#   {
#     "id": 1,
#     "username": "admin",
#     "email": "admin@example.com",
#     "is_admin": true,
#     ...
#   },
#   {
#     "id": 2,
#     "username": "johndoe",
#     ...
#   }
# ]


# 2.2 RÉCUPÉRER UN UTILISATEUR SPÉCIFIQUE
echo "▶️  GET /api/users/1"
curl -X GET "http://localhost:8000/api/users/1" \
  -H "Authorization: Bearer $ADMIN_TOKEN"

# Réponse attendue: Les détails de l'utilisateur


# 2.3 MODIFIER LES RÔLES D'UN UTILISATEUR
echo "▶️  PUT /api/users/2/roles"
curl -X PUT "http://localhost:8000/api/users/2/roles" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -d '{
    "is_admin": false,
    "is_employer": true,
    "is_client": false
  }'

# Réponse attendue:
# {
#   "id": 2,
#   "username": "johndoe",
#   ...
#   "is_admin": false,
#   "is_employer": true,
#   "is_client": false,
#   ...
# }


# 2.4 DÉSACTIVER UN UTILISATEUR
echo "▶️  DELETE /api/users/3"
curl -X DELETE "http://localhost:8000/api/users/3" \
  -H "Authorization: Bearer $ADMIN_TOKEN"

# Réponse attendue:
# {
#   "message": "Utilisateur désactivé"
# }


# ═══════════════════════════════════════════════════════════════
# EXEMPLES EN JAVASCRIPT (depuis le frontend)
# ═══════════════════════════════════════════════════════════════

/*
// 1. INSCRIPTION
async function register() {
  const response = await fetch('http://localhost:8000/api/auth/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'johndoe',
      email: 'john@example.com',
      password: 'securepassword123',
      first_name: 'John',
      last_name: 'Doe',
      is_client: true,
      is_employer: false
    })
  });
  const data = await response.json();
  console.log(data);
}

// 2. CONNEXION
async function login() {
  const response = await fetch('http://localhost:8000/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'johndoe',
      password: 'securepassword123'
    })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
  localStorage.setItem('user', JSON.stringify(data.user));
  console.log('Connecté!', data.user);
}

// 3. RÉCUPÉRER TOUS LES UTILISATEURS
async function getAllUsers() {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/api/users', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  const users = await response.json();
  console.log(users);
}

// 4. MODIFIER LES RÔLES D'UN UTILISATEUR
async function updateUserRoles(userId, roles) {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`http://localhost:8000/api/users/${userId}/roles`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(roles)
  });
  const data = await response.json();
  console.log('Utilisateur mis à jour:', data);
}

// 5. DÉSACTIVER UN UTILISATEUR
async function deactivateUser(userId) {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`http://localhost:8000/api/users/${userId}`, {
    method: 'DELETE',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  const data = await response.json();
  console.log('Utilisateur désactivé:', data);
}

// 6. OBTENIR MES INFOS
async function getMyInfo() {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/api/auth/me', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  const user = await response.json();
  console.log('Mes infos:', user);
}
*/


# ═══════════════════════════════════════════════════════════════
# POSTMAN - IMPORTER CES EXEMPLES
# ═══════════════════════════════════════════════════════════════

"""
{
  "info": {
    "name": "User Management API",
    "description": "Collection de tests pour l'API",
    "version": "1.0"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Register",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/auth/register",
            "body": {
              "mode": "raw",
              "raw": "{...}"
            }
          }
        },
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/auth/login",
            "body": {
              "mode": "raw",
              "raw": "{...}"
            }
          }
        }
      ]
    },
    {
      "name": "Users",
      "item": [
        {
          "name": "Get All Users",
          "request": {
            "method": "GET",
            "url": "http://localhost:8000/api/users",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer {{access_token}}"
              }
            ]
          }
        }
      ]
    }
  ]
}
"""


# ═══════════════════════════════════════════════════════════════
# CODES D'ERREUR COURANTS
# ═══════════════════════════════════════════════════════════════

200 OK                    La requête a réussi
201 Created               Ressource créée avec succès
400 Bad Request           Les données envoyées sont invalides
401 Unauthorized          Token manquant ou invalide
403 Forbidden             Accès refusé (permissions insuffisantes)
404 Not Found             Ressource non trouvée
500 Internal Server Error Erreur serveur


# ═══════════════════════════════════════════════════════════════
# ASTUCES POUR TESTER
# ═══════════════════════════════════════════════════════════════

# Installer jq pour parser le JSON (optionnel)
sudo apt-get install jq

# Extraire le token automatiquement
TOKEN=$(curl -s -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' | jq -r '.access_token')

# Utiliser le token dans d'autres requêtes
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/users

# Tester avec Postman
# 1. Importer la collection JSON
# 2. Créer une variable d'environnement {{access_token}}
# 3. Exécuter les requêtes

# Tester avec VS Code REST Client
# Installer l'extension "REST Client"
# Créer un fichier requests.http avec les requêtes
# Cliquer sur "Send Request"
