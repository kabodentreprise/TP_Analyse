import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .client_route import router as user_router
from .admin_routes import router as admin_router
from .employer_route import router as super_admin_router
from .auth_routes import router as auth_router
from .database import Base, engine

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Système de Gestion des Utilisateurs",
    description="API pour la gestion des utilisateurs avec rôles",
    version="1.0.0"
)

# Configuration CORS - Adaptée pour production et développement
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

allowed_origins = [
    FRONTEND_URL,
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

if DEBUG:
    allowed_origins.append("*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(user_router, prefix="/api", tags=["user"])
app.include_router(admin_router, prefix="/api", tags=["admin"])
app.include_router(super_admin_router, prefix="/api", tags=["super_admin"]) 

@app.get("/")
def root():
    return {"message": "Bienvenue sur le microservice Commandes et Paiements"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=True)
