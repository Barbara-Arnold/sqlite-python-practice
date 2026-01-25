from db import create_connection
from seed import insert_users, insert_accounts
from queries import show_users_with_accounts
from queries import show_users_summary


def main():
    # Creates connection to database, and database if it doesn't exist
    connector = create_connection()

    cursor = connector.cursor()

    # Executes the schema.sql file to create SQL tables
    with open("db/schema.sql", "r") as schema_file:
        schema_script = schema_file.read()
        cursor.executescript(schema_script)

    # Saves changes into database
    connector.commit()

    # Inserts data into the tables
    insert_users(connector)
    insert_accounts(connector)

    # Shows the SQL queries
    show_users_with_accounts(connector)
    show_users_summary(connector)

    connector.close()


# Python main guard
if __name__ == "__main__":
    main()
