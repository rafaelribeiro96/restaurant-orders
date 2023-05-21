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
            if dish_info.name not in obj:
                dish = Dish(dish_info.name, dish_info.price)
                obj[dish_info.name] = dish
                self.dishes.add(dish)
            ingredient_obj = Ingredient(dish_info.ingredient)
            obj[dish_info.name].add_ingredient_dependency(ingredient_obj, dish_info.amount)

    def __len__(self):
        return self.__length
