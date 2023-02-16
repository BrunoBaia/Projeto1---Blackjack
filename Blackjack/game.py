from models import *
from time import sleep
from random import randint


def opponent_turn(opponent: Blackjack) -> Blackjack:
    print("\nVez do oponente!")
    for value in range(2):
        opponent.distribute_card()
    opponent.initial_point(manual=False)
    while True:
        if opponent.point < 15:
            opponent.distribute_card()
            opponent.calculate_point(manual=False)
            print("O oponente comprou uma carta...")
            sleep(2)
            if opponent.point > 21:
                print(f"O oponente estorou com {opponent.point} pontos")
                opponent.point = 0
                sleep(2)
                return opponent
        else:
            print(f"O oponente finalizou com {len(opponent.hand)} cartas na mao")
            sleep(2)
            return opponent


def player_turn(player: Blackjack) -> Blackjack:
    print("\nSua vez!")
    for value in range(2):
        player.distribute_card()
    player.show_hand()
    player.initial_point()
    print(f"Total de pontos: {player.point}")
    sleep(2)
    while True:
        pick = input("Digite 'S' para pegar uma carta 'N' para manter mao: ")
        if pick.upper() == "S":
            player.distribute_card()
            player.show_hand()
            player.calculate_point()
            if player.point > 21:
                print(f"A pontuacao estorou em {player.point}")
                player.point = 0
                sleep(2)
                return player
            print(f"Total de pontos: {player.point}")
            sleep(2)
        else:
            print(f"Voce finalizou com {len(player.hand)} cartas na mao")
            sleep(2)
            return player


def game(coin, counter):
    counter += 1
    player = Blackjack()
    opponent = Blackjack()
    turn = randint(0, 1)
    if turn:
        player = player_turn(player)
        opponent = opponent_turn(opponent)
    else:
        opponent = opponent_turn(opponent)
        player = player_turn(player)
    coin = player.compare_results(opponent, coin)
    continua = input("Digite 'S' para jogar novamente 'N' para parar: ")
    if continua.upper() == "S" and coin > 0:
        return game(coin, counter)
    else:
        print(f"\nJogo finalizado; \nNumero de partida(s): {counter}; \nMoedas iniciais: 5; \nMoedas finais: {coin}.")


def main():
    coin = 5
    counter = 0
    game(coin, counter)


if __name__ == "__main__":
    main()
