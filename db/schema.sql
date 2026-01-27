-- =========================
-- Configuración SQLite
-- =========================

-- Activa el uso de claves foráneas (SQLite lo tiene desactivado por defecto)
PRAGMA foreign_keys = ON;

-- Mejora concurrencia y estabilidad (opcional, pero buena práctica)
PRAGMA journal_mode = WAL;

-- Se asegura de que la base de datos no esté corrupta, útil para depuración
PRAGMA integrity_check;

-- =========================
-- Tabla: users y accounts
-- =========================

-- Eliminamos las tablas si existen para evitar conflictos al rehacer el esquema
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS accounts;

-- Tabla que almacena los usuarios del sistema
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador único del usuario
    name TEXT NOT NULL  -- Nombre del usuario
);

-- Tabla que representa cuentas asociadas a usuarios
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador único de la cuenta
    user_id INTEGER NOT NULL,   -- Usuario propietario de la cuenta
    balance REAL NOT NULL,      -- Saldo de la cuenta
    -- Relación entre accounts y users
    FOREIGN KEY (user_id) REFERENCES users(id)
);