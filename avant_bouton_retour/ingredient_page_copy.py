# gui/ingredient_page.py
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QLineEdit,
    QDialog,
    QDialogButtonBox,
    QMessageBox,
)
from PyQt6.QtCore import QSize, Qt
from core.ingredient import get_all_ingredients, add_ingredient, update_ingredient, delete_ingredient

class IngredientPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingrédients")
        self.setFixedSize(QSize(900, 600))

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QVBoxLayout(central_widget)

        # Titre
        title_label = QLabel("<h1>Gestion des Ingrédients</h1>")
        main_layout.addWidget(title_label)

        # Liste des ingrédients
        self.ingredient_list = QListWidget()
        self.load_ingredients()  # Charger les ingrédients depuis la base de données
        main_layout.addWidget(self.ingredient_list)

        # Layout pour les tuiles
        tile_layout = QGridLayout()
        main_layout.addLayout(tile_layout)

        # Taille des tuiles
        tile_width = 200
        tile_height = 100

        # Style CSS pour les tuiles
        tile_style = """
            font-size: 24px;
            font-family: Palatino;
            font-weight: bold;
        """

        # Tuile "Ajouter"
        add_button = QPushButton("Ajouter")
        add_button.setStyleSheet(tile_style)
        add_button.setFixedSize(QSize(tile_width, tile_height))
        add_button.clicked.connect(self.add_ingredient_dialog)
        tile_layout.addWidget(add_button, 0, 0)

        # Tuile "Modifier"
        edit_button = QPushButton("Modifier")
        edit_button.setStyleSheet(tile_style)
        edit_button.setFixedSize(QSize(tile_width, tile_height))
        edit_button.clicked.connect(self.edit_ingredient_dialog)
        tile_layout.addWidget(edit_button, 0, 1)

        # Tuile "Supprimer"
        delete_button = QPushButton("Supprimer")
        delete_button.setStyleSheet(tile_style)
        delete_button.setFixedSize(QSize(tile_width, tile_height))
        delete_button.clicked.connect(self.delete_ingredient)
        tile_layout.addWidget(delete_button, 0, 2)

    def load_ingredients(self):
        """Charge les ingrédients depuis la base de données et les affiche dans la liste."""
        self.ingredient_list.clear()
        ingredients = get_all_ingredients()
        for ingredient in ingredients:
            item = QListWidgetItem(f"{ingredient[1]} ({ingredient[2]})")  # Nom (Catégorie)
            item.setData(1000, ingredient[0])  # Stocker l'ID de l'ingrédient
            self.ingredient_list.addItem(item)

    def add_ingredient_dialog(self):
        """Affiche une boîte de dialogue pour ajouter un nouvel ingrédient."""
        dialog = AddIngredientDialog(self)
        if dialog.exec():
            name, category = dialog.get_inputs()
            add_ingredient(name, category)
            self.load_ingredients()  # Recharger la liste après l'ajout

    def edit_ingredient_dialog(self):
        """Affiche une boîte de dialogue pour modifier l'ingrédient sélectionné."""
        selected_item = self.ingredient_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Sélection requise", "Veuillez sélectionner un ingrédient à modifier.")
            return

        ingredient_id = selected_item.data(1000)  # Récupérer l'ID de l'ingrédient
        ingredient_name = selected_item.text().split(" (")[0]  # Extraire le nom

        dialog = EditIngredientDialog(self, ingredient_name)
        if dialog.exec():
            name, category = dialog.get_inputs()
            update_ingredient(ingredient_id, name, category)
            self.load_ingredients()  # Recharger la liste après la modification

    def delete_ingredient(self):
        """Supprime l'ingrédient sélectionné."""
        selected_item = self.ingredient_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Sélection requise", "Veuillez sélectionner un ingrédient à supprimer.")
            return

        ingredient_id = selected_item.data(1000)  # Récupérer l'ID de l'ingrédient
        reply = QMessageBox.question(self, "Supprimer l'ingrédient",
                                    "Êtes-vous sûr de vouloir supprimer cet ingrédient ?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            delete_ingredient(ingredient_id)
            self.load_ingredients()  # Recharger la liste après la suppression

class AddIngredientDialog(QDialog):
    """Boîte de dialogue pour ajouter un ingrédient."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ajouter un ingrédient")
        self.name = QLineEdit(self)
        self.category = QLineEdit(self)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Nom:"))
        layout.addWidget(self.name)
        layout.addWidget(QLabel("Catégorie:"))
        layout.addWidget(self.category)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
                                   Qt.Orientation.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_inputs(self):
        """Retourne les valeurs entrées par l'utilisateur."""
        return self.name.text(), self.category.text()

class EditIngredientDialog(QDialog):
    """Boîte de dialogue pour modifier un ingrédient."""
    def __init__(self, parent=None, ingredient_name: str = ""):
        super().__init__(parent)
        self.setWindowTitle("Modifier l'ingrédient")
        self.name = QLineEdit(self)
        self.name.setText(ingredient_name)  # Pré-remplir avec le nom existant
        self.category = QLineEdit(self)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Nom:"))
        layout.addWidget(self.name)
        layout.addWidget(QLabel("Catégorie:"))
        layout.addWidget(self.category)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
                                   Qt.Orientation.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_inputs(self):
        """Retourne les valeurs entrées par l'utilisateur."""
        return self.name.text(), self.category.text()

def create_ingredient_page():
    """Crée et retourne une instance de IngredientPage."""
    ingredient_page = IngredientPage()
    return ingredient_page
