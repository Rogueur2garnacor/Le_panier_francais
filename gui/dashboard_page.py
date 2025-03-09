# gui/inventory_page.py
from PyQt6.QtWidgets import QMainWindow, QLabel

class DashboardPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventaire")
        
        label = QLabel("Bienvenue sur la page Inventaire !", self)
        label.move(50, 50)

def create_dashboard_page():
    """Crée et retourne une instance de DashboardPage."""
    dashboard_page = DashboardPage()
    return dashboard_page
