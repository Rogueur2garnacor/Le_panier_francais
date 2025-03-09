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
        inventory_button.setFixedSize(QSize(tile_width, tile_height))
        inventory_button.clicked.connect(self.open_inventory_page)
        grid_layout.addWidget(inventory_button, 0, 0)

        recipe_button = QPushButton("Recettes")
        recipe_button.setFixedSize(QSize(tile_width, tile_height))
        recipe_button.clicked.connect(self.open_recipe_page)
        grid_layout.addWidget(recipe_button, 0, 1)

        shopping_list_button = QPushButton("Listes de courses")
        shopping_list_button.setFixedSize(QSize(tile_width, tile_height))
        shopping_list_button.clicked.connect(self.open_shopping_list_page)
        grid_layout.addWidget(shopping_list_button, 1, 0)

        ingredient_button = QPushButton("Ingrédients")
        ingredient_button.setFixedSize(QSize(tile_width, tile_height))
        ingredient_button.clicked.connect(self.open_ingredient_page)
        grid_layout.addWidget(ingredient_button, 1, 1)

        dashboard_button = QPushButton("Tableau de bord")
        dashboard_button.setFixedSize(QSize(tile_width * 2 + 20 , tile_height))  # Double la largeur et ajuste la position
        dashboard_button.clicked.connect(self.open_dashboard_page)
        grid_layout.addWidget(dashboard_button, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)  # S'étend sur deux colonnes et est centré

        # Attributs pour conserver les fenêtres ouvertes
        self.inventory_window = None
        self.recipe_window = None
        self.shopping_list_window = None
        self.dashboard_window = None
        self.ingredient_window = None

    def open_inventory_page(self):
        """Ouvre la page Inventaire."""
        if not self.inventory_window:
            self.inventory_window = create_inventory_page()
            self.inventory_window.show()
            self.inventory_window.destroyed.connect(lambda: setattr(self, 'inventory_window', None))

    def open_recipe_page(self):
        """Ouvre la page Recettes."""
        if not self.recipe_window:
            self.recipe_window = create_recipe_page()
            self.recipe_window.show()
            self.recipe_window.destroyed.connect(lambda: setattr(self, 'recipe_window', None))

    def open_shopping_list_page(self):
        """Ouvre la page Listes de courses."""
        if not self.shopping_list_window:
            self.shopping_list_window = create_shopping_list_page()
            self.shopping_list_window.show()
            self.shopping_list_window.destroyed.connect(lambda: setattr(self, 'shopping_list_window', None))

    def open_dashboard_page(self):
        """Ouvre la page Tableau de bord."""
        if not self.dashboard_window:
            self.dashboard_window = create_dashboard_page()
            self.dashboard_window.show()
            self.dashboard_window.destroyed.connect(lambda: setattr(self, 'dashboard_window', None))

    def open_ingredient_page(self):
        """Ouvre la page Ingrédients."""
        if not self.ingredient_window:
            self.ingredient_window = create_ingredient_page()
            self.ingredient_window.show()
            self.ingredient_window.destroyed.connect(lambda: setattr(self, 'ingredient_window', None))

def create_main_page():
    """Crée et retourne une instance de MainPage."""
    main_page = MainPage()
    return main_page
