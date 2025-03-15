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
    try:
        try:
            create_tables(str(DB_PATH), TABLE_SCHEMAS)
            print(f"Base de données créée avec succès à l'emplacement : {DB_PATH}")
        except Exception as e:
            print(f"L'erreur main 1.1 s'est produite : {e}")
            

        """Point d'entrée principal de l'application."""
        try:
            app = QApplication(sys.argv)
            main_window = create_main_page()
            main_window.show()
            sys.exit(app.exec())
        except Exception as e:
            print(f"L'erreur main 1.2 s'est produite : {e}")   
    except Exception as e:
        print(f"L'erreur main 1.3 s'est produite : {e}") 
    

"""
Main code"""

if __name__ == "__main__":
    main()
