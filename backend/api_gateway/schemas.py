from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Schémas d'inscription et connexion
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_client: bool = False
    is_employer: bool = False

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

# Schémas pour afficher les utilisateurs
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    is_admin: bool
    is_employer: bool
    is_client: bool
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserRoleUpdate(BaseModel):
    is_admin: bool = False
    is_employer: bool = False
    is_client: bool = False

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
