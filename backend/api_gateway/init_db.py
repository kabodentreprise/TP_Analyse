#!/usr/bin/env python3
"""
Script d'initialisation de la base de données
Crée les tables et ajoute un utilisateur admin par défaut
"""
import os
import sys
from dotenv import load_dotenv

# Charger les variables d'environnement
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

from database import engine, Base
from models import User
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def init_db():
    """Initialiser la base de données"""
    print("🔧 Création des tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables créées avec succès!")

def add_default_admin():
    """Ajouter un utilisateur admin par défaut"""
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    # Vérifier si un admin existe
    admin = db.query(User).filter(User.is_admin == True).first()
    
    if admin:
        print("⚠️  Un administrateur existe déjà dans la base de données")
        db.close()
        return
    
    # Créer l'admin par défaut
    admin_user = User(
        username="admin",
        email="admin@example.com",
        password_hash=pwd_context.hash("admin123"),
        first_name="Admin",
        last_name="Système",
        is_admin=True,
        is_active=True
    )
    
    db.add(admin_user)
    db.commit()
    
    print("✅ Utilisateur admin créé avec succès!")
    print("   - Username: admin")
    print("   - Password: admin123")
    print("   ⚠️  IMPORTANT: Changez ce mot de passe après la première connexion!")
    
    db.close()

if __name__ == "__main__":
    try:
        print("🚀 Initialisation de la base de données...")
        init_db()
        add_default_admin()
        print("\n✨ Initialisation terminée avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de l'initialisation: {e}")
        sys.exit(1)
