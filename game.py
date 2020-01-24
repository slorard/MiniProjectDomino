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



    
   
def music():
    playsound('./music/Bachata.mp3')
thread1 = threading.Thread(target=start)
thread2 = threading.Thread(target=music)


thread1.start()
thread2.start()