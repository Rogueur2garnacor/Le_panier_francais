# gui/inventory_page.py
from PyQt6.QtWidgets import QMainWindow, QLabel

class InventoryPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventaire")
        
        label = QLabel("Bienvenue sur la page Inventaire !", self)
        label.move(50, 50)

def create_inventory_page():
    """Crée et retourne une instance de InventoryPage."""
    inventory_page = InventoryPage()
    return inventory_page
