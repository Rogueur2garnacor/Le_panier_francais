import unittest
from unittest.mock import patch
from core.inventory import add_item, get_item, update_item, delete_item, get_all_items

class TestInventory(unittest.TestCase):

    @patch('core.inventory.create_record')
    def test_add_item(self, mock_create_record):
        add_item("Apple", 10.0, "kg", 2.0, 20.0, "2023-12-31")
        mock_create_record.assert_called_once_with("items", {
            "name": "Apple",
            "quantity": 10.0,
            "unit": "kg",
            "low_threshold": 2.0,
            "high_threshold": 20.0,
            "expiration_date": "2023-12-31"
        })

    @patch('core.inventory.get_record_by_id')
    def test_get_item(self, mock_get_record_by_id):
        mock_get_record_by_id.return_value = ("Apple", 10.0, "kg", 2.0, 20.0, "2023-12-31")
        item = get_item(1)
        mock_get_record_by_id.assert_called_once_with("items", 1)
        self.assertEqual(item, ("Apple", 10.0, "kg", 2.0, 20.0, "2023-12-31"))

    @patch('core.inventory.update_record')
    def test_update_item(self, mock_update_record):
        update_item(1, "Apple", 15.0, "kg", 2.0, 20.0, "2023-12-31")
        mock_update_record.assert_called_once_with("items", 1, {
            "name": "Apple",
            "quantity": 15.0,
            "unit": "kg",
            "low_threshold": 2.0,
            "high_threshold": 20.0,
            "expiration_date": "2023-12-31"
        })

    @patch('core.inventory.delete_record')
    def test_delete_item(self, mock_delete_record):
        delete_item(1)
        mock_delete_record.assert_called_once_with("items", 1)

    @patch('core.inventory.get_all_records')
    def test_get_all_items(self, mock_get_all_records):
        mock_get_all_records.return_value = [
            ("Apple", 10.0, "kg", 2.0, 20.0, "2023-12-31"),
            ("Banana", 5.0, "kg", 1.0, 10.0, "2023-11-30")
        ]
        items = get_all_items()
        mock_get_all_records.assert_called_once_with("items")
        self.assertEqual(items, [
            ("Apple", 10.0, "kg", 2.0, 20.0, "2023-12-31"),
            ("Banana", 5.0, "kg", 1.0, 10.0, "2023-11-30")
        ])

    @patch('core.inventory.create_record')
    def test_add_item_with_invalid_data(self, mock_create_record):
        with self.assertRaises(TypeError):
            add_item("Apple", "ten", "kg", 2.0, 20.0, "2023-12-31")
        mock_create_record.assert_not_called()

    @patch('core.inventory.get_record_by_id')
    def test_get_nonexistent_item(self, mock_get_record_by_id):
        mock_get_record_by_id.return_value = None
        item = get_item(999)
        mock_get_record_by_id.assert_called_once_with("items", 999)
        self.assertIsNone(item)

    @patch('core.inventory.update_record')
    def test_update_nonexistent_item(self, mock_update_record):
        mock_update_record.side_effect = KeyError("Item not found")
        with self.assertRaises(KeyError):
            update_item(999, "Apple", 15.0, "kg", 2.0, 20.0, "2023-12-31")
        mock_update_record.assert_called_once_with("items", 999, {
            "name": "Apple",
            "quantity": 15.0,
            "unit": "kg",
            "low_threshold": 2.0,
            "high_threshold": 20.0,
            "expiration_date": "2023-12-31"
        })

    @patch('core.inventory.delete_record')
    def test_delete_nonexistent_item(self, mock_delete_record):
        mock_delete_record.side_effect = KeyError("Item not found")
        with self.assertRaises(KeyError):
            delete_item(999)
        mock_delete_record.assert_called_once_with("items", 999)

if __name__ == '__main__':
    unittest.main()