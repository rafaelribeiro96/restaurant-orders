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
            if get_info.name not in obj:
                dish = Dish(get_info.name, get_info.price)
                obj[get_info.name] = dish
                self.dishes.add(dish)
            get_ingredients = Ingredient(get_info.ingredient)
            obj[get_info.name].add_ingredient_dependency(get_ingredients, get_info.amount)

    def __len__(self):
        return self.__length
