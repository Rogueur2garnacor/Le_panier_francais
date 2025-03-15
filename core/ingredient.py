# core/ingredient.py
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records

def add_ingredient(name: str, category: str) -> None:
    try:
        """Ajoute un nouvel ingrédient."""
        ingredient_data = {
            "name": name,
            "category": category
        }
        create_record("ingredients", ingredient_data)
    except Exception as e:
        print(f"L'erreur ingredient 1.1 s'est produite: {e}")
    

def get_ingredient(ingredient_id: int) -> tuple:
    try:
        """Récupère un ingrédient par son ID."""
        return get_record_by_id("ingredients", ingredient_id)
    except Exception as e:
        print(f"L'erreur ingredient 1.2 s'est produite: {e}")
    

def update_ingredient(ingredient_id: int, name: str, category: str) -> None:
    try:
        """Met à jour un ingrédient."""
        ingredient_data = {
            "name": name,
            "category": category
        }
        update_record("ingredients", ingredient_id, ingredient_data)
    except Exception as e:
        print(f"L'erreur ingredient 1.3 s'est produite: {e}")
    
   
def delete_ingredient(ingredient_id: int) -> None:
    try:
        """Supprime un ingrédient."""
        delete_record("ingredients", ingredient_id)
    except Exception as e:
        print(f"L'erreur ingredient 1.4 s'est produite: {e}")
   

def get_all_ingredients() -> list:
    try:
        """Récupère tous les ingrédients."""
        return get_all_records("ingredients")
    except Exception as e:
        print(f"L'erreur ingredient 1.5 s'est produite: {e}")
    
