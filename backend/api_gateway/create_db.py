#!/usr/bin/env python3
"""
Crée la base de données Postgres définie dans `.env` si elle n'existe pas.
Usage: python create_db.py
"""
import os
from dotenv import load_dotenv, dotenv_values
import psycopg2
from psycopg2 import sql

here = os.path.dirname(__file__)
dotenv_path = os.path.join(here, ".env")
load_dotenv(dotenv_path)
config = dotenv_values(dotenv_path)

DB_HOST = config.get("DB_HOST")
DB_PORT = config.get("DB_PORT") or 5432
DB_USER = config.get("DB_USER")
DB_PASSWORD = config.get("DB_PASSWORD")
DB_NAME = config.get("DB_NAME")

def create_database_if_not_exists():
    conn = None
    try:
        # Connect to the default 'postgres' database to manage creation
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname='postgres'
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [DB_NAME])
        exists = cur.fetchone()
        if exists:
            print(f"✅ La base de données '{DB_NAME}' existe déjà.")
        else:
            cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(DB_NAME)))
            print(f"✅ Base de données '{DB_NAME}' créée avec succès.")

        cur.close()
    except Exception as e:
        print(f"❌ Impossible de créer/ vérifier la base: {e}")
        raise
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database_if_not_exists()
