#class Ingredient:
   # """
   # Модель ингредиента.
   # Ингредиент: начинка или соус.
    #У ингредиента есть тип (начинка или соус), название и цена.
    #"""
   # =
    #def get_price(self) -> float:
      #  return self.price

    #def get_name(self) -> str:
        #return self.name

   # def get_type(self) -> str:
        #return self.type

import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_ingredient_creation(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 50.0)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "Ketchup"
        assert ingredient.price == 50.0

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Cheese", 70.0)
        assert ingredient.get_price() == 70.0

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Mustard", 40.0)
        assert ingredient.get_name() == "Mustard"

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Bacon", 90.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
