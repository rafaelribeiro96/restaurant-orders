import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.csv_reader = pd.read_csv(source_path).itertuples(index=False)

        obj = {}

        for dish_info in self.csv_reader:
            name, price, ingredient, amount = f_info
            if name not in obj:
                dish = Dish(name, price)
                obj[name] = dish
                self.dishes.add(dish)
            ingredient_obj = Ingredient(ingredient_name)
            obj[name].add_ingredient_dependency(ingredient_obj, amount)

    def __len__(self):
        return len(self.dishes)
