import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        # Меняем местами
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    def test_get_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ing = Mock()
        mock_ing.get_price.return_value = 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        # Цена = (100 * 2) + 50 = 250
        assert burger.get_price() == 250

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        mock_ing = Mock()
        mock_ing.get_name.return_value = "hot sauce"
        mock_ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ing.get_price.return_value = 100

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()

        # Проверяем наличие ключевых строк в чеке
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "Price: 300" in receipt

