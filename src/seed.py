from db import create_connection
from faker import Faker
from random import uniform

fake = Faker()

def get_id(connector, table):
    cursor = connector.cursor()

    cursor.execute(
        f"""SELECT id FROM {table}"""
    )

    ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return ids

def insert_users(connector, n=10):
    cursor = connector.cursor()
    
    users = [(fake.name(),) for _ in range(n)]

    cursor.executemany(
        """INSERT INTO users (name) VALUES (?)""", users
    )

    connector.commit()
    cursor.close()

    print(f"{n} users inserted successfully!")

def insert_accounts(connector, n=10):
    cursor = connector.cursor()

    account_ids = get_id(connector, "users")

    accounts = [(user_id, round(uniform(100, 10_000), 2)) for user_id in account_ids]

    cursor.executemany(
        """INSERT INTO accounts (user_id, balance) VALUES (?, ?)""", accounts
    )

    connector.commit()

    cursor.close()

    print(f"{n} accounts inserted successfully!")

if __name__ == "__main__":
    connector = create_connection()
    insert_users(connector)
    insert_accounts(connector)
    connector.close()

