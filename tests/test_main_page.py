import unittest
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from gui.main_page import create_base_page, create_tile, create_title, clic_tile, create_start_page, create_main_page
from PyQt6.QtCore import QSize

class TestMainPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def test_create_base_page(self):
        title = "Test Page"
        width = 800
        height = 600
        background_image_path = "gui/background.jpg"
        page = create_base_page(title, width, height, background_image_path)
        
        self.assertIsInstance(page, QMainWindow)
        self.assertEqual(page.windowTitle(), title)
        self.assertEqual(page.size(), QSize(width, height))

    def test_create_tile(self):
        height = 100
        width = 200
        style = "background-color: red;"
        text = "Test Tile"
        tile = create_tile(height, width, style, text)
        
        self.assertIsInstance(tile, QPushButton)
        self.assertEqual(tile.text(), text)
        self.assertEqual(tile.size(), QSize(width, height))
        self.assertEqual(tile.styleSheet(), style)

    def test_create_title(self):
        text = "Test Title"
        style = "font-size: 24px;"
        height = 100
        width = 200
        title = create_title(text, style, height, width)
        
        self.assertIsInstance(title, QPushButton)
        self.assertEqual(title.text(), text)
        self.assertEqual(title.size(), QSize(width, height))
        self.assertEqual(title.styleSheet(), style)

    def test_clic_tile(self):
        page_to_close = create_base_page("Close Page", 800, 600, "gui/background.jpg")
        page_to_open = create_base_page("Open Page", 800, 600, "gui/background.jpg")
        tile = create_tile(100, 200, "background-color: red;", "Click Me")
        
        clic_tile(tile, page_to_close, page_to_open)
        
        # Simulate click
        tile.click()
        
        self.assertFalse(page_to_close.isVisible())
        self.assertTrue(page_to_open.isVisible())

    def test_create_start_page(self):
        start_page = create_start_page()
        
        self.assertIsInstance(start_page, QMainWindow)
        self.assertEqual(start_page.windowTitle(), "Le panier français")
        self.assertEqual(start_page.size(), QSize(1200, 750))

    def test_create_main_page(self):
        main_page = create_main_page()
        
        self.assertIsInstance(main_page, QMainWindow)
        self.assertEqual(main_page.windowTitle(), "Le panier français")
        self.assertEqual(main_page.size(), QSize(1200, 750))

if __name__ == "__main__":
    unittest.main()