from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import QSize, Qt

def create_base_page(title: str, width: int, height: int, background_image_path: str) -> QMainWindow:
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

def create_tile(height: int, width: int, style: str, text: str) -> QPushButton:
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

def create_title(text: str, style: str,height: int,width: int ) -> QPushButton:
    """
    Crée un titre sous forme de tuile avec des paramètres prédéfinis.

    Args:
        text (str): Texte du titre.
        style (str): Style CSS à appliquer au titre.
        height (int): Hauteur du titre.
        with (int): Largeur du titre.
    Returns:
        QPushButton: Une instance du titre créé sous forme de tuile.
    """
    return create_tile(height=height, width=width, style=style, text=text)


def create_main_page() -> QMainWindow:
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

    return main_page
