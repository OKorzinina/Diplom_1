"""
Тесты для класса Ingredient из ingredient.py
"""
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тестирование модели ингредиента"""

    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "Острый соус", 50.0),
        (INGREDIENT_TYPE_FILLING, "Котлета", 100.0),
        (INGREDIENT_TYPE_SAUCE, "Сырный соус", 75.5),
        (INGREDIENT_TYPE_FILLING, "Салат", 30.0),
    ])
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):
        """Параметризованный тест инициализации и геттеров ингредиента"""
        # Arrange & Act
        ingredient = Ingredient(ingredient_type, name, price)

        # Assert
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_types_constants(self):
        """Проверка констант типов ингредиентов"""
        # Arrange & Act
        sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Кетчуп", 40.0)
        filling_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Бекон", 120.0)

        # Assert
        assert sauce_ingredient.get_type() == "SAUCE"
        assert filling_ingredient.get_type() == "FILLING"

    def test_ingredient_price_is_float(self):
        """Проверка, что цена ингредиента возвращается как float"""
        # Arrange & Act
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Майонез", 45)

        # Assert
        assert isinstance(ingredient.get_price(), float)
        assert ingredient.get_price() == 45.0
