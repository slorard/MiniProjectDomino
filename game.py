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


def win(playerHand):
    # for hand in playerHand:
    if playerHand.hand == []:
        print(f"El jugador {playerHand.name} ha ganado con {table.countPoints()} puntos")
        return False
    else:
        return True



os.system('clear')
def start():
    turns = maxToken.index(max(maxToken))
    while win(playerList[turns-1]):
        print("it's the turn of: " + playerList[turns].name)
        playerList[turns].show_hand()
        playerList[turns].drop_tokens()
        table.showDominos()
        if turns+1 <= inputNumPlayer:
            turns += 1
        if turns+1 > inputNumPlayer:
            turns = 0
createPlayer()
playerTurn()
start()
