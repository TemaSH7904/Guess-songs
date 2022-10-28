import unittest
from unittest import result
import main

class TestGame(unittest.TestCase):
    def test_menu(self):
        result = main.menu()
        self.assertEqual(result, "0")

    def test_start_game(self):
         result = main.start_game()
         self.assertEqual(result, "Good")
    def test_get_random_song(self):
          result = main.get_random_song()
          self.assertEqual(result, "0 song -- CC CATCh - Cause You Are Young.mp3")

    def test_get_songs(self):
         result = main.get_songs()
         self.assertEqual(result, ["1 song Basta-SolnceNeVidno.mp3"])

    def test_get_variants(self):
         result = main.get_var()
         self.assertEqual(result, "2 song Basta-yrban.mp3")

