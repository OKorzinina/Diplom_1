#from typing import List

#from praktikum.bun import Bun
#from praktikum.ingredient import Ingredient


#class Burger:
   #"""
    #Модель бургера.
    #Бургер состоит из булочек и ингредиентов (начинка или соус).
    #Ингредиенты можно перемещать и удалять.
    #Можно распечать чек с информацией о бургере.
    #"""

    #def __init__(self):
        #self.bun = None
        #self.ingredients: List[Ingredient] = []

    #def set_buns(self, bun: Bun):
        #self.bun = bun

    #def add_ingredient(self, ingredient: Ingredient):
        #self.ingredients.append(ingredient)

    #def remove_ingredient(self, index: int):
        #del self.ingredients[index]

    #def move_ingredient(self, index: int, new_index: int):
        #self.ingredients.insert(new_index, self.ingredients.pop(index))

    #def get_price(self) -> float:
        #price = self.bun.get_price() * 2

        #for ingredient in self.ingredients:
            #price += ingredient.get_price()

        #return price

    #def get_receipt(self) -> str:
        #receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']

        #for ingredient in self.ingredients:
            #receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')

       # receipt.append(f'(==== {self.bun.get_name()} ====)\n')
       # receipt.append(f'Price: {self.get_price()}')

        #return '\n'.join(receipt)






import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 50
        bun.get_name.return_value = "Mock Bun"
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient1
        assert burger.ingredients[1] == ingredient2

    def test_get_price(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 50
        burger.set_buns(bun)

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 20
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 30
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert burger.get_price() == 150.0  # 50*2 + 20 + 30

    def test_get_receipt(self, mocker):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Mock Bun"
        bun.get_price.return_value = 50
        burger.set_buns(bun)

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = "Mock Sauce"
        ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient1.get_price.return_value = 20
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = "Mock Filling"
        ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient2.get_price.return_value = 30
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_receipt = (
            "(==== Mock Bun ====)\n"
            "= sauce Mock Sauce =\n"
            "= filling Mock Filling =\n"
            "(==== Mock Bun ====)\n"
            "Price: 150.0"
        )

        assert burger.get_receipt() == expected_receipt
