# Mini proyecto - SQLite y Python

Proyecto de práctica para trabajar con bases de datos relacionales usando SQLite y Python.
Incluye creación de esquema, carga de datos fake y consultas con JOIN.

## Tecnologías usadas

- Python 3 
- SQLite
- Faker (datos de prueba)

## Estructura del proyecto

sqlite3_project/
├─ db/
│  ├─ schema.sql    # Esquema de la base de datos sql
│  └─ database.db   # Archivo con la base de datos
├─ src/
│  ├─ db.py         # Crea la conexión a la base de datos, y si no existe, la crea.
│  ├─ seed.py       # Define las funciones de insersión de datos.
│  └─ queries.py    # Define las funciones con las consultas a la base de datos.
├─ main.py          # Importa las funciones para crear la bbdd, insertar datos y hacer consultas.
└─ README.md

## Modelo de datos

- users
    - id (PK)
    - name

- accounts
    - id (PK)
    - user_id (FK → users.id)
    - balance

## Cómo ejecutar el proyecto

1. Crear la base de datos y las tablas:
    sqlite3 db/database.db < db/schema.sql

2. Insertar datos fake:
    python src/seed.py

3. Ejecutar consultas:
    python src/queries.py

## Qué se demuestra

- Uso de SQLite desde Python
- Creación y gestión de tablas
- Inserción de datos con executemany
- Uso correcto de commit y cursor
- Consultas JOIN entre tablas relacionadas
- Código organizado por responsabilidades