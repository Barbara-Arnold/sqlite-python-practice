# Mini proyecto – Gestión de datos relacionales con SQLite y Python

Proyecto de práctica para trabajar con bases de datos relacionales usando SQLite y Python. Orientado a consolidar fundamentos de bases de datos relacionales y su integración con Python.
Incluye creación de esquema, carga de datos fake y consultas con JOIN.

## Tecnologías usadas

- Python 3
- SQLite
- Faker (datos de prueba)

## Estructura del proyecto
```
sqlite3_project/
├── db/
│ ├── schema.sql     # Esquema de la base de datos (DDL)
│ └── database.db    # Archivo de la base de datos (generado al ejecutar)
├── src/
│ ├── **init**.py    # Archivo necesario para tratar la carpeta como paquete
│ ├── db.py          # Gestión de conexión y creación de la BBDD
│ ├── seed.py        # Funciones para inserción de datos masivos
│ ├── queries.py     # Consultas SQL, JOINs y agregaciones
│ └── main.py        # Punto de entrada que coordina todo el flujo
├── core_reconciliation/
│   ├── database.py  # Gestión de conexión, tablas financieras y logs de auditoría  
│   └── seed_data.py # Inyección de escenarios y facturas de prueba
├── .gitignore       # Archivos excluidos del repositorio
├── README.md        # Documentación y guía del proyecto
└── CONTRIBUTING.md  # Guía para contribuir en el proyecto
```

## Modelo de datos

### users
- id (PK)
- name

### accounts
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

- Diseño básico de un flujo de inicialización de base de datos
- Uso de SQLite desde Python
- Creación y gestión de tablas
- Inserción de datos con executemany
- Uso correcto de commit y cursor
- Consultas JOIN entre tablas relacionadas
- Código organizado por responsabilidades

# 🚀 Fintech Suite: Engine Modular B2B

Proyecto avanzado de desarrollo backend enfocado en soluciones financieras corporativas para medianas empresas, diseñado para cubrir requerimientos de consistencia de datos, auditoría interna y gestión de riesgos financieros.

**Duración estimada:** 3 meses (Junio - Agosto 2026)  
**Stack Tecnológico:** Python 3, SQL / SQLite (Aislamiento mediante Patrón Repositorio)

---

## 📅 Roadmap del Proyecto

### 🔹 Módulo 1: Motor de Conciliación Bancaria (Reconciliation Engine)
* **Estado:** 🟢 En desarrollo  
* **Fecha de inicio:** 12 de Junio de 2026  
* **Fecha estimada de entrega:** 30 de Junio de 2026  

**Alcance del hito actual:**
* [x] Diseño del modelo de datos e integridad financiera (Completado: 12/06)
* [ ] Parser automatizado de extractos bancarios (CSV)
* [ ] Motor de emparejamiento por reglas jerárquicas
* [ ] Tabla e implementación de logs de auditoría (Compliance)

--------------------

* **Estructura e Integridad:** Modelado de datos financieros con restricciones estrictas de claves foráneas (`PRAGMA foreign_keys = ON`) y tipos fijos para importes monetarios (`DECIMAL`).
* **Ingesta de Datos:** Parser automatizado de extractos bancarios en formato de texto plano (`CSV`).
* **Matching Engine:** Motor jerárquico de emparejamiento de transacciones:
  * *Nivel 1:* Coincidencia exacta (Importe + Referencia única).
  * *Nivel 2:* Lógica difusa de tolerancia por desfase de céntimos (Umbral técnico).
  * *Nivel 3:* Agregación y resolución de cobros agrupados (Multi-invoice matching).
* **Compliance:** Registro inmutable de auditoría (`audit_logs`) para el rastreo y justificación de cada conciliación automatizada.

### 🔹 Módulo 2: Previsión de Tesorería y Flujos de Caja ── *Próximamente (Julio)*
* Proyección diaria de saldos a 30/60/90 días basada en vencimientos de facturas.
* Sistema de alertas preventivas de descubierto bancario.

### 🔹 Módulo 3: Motor de Riesgos y Factoring B2B ── *Próximamente (Agosto)*
* Evaluación automatizada del riesgo de crédito de facturas pendientes y cálculo dinámico de tasas de interés/comisiones de descuento.

---

## 🏛️ Decisiones de Arquitectura ("El porqué")

* **¿Por qué SQLite con Patrón Repositorio?** Se utiliza SQLite para agilizar el desarrollo del prototipo en entorno local. Sin embargo, toda la interacción con la base de datos se abstrae tras una capa de persistencia (clases Repositorio). Esto garantiza que el sistema pueda migrar a una base de datos relacional corporativa (como PostgreSQL) modificando únicamente la cadena de conexión, sin alterar una sola línea de la lógica de negocio.
* **¿Por qué el control de céntimos e importes estrictos?** En desarrollo Fintech, el uso de tipos de datos flotantes (`float`) está descartado debido a los errores de redondeo binario. Toda la lógica maneja precisión decimal exacta expresada en la divisa correspondiente (`EUR`), protegiendo la integridad de los balances.
