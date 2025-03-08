# core/shopping_list.py
import sqlite3
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records
from config import DB_PATH


def add_shopping_list(name: str) -> None:
    """Ajoute une nouvelle liste de courses."""
    if not name:
        raise ValueError("The name of the shopping list cannot be empty.")
         
    shopping_list_data = {
        "name": name
    }
    create_record("shopping_lists", shopping_list_data)


def get_shopping_list(shopping_list_id: int) -> tuple:
    """Récupère une liste de courses par son ID."""
    return get_record_by_id("shopping_lists", shopping_list_id)


def update_shopping_list(shopping_list_id: int, name: str) -> None:
    """Met à jour une liste de courses."""
    if not name:
        raise ValueError("Le nom de la liste de courses ne peut pas être vide.")

    shopping_list_data = {
        "name": name
    }
    update_record("shopping_lists", shopping_list_id, shopping_list_data)


def delete_shopping_list(shopping_list_id: int) -> None:
    """Supprime une liste de courses."""
    delete_record("shopping_lists", shopping_list_id)


def get_all_shopping_lists() -> list:
    """Récupère toutes les listes de courses."""
    return get_all_records("shopping_lists")


def add_item_to_shopping_list(shopping_list_id: int, item_id: int, quantity_needed: float) -> None:
    """Ajoute un item à une liste de courses."""
    shopping_list_item_data = {
        "list_id": shopping_list_id,
        "item_id": item_id,
        "quantity_needed": quantity_needed
    }
    create_record("shopping_list_items", shopping_list_item_data)


def get_shopping_list_items(shopping_list_id: int) -> list:
    """Récupère tous les items d'une liste de courses."""
    conn = sqlite3.connect(DB_PATH)  # Connexion locale
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM shopping_list_items WHERE list_id = ?"
        cursor.execute(sql, (shopping_list_id,))
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des enregistrements dans shopping_list_items: {e}")
        return []
    finally:
        conn.close()


def delete_item_from_shopping_list(shopping_list_id: int, item_id: int) -> None:
    """Supprime un item d'une liste de courses."""
    conn = sqlite3.connect(DB_PATH)  # Connexion locale
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM shopping_list_items WHERE list_id = ? AND item_id = ?"
        cursor.execute(sql, (shopping_list_id, item_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression de l'enregistrement dans shopping_list_items: {e}")
        conn.rollback()
    finally:
        conn.close()
