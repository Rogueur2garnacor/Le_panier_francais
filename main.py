from config import DB_PATH, TABLE_SCHEMAS
from data.database import create_tables , delete_database
from gui.windows import create_main_window
import sys

create_tables(str(DB_PATH), TABLE_SCHEMAS)
print(f"Base de données créée avec succès à l'emplacement : {DB_PATH}")

main_window, app = create_main_window()
main_window.show()
sys.exit(app.exec())