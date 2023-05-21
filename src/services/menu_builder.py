import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, res=None) -> pd.DataFrame:
        arr = []

        for recipe in self.menu_data.dishes:
            obj = {
                    "dish_name": recipe.name,
                    "ingredients": recipe.get_ingredients(),
                    "price": recipe.price,
                    "restrictions": recipe.get_restrictions(),
                }
            if res not in recipe.get_restrictions():
                arr.append(obj)
        return pd.DataFrame(arr)
