from Player import Player
from Table import table, dominoes_tokens
import os

playerList = []
inputNumPlayer = int(input('How many wants to play? '))
def createPlayer():
    for i in range (inputNumPlayer): #Create the players in a list
        playerList.append(Player(input("Player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoes_tokens)


listSumTokenPlayer = []
listMaxAllPlayersToken = []
maxToken = []

def playerTurn():
    numTokenPlayer = 7
    for i in range(inputNumPlayer):#range each player
        listSumTokenPlayer = []

        for playerToken in range(numTokenPlayer):#range each player hand token
            listSumTokenPlayer.append(eval("".join(playerList[i].hand[playerToken]).replace("-","+")))

        listMaxAllPlayersToken.append(playerList[i].hand[listSumTokenPlayer.index(max(listSumTokenPlayer))])

    for compareMaxTokenAllPlayer in listMaxAllPlayersToken:
        maxToken.append(eval("".join(compareMaxTokenAllPlayer).replace("-","+")))

os.system('clear')
def start():
    a = maxToken.index(max(maxToken))
    for i in range(inputNumPlayer*7):
        if a == inputNumPlayer:
            a = 0
        print("it's the turn of: " + playerList[a].name)
        playerList[a].show_hand()
        playerList[a].drop_tokens()
        table.showDominos()
        if a+1 <= inputNumPlayer:
            a += 1

createPlayer()
playerTurn()
start()
