import unittest
from unittest.mock import patch, MagicMock

# core/test_shopping_list.py
from core.shopping_list import (
    add_shopping_list,
    get_shopping_list,
    update_shopping_list,
    delete_shopping_list,
    get_all_shopping_lists,
    add_item_to_shopping_list,
    get_shopping_list_items,
    delete_item_from_shopping_list
)

class TestShoppingList(unittest.TestCase):

    @patch('core.shopping_list.create_record')
    def test_add_shopping_list(self, mock_create_record):
        add_shopping_list("Groceries")
        mock_create_record.assert_called_once_with("shopping_lists", {"name": "Groceries"})

    @patch('core.shopping_list.get_record_by_id')
    def test_get_shopping_list(self, mock_get_record_by_id):
        mock_get_record_by_id.return_value = ("Groceries",)
        result = get_shopping_list(1)
        mock_get_record_by_id.assert_called_once_with("shopping_lists", 1)
        self.assertEqual(result, ("Groceries",))

    @patch('core.shopping_list.update_record')
    def test_update_shopping_list(self, mock_update_record):
        update_shopping_list(1, "Updated Groceries")
        mock_update_record.assert_called_once_with("shopping_lists", 1, {"name": "Updated Groceries"})

    @patch('core.shopping_list.delete_record')
    def test_delete_shopping_list(self, mock_delete_record):
        delete_shopping_list(1)
        mock_delete_record.assert_called_once_with("shopping_lists", 1)

    @patch('core.shopping_list.get_all_records')
    def test_get_all_shopping_lists(self, mock_get_all_records):
        mock_get_all_records.return_value = [("Groceries",), ("Electronics",)]
        result = get_all_shopping_lists()
        mock_get_all_records.assert_called_once_with("shopping_lists")
        self.assertEqual(result, [("Groceries",), ("Electronics",)])

    @patch('core.shopping_list.create_record')
    def test_add_item_to_shopping_list(self, mock_create_record):
        add_item_to_shopping_list(1, 2, 3.5)
        mock_create_record.assert_called_once_with("shopping_list_items", {
            "list_id": 1,
            "item_id": 2,
            "quantity_needed": 3.5
        })

    @patch('core.shopping_list.sqlite3.connect')
    def test_get_shopping_list_items(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [("item1", 2), ("item2", 3)]

        result = get_shopping_list_items(1)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM shopping_list_items WHERE list_id = ?", (1,))
        self.assertEqual(result, [("item1", 2), ("item2", 3)])

    @patch('core.shopping_list.sqlite3.connect')
    def test_delete_item_from_shopping_list(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        delete_item_from_shopping_list(1, 2)
        mock_cursor.execute.assert_called_once_with("DELETE FROM shopping_list_items WHERE list_id = ? AND item_id = ?", (1, 2))
        mock_conn.commit.assert_called_once()

    @patch('core.shopping_list.create_record')
    def test_add_shopping_list_empty_name(self, mock_create_record):
        with self.assertRaises(ValueError):
            add_shopping_list("")
        mock_create_record.assert_not_called()

    @patch('core.shopping_list.get_record_by_id')
    def test_get_shopping_list_not_found(self, mock_get_record_by_id):
        mock_get_record_by_id.return_value = None
        result = get_shopping_list(999)
        mock_get_record_by_id.assert_called_once_with("shopping_lists", 999)
        self.assertIsNone(result)

    @patch('core.shopping_list.update_record')
    def test_update_shopping_list_empty_name(self, mock_update_record):
        with self.assertRaises(ValueError):
            update_shopping_list(1, "")
        mock_update_record.assert_not_called()

    @patch('core.shopping_list.delete_record')
    def test_delete_shopping_list_not_found(self, mock_delete_record):
        mock_delete_record.side_effect = ValueError("Record not found")
        with self.assertRaises(ValueError):
            delete_shopping_list(999)
        mock_delete_record.assert_called_once_with("shopping_lists", 999)

if __name__ == '__main__':
    unittest.main()