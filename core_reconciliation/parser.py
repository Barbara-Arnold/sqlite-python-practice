import csv
import os
from database import get_connection

# Rutas dinámicas
BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, '..', 'data', 'bank_statement.csv')

def parse_and_import_bank_statement():
    """Lee el extracto bancario en CSV e inyecta las transacciones en la DB."""
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: No se encuentra el archivo CSV en la ruta: {CSV_PATH}")
        return

    conn = get_connection()
    cursor = conn.cursor()
    
    transactions_imported = 0

    print("⏳ Iniciando la ingesta del extracto bancario...")

    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # 🛡️ CONTROL DE ERRORES: Si la línea está vacía o falta la columna 'amount', nos la saltamos de forma segura
            if not row.get('amount') or not row.get('date'):
                continue
                
            # Extraer y limpiar campos
            date = row['date'].strip()
            description = row['description'].strip()
            reference = row['reference'].strip() if row['reference'] else None
            
            try:
                amount = float(row['amount'].strip())
            except ValueError:
                print(f"⚠️ Saltando línea malformada por importe inválido: {row}")
                continue

            # Insertar en la tabla bank_transactions evitando duplicados exactos
            cursor.execute("""
            INSERT INTO bank_transactions (transaction_date, description, reference_text, amount, status)
            SELECT ?, ?, ?, ?, 'UNRECONCILED'
            WHERE NOT EXISTS (
                SELECT 1 FROM bank_transactions 
                WHERE transaction_date = ? AND description = ? AND amount = ?
            );
            """, (date, description, reference, amount, date, description, amount))
            
            if cursor.rowcount > 0:
                transactions_imported += cursor.rowcount

    # Registrar la acción en la tabla de auditoría (Compliance corporativo)
    if transactions_imported > 0:
        cursor.execute("""
        INSERT INTO audit_logs (action_type, description)
        VALUES ('INGEST', ?);
        """, (f"Se han importado con éxito {transactions_imported} transacciones desde bank_statement.csv",))
        
        conn.commit()
        print(f"✅ Ingesta completada. {transactions_imported} nuevas transacciones cargadas en el sistema.")
    else:
        print("ℹ️ El extracto bancario ya estaba procesado. No se han añadido transacciones duplicadas.")

    conn.close()

if __name__ == "__main__":
    parse_and_import_bank_statement()