"""GuardAI: isolated, educational SQL injection comparison using SQLite in memory.

Only fixed fictional data and a fixed training input are used.
DO NOT reuse vulnerable_login in real applications.
"""
import sqlite3


def create_database():
    connection = sqlite3.connect(":memory:")
    connection.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    connection.executemany(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        [
            ("ana_lab", "exemplo123"),
            ("leo_lab", "exemplo456"),
        ],
    )
    connection.commit()
    return connection


def vulnerable_login(connection, username, password):
    """Unsafe on purpose for a bounded, in-memory laboratory demonstration."""
    query = (
        f"SELECT id FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )
    result = connection.execute(query).fetchone()
    return result is not None


def secure_login(connection, username, password):
    """Parameterized query: untrusted strings remain data, not SQL syntax."""
    query = (
        "SELECT id FROM users "
        "WHERE username = ? AND password = ?"
    )
    result = connection.execute(query, (username, password)).fetchone()
    return result is not None


def main():
    connection = create_database()
    try:
        valid_user = "ana_lab"
        valid_password = "exemplo123"
        normal_login = secure_login(connection, valid_user, valid_password)

        # Fixed input, used only on fictional data in the in-memory database.
        test_input = "' OR '1'='1' -- "
        wrong_password = "incorrect_demo_password"

        vulnerable_result = vulnerable_login(connection, test_input, wrong_password)
        secure_result = secure_login(connection, test_input, wrong_password)

        print("=== GUARDAI SECURITY LAB ===")
        print(f"Normal login: {normal_login}")
        print(f"Vulnerable query accepted input: {vulnerable_result}")
        print(f"Secure query accepted input: {secure_result}")

        assert normal_login is True
        assert vulnerable_result is True
        assert secure_result is False

        print("Security comparison: PASSED")
        print("Parameterized query mitigation: VERIFIED")
        print("Environment: LOCAL AND ISOLATED")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
