"""
Tests pour l'API d'authentification
Tests des routes d'authentification et gestion des utilisateurs
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app
from models import User
from schemas import UserRegister, UserLogin

# Configuration de test avec SQLite
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer les tables de test
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Tests d'authentification
class TestAuthentication:
    
    def test_register_success(self):
        """Test d'inscription réussie"""
        response = client.post(
            "/api/auth/register",
            json={
                "username": "testuser",
                "email": "test@example.com",
                "password": "password123",
                "first_name": "Test",
                "last_name": "User",
                "is_client": True,
                "is_employer": False
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
        assert data["is_client"] == True
    
    def test_register_duplicate_username(self):
        """Test inscription avec username déjà existant"""
        # Première inscription
        client.post(
            "/api/auth/register",
            json={
                "username": "duplicateuser",
                "email": "first@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        
        # Deuxième inscription avec même username
        response = client.post(
            "/api/auth/register",
            json={
                "username": "duplicateuser",
                "email": "second@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        assert response.status_code == 400
        assert "existe déjà" in response.json()["detail"]
    
    def test_register_duplicate_email(self):
        """Test inscription avec email déjà existant"""
        # Première inscription
        client.post(
            "/api/auth/register",
            json={
                "username": "user1",
                "email": "duplicate@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        
        # Deuxième inscription avec même email
        response = client.post(
            "/api/auth/register",
            json={
                "username": "user2",
                "email": "duplicate@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        assert response.status_code == 400
        assert "email est déjà utilisé" in response.json()["detail"]
    
    def test_login_success(self):
        """Test connexion réussie"""
        # D'abord, s'inscrire
        client.post(
            "/api/auth/register",
            json={
                "username": "loginuser",
                "email": "login@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        
        # Puis se connecter
        response = client.post(
            "/api/auth/login",
            json={
                "username": "loginuser",
                "password": "password123"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["username"] == "loginuser"
    
    def test_login_invalid_credentials(self):
        """Test connexion avec identifiants invalides"""
        # S'inscrire
        client.post(
            "/api/auth/register",
            json={
                "username": "validuser",
                "email": "valid@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        
        # Essayer de se connecter avec mauvais mot de passe
        response = client.post(
            "/api/auth/login",
            json={
                "username": "validuser",
                "password": "wrongpassword"
            }
        )
        assert response.status_code == 401
        assert "invalides" in response.json()["detail"]
    
    def test_login_nonexistent_user(self):
        """Test connexion avec utilisateur inexistant"""
        response = client.post(
            "/api/auth/login",
            json={
                "username": "nonexistent",
                "password": "password123"
            }
        )
        assert response.status_code == 401
        assert "invalides" in response.json()["detail"]


# Tests de gestion des utilisateurs
class TestUserManagement:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configuration avant chaque test"""
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
    
    def test_get_all_users_as_admin(self):
        """Test récupération de tous les utilisateurs en tant qu'admin"""
        # Créer un utilisateur admin
        admin_response = client.post(
            "/api/auth/register",
            json={
                "username": "admin",
                "email": "admin@example.com",
                "password": "admin123",
                "is_client": False,
                "is_employer": False
            }
        )
        
        # Transformer en admin (simulation - en réalité via la BD)
        # ...
        
        # Note: Ce test nécessite une vraie setup avec un vrai admin
        # C'est un exemple de ce qu'on pourrait faire
    
    def test_get_all_users_unauthorized(self):
        """Test que seul un admin peut voir tous les utilisateurs"""
        # S'inscrire en tant que client
        client.post(
            "/api/auth/register",
            json={
                "username": "regularuser",
                "email": "regular@example.com",
                "password": "password123",
                "is_client": True
            }
        )
        
        # Se connecter
        login_response = client.post(
            "/api/auth/login",
            json={
                "username": "regularuser",
                "password": "password123"
            }
        )
        token = login_response.json()["access_token"]
        
        # Essayer d'accéder à la liste des utilisateurs
        response = client.get(
            "/api/users",
            headers={"Authorization": f"Bearer {token}"}
        )
        # Devrait être 403 (Forbidden)
        assert response.status_code == 403


# Tests des rôles
class TestRoles:
    
    def test_create_user_with_client_role(self):
        """Test création d'utilisateur avec rôle client"""
        response = client.post(
            "/api/auth/register",
            json={
                "username": "client_user",
                "email": "client@example.com",
                "password": "password123",
                "is_client": True,
                "is_employer": False
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["is_client"] == True
        assert data["is_employer"] == False
        assert data["is_admin"] == False
    
    def test_create_user_with_employer_role(self):
        """Test création d'utilisateur avec rôle employé"""
        response = client.post(
            "/api/auth/register",
            json={
                "username": "employer_user",
                "email": "employer@example.com",
                "password": "password123",
                "is_client": False,
                "is_employer": True
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["is_client"] == False
        assert data["is_employer"] == True
        assert data["is_admin"] == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
