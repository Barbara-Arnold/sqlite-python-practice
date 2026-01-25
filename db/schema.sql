-- Here we create tables and definde relations

-- PRAGMA configuration instructions, original from SQLite
PRAGMA foreign_keys = ON;

-- Temporal log
PRAGMA journal_mode = WAL;

-- Tells if db is corrupt, useful when debugging
PRAGMA integrity_check;

DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL
);

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER NOT NULL, 
    balance REAL NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users(id)
);