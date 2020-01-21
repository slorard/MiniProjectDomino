from Dominoes_pieces import dominoes_tokens
from Player import Player
from Table import table

def start():
    jugadores = []

    for i in range (1,5):
        jugadores.append(input('Player ' + str(i) + ': '))

    jugador1 = Player(jugadores[0])
    jugador2 = Player(jugadores[1])
    jugador3 = Player(jugadores[2])
    jugador4 = Player(jugadores[3])

    jugador1.TakeHand(dominoes_tokens)
    jugador2.TakeHand(dominoes_tokens)
    jugador3.TakeHand(dominoes_tokens)
    jugador4.TakeHand(dominoes_tokens)

    while True:
        print(jugadores[0])
        jugador1.show_hand()
        jugador1.drop_tokens()
        table.showDominos()

        print(jugadores[1])
        jugador2.show_hand()
        jugador2.drop_tokens()
        table.showDominos()

        print(jugadores[2])
        jugador3.show_hand()
        jugador3.drop_tokens()
        table.showDominos()

        print(jugadores[3])
        jugador4.show_hand()
        jugador4.drop_tokens()
        table.showDominos()

start()
