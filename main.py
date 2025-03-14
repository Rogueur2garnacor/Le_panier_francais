# -*- coding: utf-8 -*-

"""
Imporotation des modules nécessaires pour le bon fonctionnement de l'application.
"""
from config import DB_PATH, TABLE_SCHEMAS
from data.database import create_tables , delete_database
from gui.main_page import *
import sys
from PyQt6.QtWidgets import QApplication

"""
Déclaration des variables globales.
"""



"""
Déclaration des fonctions
"""


def main():
    
    create_tables(str(DB_PATH), TABLE_SCHEMAS)
    print(f"Base de données créée avec succès à l'emplacement : {DB_PATH}")


    """Point d'entrée principal de l'application."""
    app = QApplication(sys.argv)
    main_window = create_main_page()
    main_window.show()
    sys.exit(app.exec())
    
    

"""
Main code"""

if __name__ == "__main__":
    main()
