from Player import Player
from Table import table, dominoes_tokens
import os
import random

playerList = []
inputNumPlayer = int(input('How many wants to play? '))
def createPlayer():
    for i in range (inputNumPlayer): #Create the players in a list
        playerList.append(Player(input("Player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoes_tokens)

listSumTokenPlayer = []
listMaxAllPlayersToken = []
maxToken = []
def playerTurnFirst():
    numTokenPlayer = 7
    for i in range(inputNumPlayer):#range each player
        listSumTokenPlayer = []
        for playerToken in range(numTokenPlayer):#range each player hand token
            listSumTokenPlayer.append(eval("".join(playerList[i].hand[playerToken]).replace("-","+")))
        listMaxAllPlayersToken.append(playerList[i].hand[listSumTokenPlayer.index(max(listSumTokenPlayer))])
    for compareMaxTokenAllPlayer in listMaxAllPlayersToken:
        maxToken.append(eval("".join(compareMaxTokenAllPlayer).replace("-","+")))

def turn():
    turns = maxToken.index(max(maxToken))
    return turns

def countPoints(self):
    join = " ".join(table.tableDomino).replace("-", "+").replace(" ", "+")
    totalPoint = (abs(int(eval(join))) + abs(int(eval(" ".join(dominoes_tokens).replace("-","+").replace(" ", "+")))))
    return int(168 - totalPoint)

def gameLoop(player):
    if player.points >= 200:
        return False
    else:
        return True

def win(player):
    if player.hand == []:
        os.system('clear')
        player.points += table.countPoints()
        print(f"{player.name} has won with {table.countPoints()} points, now has {player.points} points")
        for tokenTable in table.tableDomino:
            dominoes_tokens.append(tokenTable)
        for playerHands in playerList:
            for i in range(len(playerHands.hand)):
                if playerHands.hand != []:
                    dominoes_tokens.append(playerHands.hand[i])
            playerHands.hand = []
            random.shuffle(dominoes_tokens)
            playerHands.TakeHand(dominoes_tokens)
            table.join = None
            table.tableDomino = []

def start():
    turns = turn()
    while gameLoop(playerList[turns]):
        while True:
            if playerList[turns-1].hand == []:
                win(playerList[turns-1])
                turns -= 1

            win(playerList[turns-1])
            print(f"points of player{playerList[turns].name}: {playerList[turns].points}")
            print("it's the turns of: " + playerList[turns].name)
            playerList[turns].show_hand()
            playerList[turns].drop_tokens()
            print(table.showDominos())
            if turns+1 < inputNumPlayer:
                turns += 1
            else:
                turns = 0

createPlayer()
playerTurnFirst()
start()
