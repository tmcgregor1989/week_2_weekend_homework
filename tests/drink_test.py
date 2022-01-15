import unittest

from classes.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennents", 3.50)

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.name)