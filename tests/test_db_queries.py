import unittest
import sqlite3
from typing import Dict, Any
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records
from config import DB_PATH

class TestDBQueries(unittest.TestCase):
    """
    Unit tests for database query functions.
    This test suite includes the following tests:
    - `test_create_record`: Tests the creation of a new record in the database.
    - `test_get_record_by_id`: Tests retrieving a record by its ID.
    - `test_update_record`: Tests updating an existing record in the database.
    - `test_delete_record`: Tests deleting a record from the database.
    - `test_get_all_records`: Tests retrieving all records from the database.
    Each test uses a temporary SQLite database created in `setUpClass` and cleaned up in `tearDownClass`.
    The `setUp` method ensures the table is cleaned before each test.
    """

    @classmethod
    def setUpClass(cls):
        """Set up a temporary database for testing."""
        cls.conn = sqlite3.connect(DB_PATH)
        cls.cursor = cls.conn.cursor()
        cls.cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)")
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        """Tear down the temporary database."""
        cls.cursor.execute("DROP TABLE IF EXISTS test_table")
        cls.conn.commit()
        cls.conn.close()

    def setUp(self):
        """Clean up the table before each test."""
        self.cursor.execute("DELETE FROM test_table")
        self.conn.commit()

    def test_create_record(self):
        data = {"name": "test_name", "value": 123}
        create_record("test_table", data)
        self.cursor.execute("SELECT * FROM test_table WHERE name = ?", (data["name"],))
        record = self.cursor.fetchone()
        self.assertIsNotNone(record)
        self.assertEqual(record[1], data["name"])
        self.assertEqual(record[2], data["value"])

    def test_get_record_by_id(self):
        data = {"name": "test_name", "value": 123}
        create_record("test_table", data)
        self.cursor.execute("SELECT id FROM test_table WHERE name = ?", (data["name"],))
        record_id = self.cursor.fetchone()[0]
        record = get_record_by_id("test_table", record_id)
        self.assertIsNotNone(record)
        self.assertEqual(record[1], data["name"])
        self.assertEqual(record[2], data["value"])

    def test_update_record(self):
        data = {"name": "test_name", "value": 123}
        create_record("test_table", data)
        self.cursor.execute("SELECT id FROM test_table WHERE name = ?", (data["name"],))
        record_id = self.cursor.fetchone()[0]
        updated_data = {"name": "updated_name", "value": 456}
        update_record("test_table", record_id, updated_data)
        record = get_record_by_id("test_table", record_id)
        self.assertIsNotNone(record)
        self.assertEqual(record[1], updated_data["name"])
        self.assertEqual(record[2], updated_data["value"])

    def test_delete_record(self):
        data = {"name": "test_name", "value": 123}
        create_record("test_table", data)
        self.cursor.execute("SELECT id FROM test_table WHERE name = ?", (data["name"],))
        record_id = self.cursor.fetchone()[0]
        delete_record("test_table", record_id)
        record = get_record_by_id("test_table", record_id)
        self.assertIsNone(record)

    def test_get_all_records(self):
        data1 = {"name": "test_name1", "value": 123}
        data2 = {"name": "test_name2", "value": 456}
        create_record("test_table", data1)
        create_record("test_table", data2)
        records = get_all_records("test_table")
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0][1], data1["name"])
        self.assertEqual(records[1][1], data2["name"])

      
if __name__ == "__main__":
    unittest.main()