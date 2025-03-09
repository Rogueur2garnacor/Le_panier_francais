# gui/retour_page.py
from PyQt6.QtWidgets import QMainWindow
from gui.main_page import create_main_page

def go_to_main_page(current_window):
    """
    Crée et affiche la page principale, puis ferme la fenêtre actuelle.
    Args:
        current_window: La fenêtre actuelle à fermer.
    """
    main_page = create_main_page()
    main_page.show()
    current_window.close()
