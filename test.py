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

