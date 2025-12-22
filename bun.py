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


class TestBun:
    def test_bun_creation(self):
        bun = Bun("Wheat Bun", 100.0)
        assert bun.name == "Wheat Bun"
        assert bun.price == 100.0

    def test_get_name(self):
        bun = Bun("Rye Bun", 120.0)
        assert bun.get_name() == "Rye Bun"

    def test_get_price(self):
        bun = Bun("Sesame Bun", 80.0)
        assert bun.get_price() == 80.0
