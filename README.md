# Mini proyecto - SQLite y Python

Proyecto de práctica para trabajar con bases de datos relacionales usando SQLite y Python.
Incluye creación de esquema, carga de datos fake y consultas con JOIN.

## Tecnologías usadas

- Python 3 
- SQLite
- Faker (datos de prueba)

## Estructura del proyecto

sqlite3_project/
├── db/
│   ├── schema.sql    # Esquema de la base de datos (DDL)
│   └── database.db   # Archivo de la base de datos (generado al ejecutar)
├── src/
│   ├── __init__.py   # Archivo necesario para tratar la carpeta como paquete
│   ├── db.py         # Gestión de conexión y creación de la BBDD
│   ├── seed.py       # Funciones para inserción de datos masivos
│   ├── queries.py    # Consultas SQL, JOINs y agregaciones
│   └── main.py       # Punto de entrada que coordina todo el flujo
├── .gitignore        # Archivos excluidos del repositorio
└── README.md         # Documentación y guía del proyecto

## Modelo de datos

- users
    - id (PK)
    - name

- accounts
    - id (PK)
    - user_id (FK → users.id)
    - balance

## Cómo ejecutar el proyecto

Este proyecto está diseñado para ser "plug & play". No necesitas configurar la base de datos manualmente..

1 - Clona el repositorio:
git clone https://github.com/Barbara-Arnold/sqlite-python-practice.git

2 - Entra en la carpeta: cd sqlite3_project

3 - Lanza el programa con el comando de abajo o ejecuta en tu editor el archivo main.py:
python src/main.py 

Nota: El script detectará si la base de datos existe; si no, creará la carpeta db/, generará el archivo database.db, insertará los datos de prueba y mostrará los resultados..

## Qué se demuestra

- Uso de SQLite desde Python
- Creación y gestión de tablas
- Inserción de datos con executemany
- Uso correcto de commit y cursor
- Consultas JOIN entre tablas relacionadas
- Código organizado por responsabilidades