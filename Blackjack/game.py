from models import *
from time import sleep


def game(coin):
    player = Blackjack()
    for value in range(2):
        player.distribute_card()
    player.show_hand()
    player.initial_point()
    print(f"Total de pontos: {player.point}")
    sleep(2)
    while True:
        pick = input("\nDigite 'S' para pegar uma carta 'N' para manter mao: ")
        if pick.upper() == "S":
            player.distribute_card()
            player.show_hand()
            player.calculate_point()
            if player.point > 21:
                print(f"Voce perdeu, a pontuacao estorou em {player.point}\n")
                coin -= 1
                sleep(2)
                break
            print(f"Total de pontos: {player.point}")
            sleep(2)
        else:
            break
    continua = input("Digite 'S' para jogar novamente 'N' para parar: ")
    if continua.upper() == "S":
        return game(coin)
    else:
        print(f"Jogo finalizado, voce terminou com {coin} moedas")


def main():
    coin = 10
    game(coin)


if __name__ == "__main__":
    main()
