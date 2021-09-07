import random
import unittest
from unittest.mock import patch

from main import play_game


class TestHangMan(unittest.TestCase):
    @patch('builtins.input')
    def test_failed_try(self, mock_input):
        mock_input.return_value = random.choice('abcdefghijklmnopqrstuvwxyz')
        test = play_game()
        self.assertIsNone(test)

    @patch('random.choice')
    @patch('builtins.input')
    def test_successful_try(self, mock_input, mock_guess_list):
        mock_input.return_value = 'i'
        mock_guess_list.return_value = 'i'
        test = play_game()
        self.assertIsNone(test)
