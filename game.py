from Player import Player
from Table import table, dominoes_tokens
import os

playerList = []
inputNumPlayer = int(input('How many wants to play? '))
def createPlayer():
    for i in range (inputNumPlayer): #Create the players in a list
        playerList.append(Player(input("Player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoes_tokens)


listHandPlayer = []
listMaxTokenPlayer = []
listMaxTokenAllPlayers = []
maxToken = []

def playerTurn():
    numTokenPlayer = 7
    for i in range(inputNumPlayer):
        listMaxTokenPlayer = []
        listHandPlayer = []
        for tokenPlayer in range(numTokenPlayer):
            listHandPlayer.append("".join(playerList[i].hand[tokenPlayer]))
            listMaxTokenPlayer.append(eval("".join(playerList[i].hand[tokenPlayer]).replace("-","+")))

        listMaxTokenAllPlayers.append(listHandPlayer[listMaxTokenPlayer.index(max(listMaxTokenPlayer))])

    for compareMaxTokenAllPlayer in listMaxTokenAllPlayers:
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
        if a+1 <= inputNumPlayer:
            a += 1
        table.showDominos()

createPlayer()
playerTurn()
start()
