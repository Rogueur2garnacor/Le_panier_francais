# core/inventory.py
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records

def add_item(name: str, quantity: float, unit: str, low_threshold: float, high_threshold: float, expiration_date: str) -> None:
    """Ajoute un nouvel item à l'inventaire."""
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not isinstance(quantity, (int, float)):
        raise TypeError("quantity must be a number")
    if not isinstance(unit, str):
        raise TypeError("unit must be a string")
    if not isinstance(low_threshold, (int, float)):
        raise TypeError("low_threshold must be a number")
    if not isinstance(high_threshold, (int, float)):
        raise TypeError("high_threshold must be a number")
    if not isinstance(expiration_date, str):
        raise TypeError("expiration_date must be a string")
    
    item_data = {
        "name": name,
        "quantity": quantity,
        "unit": unit,
        "low_threshold": low_threshold,
        "high_threshold": high_threshold,
        "expiration_date": expiration_date
    }
    create_record("items", item_data)

def get_item(item_id: int) -> tuple:
    """Récupère un item de l'inventaire par son ID."""
    return get_record_by_id("items", item_id)

def update_item(item_id: int, name: str, quantity: float, unit: str, low_threshold: float, high_threshold: float, expiration_date: str) -> None:
    """Met à jour un item dans l'inventaire."""
    item_data = {
        "name": name,
        "quantity": quantity,
        "unit": unit,
        "low_threshold": low_threshold,
        "high_threshold": high_threshold,
        "expiration_date": expiration_date
    }
    update_record("items", item_id, item_data)

def delete_item(item_id: int) -> None:
    """Supprime un item de l'inventaire."""
    delete_record("items", item_id)

def get_all_items() -> list:
    """Récupère tous les items de l'inventaire."""
    return get_all_records("items")
