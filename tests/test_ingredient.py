import unittest
from unittest.mock import patch
from core.ingredient import add_ingredient, get_ingredient, update_ingredient, delete_ingredient, get_all_ingredients

# tests/test_ingredient.py

class TestIngredient(unittest.TestCase):

    @patch('core.ingredient.create_record')
    def test_add_ingredient(self, mock_create_record):
        add_ingredient("Tomato", "Vegetable")
        mock_create_record.assert_called_once_with("ingredients", {"name": "Tomato", "category": "Vegetable"})

    @patch('core.ingredient.get_record_by_id')
    def test_get_ingredient(self, mock_get_record_by_id):
        mock_get_record_by_id.return_value = ("Tomato", "Vegetable")
        result = get_ingredient(1)
        mock_get_record_by_id.assert_called_once_with("ingredients", 1)
        self.assertEqual(result, ("Tomato", "Vegetable"))

    @patch('core.ingredient.update_record')
    def test_update_ingredient(self, mock_update_record):
        update_ingredient(1, "Tomato", "Fruit")
        mock_update_record.assert_called_once_with("ingredients", 1, {"name": "Tomato", "category": "Fruit"})

    @patch('core.ingredient.delete_record')
    def test_delete_ingredient(self, mock_delete_record):
        delete_ingredient(1)
        mock_delete_record.assert_called_once_with("ingredients", 1)

    @patch('core.ingredient.get_all_records')
    def test_get_all_ingredients(self, mock_get_all_records):
        mock_get_all_records.return_value = [("Tomato", "Vegetable"), ("Apple", "Fruit")]
        result = get_all_ingredients()
        mock_get_all_records.assert_called_once_with("ingredients")
        self.assertEqual(result, [("Tomato", "Vegetable"), ("Apple", "Fruit")])

if __name__ == '__main__':
    unittest.main()