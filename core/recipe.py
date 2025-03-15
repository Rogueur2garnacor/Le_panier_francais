# core/recipe.py
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records

def add_recipe(name: str, instructions: str, servings: int, category: str) -> None:
    try:
        """Ajoute une nouvelle recette."""
        recipe_data = {
            "name": name,
            "instructions": instructions,
            "servings": servings,
            "category": category
        }
        create_record("recipes", recipe_data)
    except Exception as e:
        print(f"L'erreur recipe 1.1 s'est produite : {e}")
    

def get_recipe(recipe_id: int) -> tuple:
    try:
        """Récupère une recette par son ID."""
        return get_record_by_id("recipes", recipe_id)   
    except Exception as e:
        print(f"L'erreur recipe 1.2 s'est produite : {e}")
 

def update_recipe(recipe_id: int, name: str, instructions: str, servings: int, category: str) -> None:
    try:
        """Met à jour une recette."""
        recipe_data = {
            "name": name,
            "instructions": instructions,
            "servings": servings,
            "category": category
        }
        update_record("recipes", recipe_id, recipe_data)
    except Exception as e:
        print(f"L'erreur recipe 1.3 s'est produite : {e}")
    

def delete_recipe(recipe_id: int) -> None:
    try:
        """Supprime une recette."""
        delete_record("recipes", recipe_id)
    except Exception as e:
        print(f"L'erreur recipe 1.4 s'est produite : {e}")
  

def get_all_recipes() -> list:
    try:
        """Récupère toutes les recettes."""
        return get_all_records("recipes")
    except Exception as e:
        print(f"L'erreur recipe 1.5 s'est produite : {e}")
    
