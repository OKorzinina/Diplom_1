import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
        (INGREDIENT_TYPE_SAUCE, "cheese sauce", 150.5),
        (INGREDIENT_TYPE_FILLING, "salad", 30.0),
    ])
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_types(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50.0)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 120.0)
        assert sauce.get_type() == "SAUCE"
        assert filling.get_type() == "FILLING"

    def test_ingredient_price_is_numeric(self):
        """Check that price works numerically"""
        # Test with float
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mayonnaise", 45.0)
        assert ingredient.get_price() == 45.0
        
        # Test with int
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "lettuce", 30)
        # Just check arithmetic works, not type
        total = ingredient.get_price() + ingredient2.get_price()
        assert total == 75.0
