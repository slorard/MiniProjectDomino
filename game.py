from Player import Player
from Table import table, dominoes_tokens
import os
from playsound import playsound
import threading

def start():
    
    playerList = []
    z = int(input('How many wants to play? '))
    
    for i in range (z): #Create the players in a list
        playerList.append(Player(input("Player {}: ".format(i + 1))))
                         
    
    os.system('clear')
    for player in playerList:
        print("it's the turn of: " + player.name)
        player.show_hand()
        player.drop_tokens()
        table.showDominos()



    
    # os.system("clear")
    # while True:
    #     print("it's the turn of: " + jugadores[0])
    #     jugador1.show_hand()
    #     jugador1.drop_tokens()
    #     table.showDominos()

    #     print("it's the turn of: " + jugadores[1])
    #     jugador2.show_hand()
    #     jugador2.drop_tokens()
    #     table.showDominos()

    #     print("it's the turn of: " + jugadores[2])
    #     jugador3.show_hand()
    #     jugador3.drop_tokens()
    #     table.showDominos()

    #     print("it's the turn of: " + jugadores[3])
    #     jugador4.show_hand()
    #     jugador4.drop_tokens()
    #     table.showDominos()

def music():
    playsound('./music/Bachata.mp3')
thread1 = threading.Thread(target=start)
thread2 = threading.Thread(target=music)


thread1.start()
thread2.start()