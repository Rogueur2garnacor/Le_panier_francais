# gui/recipe_page.py
from PyQt6.QtWidgets import QMainWindow, QLabel

class RecipePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventaire")
        
        label = QLabel("Bienvenue sur la page Inventaire !", self)
        label.move(50, 50)

def create_recipe_page():
    """Crée et retourne une instance de RecipePage."""
    recipe_page = RecipePage()
    return recipe_page
