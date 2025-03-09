# core/ingredient.py
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records

def add_ingredient(name: str, category: str) -> None:
    """Ajoute un nouvel ingrédient."""
    ingredient_data = {
        "name": name,
        "category": category
    }
    create_record("ingredients", ingredient_data)

def get_ingredient(ingredient_id: int) -> tuple:
    """Récupère un ingrédient par son ID."""
    return get_record_by_id("ingredients", ingredient_id)

def update_ingredient(ingredient_id: int, name: str, category: str) -> None:
    """Met à jour un ingrédient."""
    ingredient_data = {
        "name": name,
        "category": category
    }
    update_record("ingredients", ingredient_id, ingredient_data)

def delete_ingredient(ingredient_id: int) -> None:
    """Supprime un ingrédient."""
    delete_record("ingredients", ingredient_id)

def get_all_ingredients() -> list:
    """Récupère tous les ingrédients."""
    return get_all_records("ingredients")
