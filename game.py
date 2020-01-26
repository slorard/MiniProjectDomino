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



def gameLoop(player):
    if player.points == 200:
        return False
    else:
        return True

turnPlayer = False
def win(player):
    if player.hand == []:
        os.system('clear')
        player.points += table.countPoints()
        print(f"El jugador {player.name} ha ganado con {table.countPoints()} puntos")
        for i in range(len(table.tableDomino)):
            dominoes_tokens.append(table.tableDomino.pop())
        for playerHands in playerList:
            for i in range(len(playerHands.hand)):
                if playerHands.hand != []:
                    dominoes_tokens.append(playerHands.hand[i])
            playerHands.hand = []
            playerHands.TakeHand(dominoes_tokens)





def start():
    os.system('clear')
    turns = maxToken.index(max(maxToken))
    table.tableDomino = []
    while gameLoop(playerList[turns]):
        while True:
            print(turnPlayer)
            win(playerList[turns-1])
            print(playerList[turns].points)
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
