from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    pizza = 'pizza'

    dish_feijoada = Dish("feijoada", 35.00)
    dish_pizza_first = Dish(pizza, 38.00)
    dish_pizza_second = Dish(pizza, 38.00)

    assert dish_pizza_first.name == pizza
    assert repr(dish_pizza_first) == f"Dish('{pizza}', R${38.00:.2f})"

    assert dish_pizza_first.__eq__(dish_pizza_second) is True
    assert dish_pizza_first.__eq__(dish_feijoada) is False

    assert hash(dish_pizza_first) == hash(dish_pizza_second)
    assert hash(dish_pizza_first) != hash(dish_feijoada)

    with pytest.raises(TypeError):
        Dish(pizza, "trinta e oito")

    with pytest.raises(ValueError):
        Dish(pizza, 0)

    ingredient_salmao = Ingredient('salmão')
    ingredient_camarao = Ingredient('camarão')

    dish_pizza_first.add_ingredient_dependency(ingredient_salmao, 5)
    dish_pizza_first.add_ingredient_dependency(ingredient_camarao, 35)

    assert dish_pizza_first.get_ingredients() == {
        ingredient_salmao,
        ingredient_camarao,
    }

    assert dish_pizza_first.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
