# core/recipe.py
from data.db_queries import create_record, get_record_by_id, update_record, delete_record, get_all_records

def add_recipe(name: str, instructions: str, servings: int, category: str) -> None:
    """Ajoute une nouvelle recette."""
    recipe_data = {
        "name": name,
        "instructions": instructions,
        "servings": servings,
        "category": category
    }
    create_record("recipes", recipe_data)

def get_recipe(recipe_id: int) -> tuple:
    """Récupère une recette par son ID."""
    return get_record_by_id("recipes", recipe_id)

def update_recipe(recipe_id: int, name: str, instructions: str, servings: int, category: str) -> None:
    """Met à jour une recette."""
    recipe_data = {
        "name": name,
        "instructions": instructions,
        "servings": servings,
        "category": category
    }
    update_record("recipes", recipe_id, recipe_data)

def delete_recipe(recipe_id: int) -> None:
    """Supprime une recette."""
    delete_record("recipes", recipe_id)

def get_all_recipes() -> list:
    """Récupère toutes les recettes."""
    return get_all_records("recipes")
