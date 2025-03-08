import sqlite3
from typing import List, Tuple, Optional, Dict, Any
from config import DB_PATH  # Importez DB_PATH

def create_record(table_name: str, data: Dict[str, Any]) -> None:
    """Crée un nouvel enregistrement dans la table spécifiée."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(data.values()))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur lors de la création de l'enregistrement dans {table_name}: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_record_by_id(table_name: str, record_id: int) -> Optional[Tuple]:
    """Récupère un enregistrement par son ID dans la table spécifiée."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = f"SELECT * FROM {table_name} WHERE id = ?"
        cursor.execute(sql, (record_id,))
        record = cursor.fetchone()
        return record
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération de l'enregistrement dans {table_name}: {e}")
        return None
    finally:
        conn.close()

def update_record(table_name: str, record_id: int, data: Dict[str, Any]) -> None:
    """Met à jour un enregistrement existant dans la table spécifiée."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        set_clause = ", ".join(f"{column} = ?" for column in data.keys())
        sql = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        values = tuple(data.values()) + (record_id,)
        cursor.execute(sql, values)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur lors de la mise à jour de l'enregistrement dans {table_name}: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_record(table_name: str, record_id: int) -> None:
    """Supprime un enregistrement de la table spécifiée."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = f"DELETE FROM {table_name} WHERE id = ?"
        cursor.execute(sql, (record_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression de l'enregistrement dans {table_name}: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_all_records(table_name: str) -> List[Tuple]:
    """Récupère tous les enregistrements de la table spécifiée."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des enregistrements dans {table_name}: {e}")
        return []
    finally:
        conn.close()
    