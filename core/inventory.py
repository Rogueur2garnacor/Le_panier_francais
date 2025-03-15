# core/inventory.py
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records

def add_item(name: str, quantity: float, unit: str, low_threshold: float, high_threshold: float, expiration_date: str) -> None:
    try:
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
    except Exception as e:
        print(f"L'erreur inventory 1.1 s'est produite: {e}")
    

def get_item(item_id: int) -> tuple:
    try:
        """Récupère un item de l'inventaire par son ID."""
        return get_record_by_id("items", item_id)
    except Exception as e:
        print(f"L'erreur inventory 1.2 s'est produite: {e}")
   

def update_item(item_id: int, name: str, quantity: float, unit: str, low_threshold: float, high_threshold: float, expiration_date: str) -> None:
    try:
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
    except Exception as e:
        print(f"L'erreur inventory 1.3 s'est produite: {e}")
    

def delete_item(item_id: int) -> None:
    try:
        """Supprime un item de l'inventaire."""
        delete_record("items", item_id)
    except Exception as e:
        print(f"L'erreur inventory 1.4 s'est produite: {e}")
    
def get_all_items() -> list:
    try:
        """Récupère tous les items de l'inventaire."""
        return get_all_records("items")     
    except Exception as e:
        print(f"L'erreur inventory 1.5 s'est produite: {e}")
