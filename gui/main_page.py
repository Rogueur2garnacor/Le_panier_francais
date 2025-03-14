from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
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

    # Créer un layout en grille
    grid_layout = QGridLayout(central_widget)
    grid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrer le contenu

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

def create_main_page() -> QMainWindow:
    """
    Crée et retourne la page principale avec un titre et une tuile 'Commencer'.
    
    Returns:
        QMainWindow: Une instance de la page principale.
    """
    # Créer la page principale
    main_page = create_base_page("Le panier français", 1200, 750, "gui/background.jpg")

    # Récupérer le layout central (QGridLayout)
    grid_layout = main_page.centralWidget().layout()

    # Ajouter un titre
    title_label = QLabel("Bienvenue dans Le Panier Français !")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("""
        font-size: 36px;
        font-weight: bold;
        color: white;
        background-color: transparent;
        font-family: 'Palatino Linotype', serif;
        padding-bottom: 20px;
    """)
    
    grid_layout.addWidget(title_label, 0, 0, 1, 2)  # Le titre occupe deux colonnes

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
            background: rgba(245, 245, 240, 0.25);
            border-color: rgba(245, 245, 240, 0.05);
            transform: scale(1.08);
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
        }
    """

    # Créer une tuile "Commencer"
    start_tile = create_tile(100, 200, tile_style, "Commencer")
    
    # Ajouter la tuile au layout en grille à une position spécifique
    grid_layout.addWidget(start_tile, 2,1 )  # Ligne : 1 | Colonne : 1

    return main_page
