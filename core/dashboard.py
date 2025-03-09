# core/dashboard.py
import sqlite3
from config import DB_PATH


def get_total_items() -> int:
    """Retourne le nombre total d'articles dans l'inventaire."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM items")
        total_items = cursor.fetchone()[0]
        return total_items
    except sqlite3.Error as e:
        print(f"Erreur lors du comptage des articles : {e}")
        return 0
    finally:
        conn.close()


def get_low_stock_items() -> list:
    """Retourne une liste des articles en dessous du seuil bas."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT name, quantity, low_threshold FROM items WHERE quantity < low_threshold")
        low_stock_items = cursor.fetchall()
        return low_stock_items
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des articles en stock faible : {e}")
        return []
    finally:
        conn.close()


def get_most_used_items_in_recipes() -> list:
    """Retourne une liste des articles les plus fréquemment utilisés dans les recettes."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = """
            SELECT items.name, COUNT(recipe_ingredients.item_id) AS usage_count
            FROM recipe_ingredients
            INNER JOIN items ON recipe_ingredients.item_id = items.id
            GROUP BY recipe_ingredients.item_id
            ORDER BY usage_count DESC
            LIMIT 10
        """
        cursor.execute(sql)
        most_used_items = cursor.fetchall()
        return most_used_items
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des articles les plus utilisés : {e}")
        return []
    finally:
        conn.close()


def get_total_recipes() -> int:
    """Retourne le nombre total de recettes enregistrées."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM recipes")
        total_recipes = cursor.fetchone()[0]
        return total_recipes
    except sqlite3.Error as e:
        print(f"Erreur lors du comptage des recettes : {e}")
        return 0
    finally:
        conn.close()


def get_most_popular_recipes() -> list:
    """Retourne une liste des recettes les plus populaires."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = """
            SELECT recipes.name, COUNT(weekly_menu.recipe_id) AS popularity_count
            FROM weekly_menu
            INNER JOIN recipes ON weekly_menu.recipe_id = recipes.id
            GROUP BY weekly_menu.recipe_id
            ORDER BY popularity_count DESC
            LIMIT 10
        """
        cursor.execute(sql)
        popular_recipes = cursor.fetchall()
        return popular_recipes
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des recettes populaires : {e}")
        return []
    finally:
        conn.close()


def get_most_frequent_shopping_list_items() -> list:
    """Retourne une liste des items les plus fréquemment ajoutés aux listes de courses."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = """
            SELECT items.name, COUNT(shopping_list_items.item_id) AS frequency_count
            FROM shopping_list_items
            INNER JOIN items ON shopping_list_items.item_id = items.id
            GROUP BY shopping_list_items.item_id
            ORDER BY frequency_count DESC
            LIMIT 10
        """
        cursor.execute(sql)
        frequent_items = cursor.fetchall()
        return frequent_items
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des items fréquents : {e}")
        return []
    finally:
        conn.close()


def get_weekly_menu() -> list:
    """Retourne le menu de la semaine actuel."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        sql = """
            SELECT weekly_menu.date, recipes.name 
            FROM weekly_menu 
            INNER JOIN recipes ON weekly_menu.recipe_id = recipes.id 
            ORDER BY weekly_menu.date ASC
        """
        cursor.execute(sql)
        weekly_menu = cursor.fetchall()
        return weekly_menu
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération du menu de la semaine : {e}")
        return []
    finally:
        conn.close()
