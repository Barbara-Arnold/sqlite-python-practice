from db import create_connection


def show_users(connector):
    cursor = connector.cursor()

    cursor.execute("""SELECT * FROM users""")

    print("Users: ")

    for row in cursor.fetchall():
        print(row)

    cursor.close()


def show_accounts(connector):
    cursor = connector.cursor()

    cursor.execute("""SELECT * FROM accounts""")

    print("Accounts: ")

    for row in cursor.fetchall():
        print(row)

    cursor.close()


def show_users_with_accounts(connector):
    cursor = connector.cursor()

    cursor.execute(
        """SELECT u.id, u.name, a.id, a.balance 
        FROM users u
        JOIN accounts a ON u.id = a.user_id
        ORDER BY u.id;
        """
    )

    print("Users with accounts (JOIN): ")

    for row in cursor.fetchall():
        print(
            f"User Id: {row[0]}, Name: {row[1]}, Account Id: {row[2]}, Balance: {row[3]}"
        )

    cursor.close()


def show_users_summary(connector):
    """
    JOIN + Agregations: summary per user.
    """

    cursor = connector.cursor()

    cursor.execute(
        """
        SELECT 
            u.id, 
            u.name, 
            COUNT(a.id) AS num_accounts, 
            ROUND(SUM(a.balance), 2) AS total_balance 
        FROM users u 
        LEFT JOIN accounts a ON u.id = a.user_id 
        GROUP BY u.id 
        ORDER BY total_balance DESC;
        """
    )

    print("Summary per user: ")
    for user_id, name, num_accounts, total_balance in cursor.fetchall():
        print(
            f"User {user_id} - ({name}): Account {num_accounts} - Total: {total_balance} €."
        )

    cursor.close()


def show_high_value_users(connector, min_balance=5_000):
    """
    Filtered query: users with higher balance.
    """

    cursor = connector.cursor()

    cursor.execute(
        """
        SELECT u.name, SUM(a.balance) AS total_balance
        FROM users u
        JOIN accounts a ON u.id = a.user_id 
        GROUP BY u.id
        HAVING total_balance >= ? 
        ORDER BY total_balance DESC;
        """,
        (min_balance,),
    )

    print(f"Users with more than {min_balance} €: ")
    for name, total_balance in cursor.fetchall():
        print(f"{name}: {round(total_balance, 2)} €")

    cursor.close()


if __name__ == "__main__":
    connector = create_connection()

    show_users(connector)
    show_accounts(connector)

    show_users_with_accounts(connector)

    show_users_summary(connector)
    show_high_value_users(connector)

    connector.close()
