from pathlib import Path
import data.database as db

# Configuration centrale
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "data" / "inventory.db"

# Définition des tables au format {nom: [colonnes]}
TABLE_SCHEMAS = {
    "items": [
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
        "name TEXT UNIQUE NOT NULL",
        "quantity REAL NOT NULL",
        "unit TEXT",
        "low_threshold REAL",
        "high_threshold REAL",
        "expiration_date DATE"
    ],
    "recipes": [
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
        "name TEXT NOT NULL",
        "instructions TEXT",
        "servings INTEGER",
        "category TEXT"
    ],
    "recipe_ingredients": [
        "recipe_id INTEGER",
        "item_id INTEGER",
        "quantity REAL NOT NULL",
        "FOREIGN KEY(recipe_id) REFERENCES recipes(id)",
        "FOREIGN KEY(item_id) REFERENCES items(id)"
    ],
    "shopping_lists": [
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "name TEXT"
    ],
    "shopping_list_items": [
        "list_id INTEGER",
        "item_id INTEGER",
        "quantity_needed REAL NOT NULL",
        "FOREIGN KEY(list_id) REFERENCES shopping_lists(id)",
        "FOREIGN KEY(item_id) REFERENCES items(id)"
    ],
    "weekly_menu": [
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
        "date DATE UNIQUE NOT NULL",
        "recipe_id INTEGER",
        "FOREIGN KEY(recipe_id) REFERENCES recipes(id)"
    ],
    "purchase_history": [
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
        "item_id INTEGER",
        "quantity REAL NOT NULL",
        "purchase_date DATE NOT NULL",
        "FOREIGN KEY(item_id) REFERENCES items(id)"
    ],
}

# Création de la base au premier import
DB_PATH.parent.mkdir(exist_ok=True)
db.create_tables(str(DB_PATH), TABLE_SCHEMAS)