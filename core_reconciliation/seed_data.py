from database import get_connection

def insert_mock_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Insertar Empresas de ejemplo (Clientes a los que facturamos)
    companies = [
        ('A-12345678', 'AeroSpace S.L.'),
        ('B-87654321', 'TecnoGalicia S.A.'),
        ('W-99887766', 'Wonbu Logistics')
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO companies (tax_id, name) 
    VALUES (?, ?);
    """, companies)
    
    # 2. Insertar Facturas Emitidas (Pendientes de cobro)
    invoices = [
        ('INV-2026-001', 1, 1500.00, '2026-06-01', '2026-07-01'), # Match perfecto
        ('INV-2026-002', 2, 850.50, '2026-06-02', '2026-07-02'),  # Tolerancia de céntimos
        ('INV-2026-003', 3, 300.00, '2026-06-05', '2026-07-05'),  # Pago agrupado (Parte 1)
        ('INV-2026-004', 3, 700.00, '2026-06-05', '2026-07-05')   # Pago agrupado (Parte 2)
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO invoices (invoice_number, company_id, amount, issue_date, due_date)
    VALUES (?, ?, ?, ?, ?);
    """, invoices)
    
    conn.commit()
    conn.close()
    print("¡Datos de prueba (Clientes y Facturas) insertados correctamente!")

if __name__ == "__main__":
    insert_mock_data()