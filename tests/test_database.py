import unittest
import os
from config import DB_PATH, TABLE_SCHEMAS
from data.database import create_tables, delete_database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Suppression de la base de données avant chaque test
        if os.path.exists(DB_PATH):
            delete_database(DB_PATH)

    def tearDown(self):
        # Suppression de la base de données après chaque test
        if os.path.exists(DB_PATH):
            delete_database(DB_PATH)

    def test_create_database(self):
        # Création de la base de données
        create_tables(DB_PATH, TABLE_SCHEMAS)
        # Vérification que la base de données a été créée
        self.assertTrue(os.path.exists(DB_PATH))

    def test_delete_database(self):
        # Création de la base de données
        create_tables(DB_PATH, TABLE_SCHEMAS)
        # Suppression de la base de données
        delete_database(DB_PATH)
        # Vérification que la base de données a été supprimée
        self.assertFalse(os.path.exists(DB_PATH))

if __name__ == '__main__':
    unittest.main()
