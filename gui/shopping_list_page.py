# gui/shopping_list_page.py
from PyQt6.QtWidgets import QMainWindow, QLabel

class ShoppingListPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventaire")
        
        label = QLabel("Bienvenue sur la page Inventaire !", self)
        label.move(50, 50)

def create_shopping_list_page():
    """Crée et retourne une instance de ShoppingListPage."""
    shopping_list_page = ShoppingListPage()
    return shopping_list_page
