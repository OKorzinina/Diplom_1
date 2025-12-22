import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("", 0),
        ("special bun with long name", -10)
    ])
    def test_bun_initialization_and_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

