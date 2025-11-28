FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers
COPY backend/api_gateway/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/api_gateway/ .

# Créer l'utilisateur non-root
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Exposer le port
EXPOSE 8000

# Démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
