from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    bacon = "bacon"
    shrimp = "camarão"

    ingredient_shrimp = Ingredient(shrimp)
    ingredient_bacon = Ingredient(bacon)
    ingredient_bacon_two = Ingredient(bacon)

    assert ingredient_bacon.name == bacon
    assert repr(ingredient_bacon) == f"Ingredient('{bacon}')"

    assert hash(ingredient_bacon) == hash(ingredient_bacon_two)
    assert hash(ingredient_bacon) != hash(ingredient_shrimp)

    assert ingredient_bacon.__eq__(ingredient_bacon_two) is True
    assert ingredient_bacon.__eq__(ingredient_shrimp) is False

    bacon_restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert ingredient_bacon.restrictions == bacon_restrictions
