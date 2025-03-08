from config import DB_PATH, TABLE_SCHEMAS
from data.database import create_tables , delete_database


create_tables(str(DB_PATH), TABLE_SCHEMAS)
print(f"Base de données créée avec succès à l'emplacement : {DB_PATH}")
