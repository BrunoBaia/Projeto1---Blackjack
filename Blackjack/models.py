from typing import List
from random import shuffle


class Deck:

    def __init__(self) -> None:
        self.__deck: List[tuple] = self._create_deck()

    @property
    def deck(self) -> List[tuple]:
        return self.__deck

    @staticmethod
    def _create_deck() -> List[tuple]:
        card_value: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split(" ")
        card_suit: List[str] = "♧ ♡ ♤ ♢".split(" ")
        deck: List[tuple] = [(value, suit) for value in card_value for suit in card_suit]
        shuffle(deck)
        return deck


class Blackjack(Deck):

    def __init__(self) -> None:
        super().__init__()
        self.hand: list = []
        self.point: int = 0

    def distribute_card(self) -> None:
        self.hand.append(self.deck.pop(0))

    def show_hand(self) -> None:
        print("Suas cartas sao:")
        for card in self.hand:
            print(*card)

    def initial_point(self) -> None:
        for card in self.hand:
            self.point += self._convert_to_digit(card[0])

    def calculate_point(self) -> None:
        self.point += self._convert_to_digit(self.hand[-1][0])

    def _convert_to_digit(self, value: str) -> int:
        if value.isdigit():
            return int(value)
        elif value == "A":
            return self._convert_ace()
        return 10

    def _convert_ace(self) -> int:
        answer: str = input("Voce deseja que o 'Ás' valha 1 ou 11? ")
        if answer == "1":
            return 1
        elif answer == "11":
            return 11
        print("Valor invalido, deve ser 1 ou 11")
        return self._convert_ace()
