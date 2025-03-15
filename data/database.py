import sqlite3
import os
from typing import Dict, List
from pathlib import Path

def create_tables(db_path: str, table_definitions: Dict[str, List[str]]):
    try:
        """Crée les tables si elles n'existent pas."""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        try:
            for table_name, columns in table_definitions.items():
                sql_statement = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)});"
                cursor.execute(sql_statement)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erreur SQL: {e}")
            conn.rollback()
        finally:
            conn.close()
    except sqlite3.Error as e:
        print(f"L'erreur database 1.1 s'est produite: {e}")


def delete_database(db_path: str):
    try:
        """Supprime la base de données de manière plus robuste"""
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
            except OSError as e:
                print(f"Erreur lors de la suppression de la base de données: {e}")
        else:
            print(f"La base de données {db_path} n'existe pas.")
    except Exception as e:
        print(f"L'erreur database 1.2 s'est produite: {e}")