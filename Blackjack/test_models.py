import unittest

from models import *


class TesteBlackjack(unittest.TestCase):

    def setUp(self):
        self.blackjack = Blackjack()
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_convert_to_digit(self):
        self.assertEqual(self.blackjack._convert_to_digit("K", True), 10)
        self.assertEqual(self.blackjack._convert_to_digit("9", True), 9)

    def test_convert_ace(self):
        self.assertEqual(self.blackjack._convert_ace(manual=False), 11)
        self.blackjack.point = 12
        self.assertEqual(self.blackjack._convert_ace(manual=False), 1)

    def test_compare_results(self):
        opponent = Blackjack()
        self.blackjack.point = 20
        opponent.point = 21
        self.assertEqual(self.blackjack.compare_results(opponent, coin=6), 5)
        self.blackjack.point = 15
        opponent.point = 10
        self.assertEqual(self.blackjack.compare_results(opponent, coin=6), 7)
        self.blackjack.point, opponent.point = 20, 20
        self.assertEqual(self.blackjack.compare_results(opponent, coin=6), 6)


if __name__ == "__main__":
    unittest.main()
