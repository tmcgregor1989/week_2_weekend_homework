import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink


class TestRoom(unittest.TestCase):

    def setUp(self):

        self.drink_1 = Drink("wine", 4)
        self.drink_2 = Drink("lager", 3)
        self.song_1 = Song("jump", "van halen")
        self.song_2 = Song("song 2", "blur")
        self.song_3 = Song("DISCO", "sister sledge")
        self.song_4 = Song("Shout", "Lulu")
        self.guest_1 = Guest("Eddie", 50, self.song_1)
        self.guest_2 = Guest("Gina", 60, self.song_2)
        self.guest_3 = Guest("Rocko", 50, self.song_3)
        self.guest_4 = Guest("Felix", 100, self.song_1)
        self.room = Room("Rock Room", [self.guest_4], [], 3, 10, 100, [self.drink_1, self.drink_2])

    def test_room_has_name(self):
        self.assertEqual("Rock Room", self.room.name)

    def test_count_guests_in_room(self):
        self.room.count_guests_in_room()
        self.assertEqual(1, len(self.room.guests))

    def test_check_guest_into_room(self):
        self.room.check_guest_into_room(self.guest_1)
        self.assertEqual(2, len(self.room.guests))
 
    def test_check_out_guest_from_room(self):
        self.room.check_guest_into_room(self.guest_1)
        self.room.check_out_guest_from_room(self.guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_check_capacity_cannot_be_exceeded(self):
        self.room.check_guest_into_room(self.guest_1)
        self.room.check_guest_into_room(self.guest_2)
        self.room.check_guest_into_room(self.guest_3)
        self.assertEqual("sorry, that room is full. Go HOME!!!", self.room.check_guest_into_room(self.guest_3))

    def test_check_entry_fee_is_paid(self):
        self.room.pay_entry_fee(self.guest_1)
        self.assertEqual(40, self.guest_1.wallet)
        self.assertEqual(110, self.room.till)

    def test_check_in_and_pay(self):
        self.room.check_guest_into_room_and_pay(self.guest_1)
        self.assertEqual(40, self.guest_1.wallet)
        self.assertEqual(110, self.room.till)
        self.assertEqual(2, len(self.room.guests))

    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.song_1)
        self.assertEqual(1, len(self.room.song_list))

    def test_guest_fave_song_on_list(self):
        self.room.add_song_to_playlist(self.song_4)
        self.room.add_song_to_playlist(self.song_1)
        self.room.add_song_to_playlist(self.song_2)
        self.room.add_song_to_playlist(self.song_3)
        self.room.guest_fave_song_on_list(self.guest_1)
        self.assertEqual("WooHoo", self.room.guest_fave_song_on_list(self.guest_1))

    def test_sell_drink_to_guest(self):
        self.room.sell_drink_to_guest(self.guest_1, self.drink_1)
        self.assertEqual(46, self.guest_1.wallet)
        self.assertEqual(104, self.room.till)