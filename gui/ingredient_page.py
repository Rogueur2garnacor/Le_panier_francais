# gui/ingredient_page.py
from PyQt6.QtWidgets import QMainWindow, QLabel

class IngredientPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingrédients")

        label = QLabel("Bienvenue sur la page Ingrédients !", self)
        label.move(50, 50)

def create_ingredient_page():
    """Crée et retourne une instance de IngredientPage."""
    ingredient_page = IngredientPage()
    return ingredient_page
