from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import QSize, Qt

def create_base_page(title: str, width: int, height: int, background_image_path: str) -> QMainWindow:
    try:
        """
        Crée une page vierge avec les paramètres spécifiés.
        
        Args:
            title (str): Le titre de la fenêtre.
            width (int): La largeur de la fenêtre.
            height (int): La hauteur de la fenêtre.
            background_image_path (str): Chemin vers l'image de fond.
        
        Returns:
            QMainWindow: Une instance de la fenêtre créée.
        """
        # Créer la fenêtre principale
        page = QMainWindow()
        page.setWindowTitle(title)
        page.setFixedSize(QSize(width, height))

        # Charger l'image de fond
        background_image = QPixmap(background_image_path)
        background_image = background_image.scaled(page.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        # Créer une palette pour le fond
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        page.setPalette(palette)
        page.setAutoFillBackground(True)

        # Créer un widget central
        central_widget = QWidget()
        page.setCentralWidget(central_widget)

        # Créer un layout en grille pour gérer les positions des widgets
        layout = QGridLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrer le contenu globalement

        return page
    except Exception as e:
        print(f"L'erreur main_page 1.1 s'est produite : {e}")
    

def create_tile(height: int, width: int, style: str, text: str) -> QPushButton:
    try:
        """
        Crée une tuile (QPushButton) avec les paramètres spécifiés.
        
        Args:
            height (int): Hauteur de la tuile.
            width (int): Largeur de la tuile.
            style (str): Style CSS à appliquer à la tuile.
            text (str): Texte affiché sur la tuile.
        
        Returns:
            QPushButton: Une instance de la tuile créée.
        """
        tile = QPushButton(text)
        tile.setFixedSize(QSize(width, height))
        tile.setStyleSheet(style)
        return tile
    except Exception as e:
        print(f"L'erreur main_page 1.2 s'est produite : {e}")
    

def create_title(text: str, style: str,height: int,width: int ) -> QPushButton:
    try:
        """
        Crée un titre sous forme de tuile avec des paramètres prédéfinis.
        
        Args:
            text (str): Texte du titre.
            style (str): Style CSS à appliquer au titre.
            height (int): Hauteur du titre.
            width (int): Largeur du titre.
        
        Returns:
            QPushButton: Une instance du titre créé sous forme de tuile.
        """
        return create_tile(height=height, width=width, style=style, text=text)
    except Exception as e:
        print(f"L'erreur main_page 1.3 s'est produite : {e}")
        
    
def clic_tile(tile: QPushButton, page_to_close: QMainWindow, page_to_open: QMainWindow) -> None:
    """
    When a tile is clicked:
    - Close the current page.
    - Open a new page.

    Args:
        tile (QPushButton): The tile that the user clicks on.
        page_to_close (QMainWindow): The current page to close.
        page_to_open (QMainWindow): The new page to open.
    """
    try:
        def on_click():
            # Fermer la page actuelle
            if page_to_close.isVisible():
                page_to_close.close()
                print(f"The page '{page_to_close.windowTitle()}' has been closed.")

            # Ouvrir la nouvelle page
            if not page_to_open.isVisible():
                page_to_open.show()
                print(f"The new page '{page_to_open.windowTitle()}' has been opened.")

        # Connecter le clic de la tuile à l'action
        tile.clicked.connect(on_click)
    except Exception as e:
        print(f"An error occurred in clic_tile: {e}")


def create_start_page() -> QMainWindow:
    try:
        # Créer la page principale
        start_page = create_base_page("Le panier français", 1200, 750, "gui/background.jpg")

        # Layout central
        layout = start_page.centralWidget().layout()

        # Style CSS pour le titre
        title_style = """
            QPushButton {
                font-size: 36px;
                font-weight: bold;
                color: white;
                background-color: transparent;
                border: none;
                font-family: 'Palatino Linotype', serif;
                margin-top: -70px; /* Déplace le titre légèrement plus haut */
            }
            QPushButton:hover {
                color: white; /* Aucun changement au survol */
                background-color: transparent;
            }
        """
        # Ajouter un titre centré en haut
        title_label = create_title("Le Panier Français !", style=title_style, height=100, width=1200)
        
        layout.addWidget(title_label, 0, 1, 1, 3)  # Le titre occupe toute la largeur en haut

        # Style CSS pour les tuiles
        tile_style = """
            QPushButton {
                font-size: 24px;
                font-weight: bold;
                color: black;
                background: rgba(245, 245, 240, 0.85);
                border: 2px solid rgba(245, 245, 240, 0.85);
                border-radius: 12px;
                padding: 12px;
                font-family: 'Palatino Linotype', serif;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                color: white;
                background: rgba(245, 245, 240, 0.25);
                border-color: rgba(245, 245, 240, 0.05);
                transform: scale(1.08);
                box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
            }
        """

       


        # Créer et ajouter les 5 tuiles
        tiles = [
            ("Inventaire", 1, 2),
            ("Recettes", 2, 2),
            ("Ingrédients", 3, 2),
            ("Listes de courses", 4, 2),
            ("Tableau de bord", 5, 2),            
        ]

        for tile_info in tiles:
            tile = create_tile(50, 250, tile_style, tile_info[0])
            if len(tile_info) > 4:
                layout.addWidget(tile, tile_info[1], tile_info[2], tile_info[3], tile_info[4])
            else:
                layout.addWidget(tile, tile_info[1], tile_info[2])

        return start_page
    except Exception as e:
        print(f"L'erreur main_page 1.6 s'est produite : {e}")


def create_main_page() -> QMainWindow:
    try:
        start_page = create_start_page()
        
        
        """
        Crée et retourne la page principale avec un titre et une tuile 'Commencer'.
        
        Returns:
            QMainWindow: Une instance de la page principale.
        """
        # Créer la page principale
        main_page = create_base_page("Le panier français", 1200, 750, "gui/background.jpg")

        # Layout central
        layout = main_page.centralWidget().layout()
        
        # Style CSS pour le titre
        title_style = """
            QPushButton {
                font-size: 36px;
                font-weight: bold;
                color: white;
                background-color: transparent;
                border: none;
                font-family: 'Palatino Linotype', serif;
                margin-top: -70px; /* Déplace le titre légèrement plus haut */
            }
            QPushButton:hover {
                color: white; /* Aucun changement au survol */
                background-color: transparent;
            }
        """
        # Ajouter un titre centré en haut
        title_label = create_title("Bienvenue dans Le Panier Français !", style=title_style, height=100, width=1200)
        
        layout.addWidget(title_label, 0, 0, 1, 3)  # Le titre occupe toute la largeur en haut

        # Ajouter un espace flexible entre le titre et la tuile avec une hauteur réduite
        spacer = QSpacerItem(200, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        layout.addItem(spacer, 1, 0)  # Ajouter un espace vide dans une ligne dédiée

        # Style CSS pour les tuiles
        tile_style = """
            QPushButton {
                font-size: 24px;
                font-weight: bold;
                color: black;
                background: rgba(245, 245, 240, 0.85);
                border: 2px solid rgba(245, 245, 240, 0.85);
                border-radius: 12px;
                padding: 12px;
                font-family: 'Palatino Linotype', serif;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                color: white;
                background: rgba(245, 245, 240, 0.25);
                border-color: rgba(245, 245, 240, 0.05);
                transform: scale(1.08);
                box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
            }
        """

        # Ajouter une tuile "Commencer" centrée au milieu
        start_tile = create_tile(100, 200, tile_style, "Commencer")       
        

        layout.addWidget(start_tile, 2, 1)  # La tuile est centrée au milieu du tableau

        # Connect the tile to change pages
        clic_tile(start_tile, main_page, start_page)

        return main_page
    
        

    except Exception as e:
        print(f"L'erreur main_page 1.5 s'est produite : {e}")



