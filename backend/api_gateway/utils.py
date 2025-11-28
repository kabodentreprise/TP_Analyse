from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Utilisateur, PasswordResetToken, PolitiqueUtilisation, AcceptationPolitique
from schemas import UtilisateurCreate, PasswordResetToken
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, List 
import secrets
from sqlalchemy import select


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def generate_unique_user_id(db: Session) -> str:
    """
    Génère un ID hexadécimal unique de 12 caractères pour la table User.
    Vérifie l'unicité dans la base de données.
    """
    while True:
        new_id = secrets.token_hex(6)
        result = db.execute(select(Utilisateur).filter(Utilisateur.id == new_id))
        existing_obj = result.scalars().first()
        if not existing_obj:
            return new_id

def generate_unique_password_reset_token_id(db: Session) -> str:
    """
    Génère un ID hexadécimal unique de 12 caractères pour la table RestaurantPasswordResetToken.
    Vérifie l'unicité dans la base de données.
    """
    while True:
        new_id = secrets.token_hex(6)
        result = db.execute(select(PasswordResetToken).filter(PasswordResetToken.id == new_id))
        existing_obj = result.scalars().first()
        if not existing_obj:
            return new_id

# ------------------ FONCTIONS CRUD DE BASE (UTILISATEUR) ------------------
def get_user_by_username(db: Session, username: str) -> Optional[Utilisateur]:
    """Recuprer un utilisateur par son username"""
    return db.query(Utilisateur).filter(Utilisateur.username == username).first()

def get_user_by_email(db: Session, email: str) -> Optional[Utilisateur]:
    """Récupère un utilisateur par son email."""
    return db.query(Utilisateur).filter(Utilisateur.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[Utilisateur]:
    """Récupère un utilisateur par son ID."""
    return db.query(Utilisateur).filter(Utilisateur.id == user_id).first()

def get_all_users(db: Session) -> List[Utilisateur]:
    """Récupère la liste de tous les utilisateurs."""
    return db.query(Utilisateur).all()

def authenticate_user(db: Session, identifier: str, password: str) -> Optional[Utilisateur]:
    """Vérifie les identifiants de connexion avec email OU username."""
    user = None
    
    # ✅ CORRECTION : Essayer d'abord avec l'email
    user = get_user_by_email(db, identifier)
    
    # ✅ Si pas trouvé, essayer avec le username
    if not user:
        user = get_user_by_username(db, identifier)
    
    # Vérifier si l'utilisateur existe, est actif et le mot de passe est correct
    if not user or not user.is_active or not pwd_context.verify(password, user.mot_de_passe):
        return None
    
    return user

def create_user(
    db: Session,
    user: UtilisateurCreate,
    is_admin: bool = False,
    is_super_admin: bool = False,
    is_livreur: bool = False,
    is_active: bool = True,
    is_user: bool = True
) -> Optional[Utilisateur]:
    """
    Crée un nouvel utilisateur avec un mot de passe haché et les rôles spécifiés.
    Le username est obligatoire et doit être unique.
    """
    # Vérification du username
    if not hasattr(user, "username") or not user.username:
        raise ValueError("Le champ 'username' est obligatoire.")
    if get_user_by_username(db, user.username):
        raise ValueError("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")

    hashed_password = pwd_context.hash(user.password)
    new_user_id = generate_unique_user_id(db)
    db_user = Utilisateur(
        id=new_user_id,
        username=user.username,
        email=user.email,
        mot_de_passe=hashed_password,
        is_active=is_active,
        is_admin=is_admin,
        is_super_admin=is_super_admin,
        is_livreur=is_livreur,
        is_user=is_user,
    prenoms=user.prenoms,
    nom=user.nom,
    telephone=user.telephone,
    delivery_address=user.delivery_address,
    # Les champs suivants sont retirés car absents du schéma UtilisateurCreate :
    # photo, statut, genre, badge, otp_code, biographie, date_sup, date_creation, date_modif
    date_creation=datetime.now(timezone.utc),
    date_modif=datetime.now(timezone.utc),
        is_utilisateur_verifie=None,
        email_verified_at=None,
        token_confirmation_email=None,
        date_exp_token_confirmation_email=None
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        # Crée une acceptation de politique de confidentialité pour le nouvel utilisateur
        create_acceptation_pending(db, db_user.id)
        return db_user
    except IntegrityError:
        db.rollback()
        return None

def update_user_details(db: Session, user_id: int, fields: Dict[str, Any]) -> Optional[Utilisateur]:
    """Met à jour dynamiquement les informations d’un utilisateur."""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    for key, value in fields.items():
        if key == "password":
            if value:
                setattr(db_user, "hashed_password", pwd_context.hash(value))
        # Empêche la modification de l'ID, de l'email et du hachage de mot de passe directement
        elif hasattr(db_user, key) and key not in ["id", "email", "hashed_password"]:
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_password(db: Session, user_id: int, new_password: str) -> Optional[Utilisateur]:
    """Change le mot de passe d’un utilisateur (fonction dédiée pour plus de clarté)."""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None
    db_user.hashed_password = pwd_context.hash(new_password)
    db.commit()
    db.refresh(db_user)
    return db_user

# ------------------ GESTION DE LA RÉINITIALISATION DE MOT DE PASSE ------------------

def create_password_reset_token(db: Session, user_id: int) -> str:
    """
    Crée un code unique de 5 chiffres pour réinitialisation, valable 15 minutes.
    Supprime les anciens codes existants pour l'utilisateur.
    """
    # ... (le code pour la réinitialisation de mot de passe est correct et conservé) ...
    db.query(PasswordResetToken).filter(
        PasswordResetToken.user_id == user_id
    ).delete()
    db.commit()

    code = str(secrets.randbelow(100000)).zfill(5)
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)

    db_token = PasswordResetToken(
        token=code,
        user_id=user_id,
        expires_at=expires_at
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)

    return code

def get_valid_password_reset_token(db: Session, email: str, code: str) -> Optional[PasswordResetToken]:
    """Vérifie si un code de réinitialisation est valide pour l'utilisateur donné."""
    user = get_user_by_email(db, email)
    if not user: return None

    db_token = db.query(PasswordResetToken).filter(
        PasswordResetToken.user_id == user.id,
        PasswordResetToken.token == code
    ).first()

    if db_token and db_token.expires_at > datetime.now(timezone.utc):
        return db_token
    return None

def delete_password_reset_token(db: Session, token_id: int) -> bool:
    """Supprime un code de réinitialisation (après usage ou expiration)."""
    db_token = db.query(PasswordResetToken).filter(PasswordResetToken.id == token_id).first()
    if db_token:
        db.delete(db_token)
        db.commit()
        return True
    return False


def get_all_livreurs(db: Session) -> List[Utilisateur]:
    """Retourne la liste de tous les livreurs."""
    return db.query(Utilisateur).filter(Utilisateur.is_livreur == True).all()

# --- Gestion des utilisateurs super admin ---

def get_all_users(db: Session) -> List[Utilisateur]:
    return db.query(Utilisateur).all()

def get_user_by_email(db: Session, email: str) -> Optional[Utilisateur]:
    return db.query(Utilisateur).filter(Utilisateur.email == email).first()

def get_user_by_id(db: Session, user_id: str) -> Optional[Utilisateur]:
    # Correction de la double query()
    return db.query(Utilisateur).filter(Utilisateur.id == user_id).first()

def update_user_active_status(db: Session, user_id: str, is_active: bool) -> Optional[Utilisateur]:
    db_user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if not db_user:
        return None
    db_user.is_active = is_active
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_admin_status(db: Session, user_id: str, is_admin: bool) -> Optional[Utilisateur]:
    db_user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if not db_user:
        return None
    db_user.is_admin = is_admin
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_super_admin_status(db: Session, user_id: str, is_super_admin: bool) -> Optional[Utilisateur]:
    db_user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if not db_user:
        return None
    db_user.is_super_admin = is_super_admin
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_livreur_status(db: Session, user_id: str, is_livreur: bool) -> Optional[Utilisateur]:
    db_user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if not db_user:
        return None
    db_user.is_livreur = is_livreur
    db.commit()
    db.refresh(db_user)
    return db_user

def get_active_politique(db: Session) -> Optional[PolitiqueUtilisation]:
    """
    Récupère la politique de confidentialité actuellement active.
    """
    stmt = select(PolitiqueUtilisation).where(
        PolitiqueUtilisation.est_active == True
    ).order_by(
        PolitiqueUtilisation.date_publication.desc()
    ).limit(1)
    return db.execute(stmt).scalars().first()


def create_acceptation_pending(db: Session, user_id: str):
    """
    Crée une entrée d'acceptation de politique pour un nouvel utilisateur, non acceptée par défaut.
    """
    active_politique = get_active_politique(db)
    if not active_politique:
        return None  # Pas de politique active

    acceptation_data = {
        "id_utilisateur": user_id,
        "id_politique": active_politique.id,
        "lu_et_accepte": False,
        "date_acceptation": None
    }
    db_acceptation = AcceptationPolitique(**acceptation_data)
    db.add(db_acceptation)
    db.commit()
    db.refresh(db_acceptation)
    return db_acceptation





