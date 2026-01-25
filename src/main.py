from db import create_connection
from seed import insert_users, insert_accounts
from queries import show_users_with_accounts
from queries import show_users_summary


def main():
    connector = create_connection()
    insert_users(connector)
    insert_accounts(connector)

    print("Usuarios con cuentas: ")
    show_users_with_accounts(connector)

    print("Balance total por ususario: ")
    show_users_summary(connector)

    connector.close()


# Python main guard
if __name__ == "__main__":
    main()
