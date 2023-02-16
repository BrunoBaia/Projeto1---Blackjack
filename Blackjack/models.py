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
        self.__hand: list = []
        self.__point: int = 0

    @property
    def hand(self) -> list:
        return self.__hand

    @property
    def point(self) -> int:
        return self.__point

    @hand.setter
    def hand(self, new_value: List[tuple]) -> None:
        self.__hand = new_value

    @point.setter
    def point(self, new_value: int) -> None:
        self.__point = new_value

    def distribute_card(self) -> None:
        self.hand.append(self.deck.pop(0))

    def show_hand(self) -> None:
        print("Cartas:")
        for card in self.hand:
            print(*card)

    def initial_point(self, manual: bool = True) -> None:
        for card in self.hand:
            self.point += self._convert_to_digit(card[0], manual)

    def calculate_point(self, manual: bool = True) -> None:
        self.point += self._convert_to_digit(self.hand[-1][0], manual)

    def _convert_to_digit(self, value: str, manual: bool) -> int:
        if value.isdigit():
            return int(value)
        elif value == "A":
            return self._convert_ace(manual)
        return 10

    def _convert_ace(self, manual: bool) -> int:
        if manual:
            answer: str = input("Voce deseja que o 'Ás' valha 1 ou 11? ")
            if answer == "1":
                return 1
            elif answer == "11":
                return 11
            print("Valor invalido, deve ser 1 ou 11")
            return self._convert_ace(manual)
        else:
            if self.point + 11 <= 21:
                return 11
            return 1

    def compare_results(self, opponent, coin: int) -> int:
        if self.point > opponent.point:
            print("\nVoce venceu, parabens!")
            coin += 1
        elif self.point < opponent.point:
            print("\nVoce perdeu")
            coin -= 1
        else:
            print("\nEmpate")
        print("Sua mao ->")
        self.show_hand()
        print(f"Total de pontos: {self.point}")
        print("Mao do oponente ->")
        opponent.show_hand()
        print(f"Total de pontos: {opponent.point}")
        return coin
