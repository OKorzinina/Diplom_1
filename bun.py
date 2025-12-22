# class Bun:
   # """
   # Модель булочки для бургера.
   # Булочке можно дать название и назначить цену.
   # """
#
   # def __init__(self, name: str, price: float):
       # self.name = name
       # self.price = price

    #def get_name(self) -> str:
       # return self.name

    #def get_price(self) -> float:
        #return self.price

#import pytest
#from praktikum.bun import Bun


#class TestBun:
    #def test_bun_creation(self):
        #bun = Bun("Wheat Bun", 100.0)
       # assert bun.name == "Wheat Bun"
       # assert bun.price == 100.0

    #def test_get_name(self):
        #bun = Bun("Rye Bun", 120.0)
        #assert bun.get_name() == "Rye Bun"

    #def test_get_price(self):
        #bun = Bun("Sesame Bun", 80.0)
        #assert bun.get_price() == 80.0


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
