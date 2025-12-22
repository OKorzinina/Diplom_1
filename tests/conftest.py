
"""
Общие фикстуры для тестов
"""
import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Тестовая булочка"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce_ingredient():
    """Фикстура для создания мока соуса"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "кетчуп"
    ingredient.get_price.return_value = 50.0
    return ingredient


@pytest.fixture
def mock_filling_ingredient():
    """Фикстура для создания мока начинки"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "котлета"
    ingredient.get_price.return_value = 100.0
    return ingredient


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_sauce_ingredient, mock_filling_ingredient):
    """Фикстура для создания бургера с ингредиентами"""
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce_ingredient)
    burger.add_ingredient(mock_filling_ingredient)
    return burger
