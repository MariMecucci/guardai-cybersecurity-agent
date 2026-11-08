"""Automated tests for the isolated GuardAI SQLite demonstration."""
import unittest
from agent.app import create_database, vulnerable_login, secure_login


class GuardAISecurityTests(unittest.TestCase):
    def setUp(self):
        self.connection = create_database()

    def tearDown(self):
        self.connection.close()

    def test_valid_login(self):
        self.assertTrue(secure_login(self.connection, "ana_lab", "exemplo123"))

    def test_invalid_login(self):
        self.assertFalse(secure_login(self.connection, "ana_lab", "senha_incorreta"))

    def test_sql_injection_mitigation(self):
        payload = "' OR '1'='1' -- "
        vulnerable_result = vulnerable_login(self.connection, payload, "senha_incorreta")
        secure_result = secure_login(self.connection, payload, "senha_incorreta")
        self.assertTrue(vulnerable_result)
        self.assertFalse(secure_result)


if __name__ == "__main__":
    unittest.main()
