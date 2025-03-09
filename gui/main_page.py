# gui/main_page.py
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
)
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import QSize, Qt
from gui.inventory_page import create_inventory_page
from gui.recipe_page import create_recipe_page
from gui.shopping_list_page import create_shopping_list_page
from gui.dashboard_page import create_dashboard_page
from gui.ingredient_page import create_ingredient_page

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Le Panier Français - Page Principale")
        self.setFixedSize(QSize(1200, 750))

        # Charger l'image de fond
        background_image = QPixmap("gui/background.jpg")
        background_image = background_image.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        # Créer une palette pour le fond
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Créer un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Créer un layout en grille pour les tuiles
        grid_layout = QGridLayout(central_widget)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Définir la taille des tuiles
        tile_width = 300
        tile_height = 150

        # Ajouter des boutons (tuiles) pour chaque fonctionnalité
        inventory_button = QPushButton("Inventaire")
        inventory_button.setStyleSheet("font-size: 32px;font-family : Palatino;font-weight: bold")
        inventory_button.setFixedSize(QSize(tile_width, tile_height))
        inventory_button.clicked.connect(self.open_inventory_page)
        grid_layout.addWidget(inventory_button, 0, 0)

        recipe_button = QPushButton("Recettes")
        recipe_button.setStyleSheet("font-size: 32px;font-family : Palatino;font-weight: bold")
        recipe_button.setFixedSize(QSize(tile_width, tile_height))
        recipe_button.clicked.connect(self.open_recipe_page)
        grid_layout.addWidget(recipe_button, 0, 1)

        shopping_list_button = QPushButton("Listes de courses")
        shopping_list_button.setStyleSheet("font-size: 32px;font-family : Palatino;font-weight: bold ")
        shopping_list_button.setFixedSize(QSize(tile_width, tile_height))
        shopping_list_button.clicked.connect(self.open_shopping_list_page)
        grid_layout.addWidget(shopping_list_button, 1, 0)

        ingredient_button = QPushButton("Ingrédients")
        ingredient_button.setStyleSheet("font-size: 32px;font-family : Palatino;font-weight: bold")
        ingredient_button.setFixedSize(QSize(tile_width, tile_height))
        ingredient_button.clicked.connect(self.open_ingredient_page)
        grid_layout.addWidget(ingredient_button, 1, 1)

       
        dashboard_button = QPushButton("Tableau de bord") 
        dashboard_button.setStyleSheet("font-size: 32px;font-family : Palatino;font-weight: bold")       
        dashboard_button.setFixedSize(QSize(tile_width * 2 + 20 , tile_height))
        dashboard_button.clicked.connect(self.open_dashboard_page)
        grid_layout.addWidget(dashboard_button, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

    def open_inventory_page(self):
        """Ouvre la page Inventaire et ferme la page principale."""
        self.inventory_window = create_inventory_page()
        self.inventory_window.show()
        self.close()

    def open_recipe_page(self):
        """Ouvre la page Recettes et ferme la page principale."""
        self.recipe_window = create_recipe_page()
        self.recipe_window.show()
        self.close()

    def open_shopping_list_page(self):
        """Ouvre la page Listes de courses et ferme la page principale."""
        self.shopping_list_window = create_shopping_list_page()
        self.shopping_list_window.show()
        self.close()

    def open_dashboard_page(self):
        """Ouvre la page Tableau de bord et ferme la page principale."""
        self.dashboard_window = create_dashboard_page()
        self.dashboard_window.show()
        self.close()

    def open_ingredient_page(self):
        """Ouvre la page Ingrédients et ferme la page principale."""
        self.ingredient_window = create_ingredient_page()
        self.ingredient_window.show()
        self.close()


def create_main_page():
    """Crée et retourne une instance de MainPage."""
    main_page = MainPage()
    return main_page
