import unittest
from unittest.mock import patch
from core.recipe import add_recipe, get_recipe, update_recipe, delete_recipe, get_all_recipes

# tests/test_recipe.py

class TestRecipe(unittest.TestCase):

    @patch('core.recipe.create_record')
    def test_add_recipe(self, mock_create_record):
        add_recipe("Pasta", "Boil water, add pasta", 4, "Main Course")
        mock_create_record.assert_called_once_with("recipes", {
            "name": "Pasta",
            "instructions": "Boil water, add pasta",
            "servings": 4,
            "category": "Main Course"
        })

    @patch('core.recipe.get_record_by_id')
    def test_get_recipe(self, mock_get_record_by_id):
        mock_get_record_by_id.return_value = ("Pasta", "Boil water, add pasta", 4, "Main Course")
        recipe = get_recipe(1)
        mock_get_record_by_id.assert_called_once_with("recipes", 1)
        self.assertEqual(recipe, ("Pasta", "Boil water, add pasta", 4, "Main Course"))

    @patch('core.recipe.update_record')
    def test_update_recipe(self, mock_update_record):
        update_recipe(1, "Pasta", "Boil water, add pasta", 4, "Main Course")
        mock_update_record.assert_called_once_with("recipes", 1, {
            "name": "Pasta",
            "instructions": "Boil water, add pasta",
            "servings": 4,
            "category": "Main Course"
        })

    @patch('core.recipe.delete_record')
    def test_delete_recipe(self, mock_delete_record):
        delete_recipe(1)
        mock_delete_record.assert_called_once_with("recipes", 1)

    @patch('core.recipe.get_all_records')
    def test_get_all_recipes(self, mock_get_all_records):
        mock_get_all_records.return_value = [
            ("Pasta", "Boil water, add pasta", 4, "Main Course"),
            ("Salad", "Chop veggies, add dressing", 2, "Appetizer")
        ]
        recipes = get_all_recipes()
        mock_get_all_records.assert_called_once_with("recipes")
        self.assertEqual(recipes, [
            ("Pasta", "Boil water, add pasta", 4, "Main Course"),
            ("Salad", "Chop veggies, add dressing", 2, "Appetizer")
        ])

if __name__ == '__main__':
    unittest.main()