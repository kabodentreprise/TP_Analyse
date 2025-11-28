-- Connectez-vous à la DB tp_projet, puis exécutez :

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone VARCHAR(20),
  is_admin BOOLEAN DEFAULT FALSE,
  is_employer BOOLEAN DEFAULT FALSE,
  is_client BOOLEAN DEFAULT FALSE,
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL
);

-- Optionnel : index sur username/email déjà créés par UNIQUE,
-- mais si vous voulez un index sur is_active :
CREATE INDEX IF NOT EXISTS idx_users_is_active ON users(is_active);