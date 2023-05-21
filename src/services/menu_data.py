import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.csv_reader = pd.read_csv(source_path).itertuples(index=False)
        self.dishes = set()

        obj = {}
        for get_info in self.csv_reader:
            name, price, ingredient, amount = get_info
            if name not in obj:
                dish = Dish(name, price)
                obj[name] = dish
                self.dishes.add(dish)
            get_ingredients = Ingredient(ingredient)
            obj[name].add_ingredient_dependency(get_ingredients, amount)

    def __len__(self):
        return self.__length
