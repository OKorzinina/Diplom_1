import pytest
from praktikum.bun import Bun

class TestBun:
    def test_bun_initialization(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_name() == "black bun"
        assert bun.get_price() == 100.0

    @pytest.mark.parametrize("name,price", [
        ("Black bun", 100.0),
        ("White bun", 200.0),
        ("Red bun", 250.5),
    ])
    def test_bun_getters_with_different_values(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_price_is_float(self):
        """Check that price works as float"""
        # Test with float
        bun = Bun("Test bun", 100.0)
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() == 100.0
        
        # Test with int 
        bun2 = Bun("Test bun 2", 200)
        # Don't check type, just check arithmetic works
        total = bun.get_price() + bun2.get_price()
        assert total == 300.0
