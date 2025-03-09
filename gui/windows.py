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
from gui.main_page import create_main_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Le Panier Français")
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

        # Créer un layout vertical
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        button.clicked.connect(self.go_to_main_page)

        self.main_page = None  # Pour stocker la référence à la fenêtre principale

    def go_to_main_page(self):
        """Fonction pour passer à la fenêtre principale."""
        self.main_page = create_main_page()  # Stocke la fenêtre principale
        self.main_page.show()
        self.close()  # Ferme la fenêtre de démarrage

def create_main_window():
    """Crée et retourne une instance de MainWindow."""
    app = QApplication(sys.argv)
    main_window = MainWindow()
    return main_window, app
