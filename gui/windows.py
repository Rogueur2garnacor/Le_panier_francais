# gui/windows.py
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import Qt, QSize

def create_main_window():
    """Crée la fenêtre principale de l'application."""
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Le Panier Français")

    # Définir la taille de la fenêtre
    main_window.setFixedSize(QSize(1200, 750))

    # Charger l'image de fond
    background_image = QPixmap("gui/background.jpg")  # Assurez-vous que le chemin est correct
    background_image = background_image.scaled(main_window.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)

    # Créer une palette pour le fond
    palette = QPalette()
    palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
    main_window.setPalette(palette)
    main_window.setAutoFillBackground(True)

    # Créer un widget central
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)

    # Créer un layout vertical
    layout = QVBoxLayout(central_widget)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrer le contenu

    # Ajouter un label avec un style personnalisé
    label = QLabel("Bienvenue dans\nLe Panier Français !")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet("""
        font-size: 36px;
        font-weight: bold;
        color: white;
        background-color: transparent;
    """)
    layout.addWidget(label)

    # Ajouter un bouton avec un style personnalisé
    button = QPushButton("Entrer")
    button.setStyleSheet("""
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 24px;
        font-weight: bold;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    """)
    layout.addWidget(button)
    # button.clicked.connect(app.quit)  # Connecter le bouton à la fonction de fermeture de l'application
    
    #TODO : Connect button to next window

    return main_window, app
