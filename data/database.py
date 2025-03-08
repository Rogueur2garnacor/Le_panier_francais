import sqlite3
import os
from typing import Dict, List
from pathlib import Path

def create_tables(db_path: str, table_definitions: Dict[str, List[str]]):
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

def delete_database(db_path: str):
    """Supprime la base de données de manière plus robuste"""
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except OSError as e:
            print(f"Erreur lors de la suppression de la base de données: {e}")
    else:
        print(f"La base de données {db_path} n'existe pas.")