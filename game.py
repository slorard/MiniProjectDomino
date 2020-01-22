from Player import Player
from Table import table, dominoes_tokens
import os
from playsound import playsound
import threading

def start():
    jugadores = []
    z = int(input('How many wants to play? '))
    for i in range (1,z+1):
        jugadores.append(input('Player ' + str(i) + ': '))
    if z == 2:
        jugador1 = Player(jugadores[0])
        jugador2 = Player(jugadores[1])
        jugador1.TakeHand(dominoes_tokens)
        jugador2.TakeHand(dominoes_tokens)
    elif z == 3:
        jugador1 = Player(jugadores[0])
        jugador2 = Player(jugadores[1])
        jugador3 = Player(jugadores[2])
        jugador1.TakeHand(dominoes_tokens)
        jugador2.TakeHand(dominoes_tokens)
        jugador3.TakeHand(dominoes_tokens)
    else:
        jugador1 = Player(jugadores[0])
        jugador2 = Player(jugadores[1])
        jugador3 = Player(jugadores[2])
        jugador4 = Player(jugadores[3])
        jugador1.TakeHand(dominoes_tokens)
        jugador2.TakeHand(dominoes_tokens)
        jugador3.TakeHand(dominoes_tokens)
        jugador4.TakeHand(dominoes_tokens)

    os.system("clear")
    while True:
        print("it's the turn of: " + jugadores[0])
        jugador1.show_hand()
        jugador1.drop_tokens()
        table.showDominos()

        print("it's the turn of: " + jugadores[1])
        jugador2.show_hand()
        jugador2.drop_tokens()
        table.showDominos()

        print("it's the turn of: " + jugadores[2])
        jugador3.show_hand()
        jugador3.drop_tokens()
        table.showDominos()

        print("it's the turn of: " + jugadores[3])
        jugador4.show_hand()
        jugador4.drop_tokens()
        table.showDominos()

def music():
    playsound('./music/Bachata.mp3')
thread1 = threading.Thread(target=start)
thread2 = threading.Thread(target=music)


thread1.start()
thread2.start()