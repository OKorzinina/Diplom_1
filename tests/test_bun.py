"""
Тесты для класса Bun из bun.py
"""
import pytest


class TestBun:
    """Тестирование модели булочки для бургера"""

    def test_bun_initialization(self):
        """Проверка инициализации булочки с названием и ценой"""
        # Arrange
        name = "Красная булочка"
        price = 150.0

        # Act
        bun = Bun(name, price)

        # Assert
        assert bun.get_name() == name
        assert bun.get_price() == price

    @pytest.mark.parametrize("name,price", [
        ("Черная булочка", 100.0),
        ("Белая булочка", 200.0),
        ("Солнечная булочка", 250.5),
    ])
    def test_bun_getters_with_different_values(self, name, price):
        """Параметризованный тест для разных значений булочек"""
        # Arrange & Act
        bun = Bun(name, price)

        # Assert
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_price_is_float(self):
        """Проверка, что цена возвращается как float"""
        # Arrange & Act
        bun = Bun("Тестовая булочка", 100)

        # Assert
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() == 100.0
