import unittest
from unittest.mock import patch, MagicMock

# tests/test_dashboard.py
from core.dashboard import (
    get_total_items,
    get_low_stock_items,
    get_most_used_items_in_recipes,
    get_total_recipes,
    get_most_popular_recipes,
    get_most_frequent_shopping_list_items,
    get_weekly_menu
)


class TestDashboard(unittest.TestCase):

    @patch('core.dashboard.sqlite3.connect')
    def test_get_total_items(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [10]

        result = get_total_items()
        self.assertEqual(result, 10)
        mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM items")

    @patch('core.dashboard.sqlite3.connect')
    def test_get_low_stock_items(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('item1', 2, 5), ('item2', 1, 3)]

        result = get_low_stock_items()
        self.assertEqual(result, [('item1', 2, 5), ('item2', 1, 3)])
        mock_cursor.execute.assert_called_once_with("SELECT name, quantity, low_threshold FROM items WHERE quantity < low_threshold")

    @patch('core.dashboard.sqlite3.connect')
    def test_get_most_used_items_in_recipes(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('item1', 20), ('item2', 15)]

        result = get_most_used_items_in_recipes()
        self.assertEqual(result, [('item1', 20), ('item2', 15)])
        mock_cursor.execute.assert_called_once()

    @patch('core.dashboard.sqlite3.connect')
    def test_get_total_recipes(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [5]

        result = get_total_recipes()
        self.assertEqual(result, 5)
        mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM recipes")

    @patch('core.dashboard.sqlite3.connect')
    def test_get_most_popular_recipes(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('recipe1', 30), ('recipe2', 25)]

        result = get_most_popular_recipes()
        self.assertEqual(result, [('recipe1', 30), ('recipe2', 25)])
        mock_cursor.execute.assert_called_once()

    @patch('core.dashboard.sqlite3.connect')
    def test_get_most_frequent_shopping_list_items(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('item1', 50), ('item2', 45)]

        result = get_most_frequent_shopping_list_items()
        self.assertEqual(result, [('item1', 50), ('item2', 45)])
        mock_cursor.execute.assert_called_once()

    @patch('core.dashboard.sqlite3.connect')
    def test_get_weekly_menu(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('2023-10-01', 'recipe1'), ('2023-10-02', 'recipe2')]

        result = get_weekly_menu()
        self.assertEqual(result, [('2023-10-01', 'recipe1'), ('2023-10-02', 'recipe2')])
        mock_cursor.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()