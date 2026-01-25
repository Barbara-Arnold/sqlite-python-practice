import sqlite3

import os

# Current file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# We access the database location
DB_PATH = os.path.join(BASE_DIR, "..", "db", "database.db")

def create_connection(db_file=DB_PATH):
    """
    Creates and returns a connection to the SQLite database.
    If database doesn't exists, it's created.
    """

    #  Initializes a connection variable to None
    connection = None

    try:
        os.makedirs(os.path.dirname(db_file), exist_ok=True)
        connection = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except (sqlite3.Error, OSError) as error: # Capture SQL and operating system errors (folders)
        print("Error trying to connect to database: {error}")
    return connection

if __name__ == "__main__":
    create_connection()