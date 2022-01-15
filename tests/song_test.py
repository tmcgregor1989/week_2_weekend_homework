import unittest

from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):

        self.song = Song("Purple Rain", "Prince")

    def test_song_has_song_title(self):
        self.assertEqual("Purple Rain", self.song.song_title)