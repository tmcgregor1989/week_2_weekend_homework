import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song = Song("paranoid", "black sabbath")
        self.guest = Guest("John", 50, self.song)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)




    