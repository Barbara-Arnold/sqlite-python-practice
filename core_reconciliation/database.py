import sqlite3
import os

# Ruta donde se guardará la base de datos compartida (dentro de una carpeta 'data' en la raíz)
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'finance.db')

def get_connection():
    """Establece conexión con la base de datos y activa las Foreign Keys."""
    conn = sqlite3.connect(DB_PATH)
    # CRUCIAL PARA ENTORNOS FINANCIEROS: Forzar a SQLite a respetar las claves foráneas
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_tables():
    """Crea la estructura inicial de tablas para el módulo de conciliación."""
    # Asegurar que la carpeta 'data' en la raíz existe antes de crear la DB
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Tabla de Empresas / Clientes (A quienes emitimos facturas)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tax_id TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    # 2. Tabla de Facturas Emitidas (Pendientes de cobro)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_number TEXT UNIQUE NOT NULL,
        company_id INTEGER NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        issue_date DATE NOT NULL,
        due_date DATE NOT NULL,
        status TEXT DEFAULT 'PENDING',
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );
    """)
    
    # 3. Tabla de Transacciones Bancarias (Extracto que vendrá del CSV del banco)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bank_transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_date DATE NOT NULL,
        description TEXT NOT NULL,
        reference_text TEXT,
        amount DECIMAL(10, 2) NOT NULL,
        status TEXT DEFAULT 'UNRECONCILED',
        reconciled_with_invoice_id INTEGER,
        FOREIGN KEY (reconciled_with_invoice_id) REFERENCES invoices(id)
    );
    """)
    
    # 4. Tabla de Auditoría (Compliance / Control de modificaciones)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action_type TEXT NOT NULL,
        description TEXT NOT NULL,
        executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    conn.commit()
    conn.close()
    print("¡Base de datos y tablas financieras creadas con éxito!")

if __name__ == "__main__":
    create_tables()