from Player import Player
from Table import Table, dominoesTokens, generateTokens
from playsound import playsound
import os, random, time, threading

playerList = []#list the players that gonna play
a = True

while True:
    inputNumPlayer = input('How many wants to play? ')#Introduce How many players gonna play
    try:
        if int(inputNumPlayer) > 1 and int(inputNumPlayer) <= 4:#Verify if you write a number between 2-4
            os.system('clear')
            break
        else:
            os.system("clear")
            print("That number isn't valid, please write one between 2-4")#If you write a number isn't valid
    except:
        os.system("clear")#If you write something that is not a number
        print('Write a real number')

def createPlayer():
    for i in range(int(inputNumPlayer)): #Append in the playerList the players
        playerList.append(Player(input("Write name of player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoesTokens)
    os.system("clear")
    print("Mixing...")
    playsound('./music/baraje2.mp3')
    os.system("clear")

def playerTurnFirst():#Search for the token that have a the highest value inside the all players hands
    playerTurn = 0
    maxToken = 0
    numTokenPlayer = 7
    for player in range(int(inputNumPlayer)):#range each player
        for i in range(numTokenPlayer):#range each player hand token
            test = eval(playerList[player].hand[i-1].replace("-","+"))
            if test > maxToken:#Eval if a token is highest than others
                playerTurn = player
                maxToken = test
    return playerTurn

def countPoints():#eval the points when the player won
    join = " ".join(Table.tableDomino).replace("-", "+").replace(" ", "+")#sum the all points the table
    tablePoints = abs(int(eval(join)))
    allDominoPoints = 168 #value of all tokens
    if dominoesTokens != []:
        boxDominoPoint = abs(int(eval(" ".join(dominoesTokens).replace("-","+").replace(" ", "+"))))
        tablePoints += boxDominoPoint
    return abs(int(allDominoPoints - tablePoints))

def block():
        countTokenDoesntGo = 0
        lenHands = 0
        tokensGoOfDominoesToken = 0
        Table.showDominos()

        #count the tokens inside the domino box you can't play
        if Table.tableDomino != []:
            if dominoesTokens != []:
                for tokens in dominoesTokens:
                    if Table.join[0] != tokens[0] and Table.join[0] != tokens[-1] and Table.join[-1] != tokens[0] and Table.join[-1] != tokens[-1]:
                        tokensGoOfDominoesToken += 1
                    else:
                        break
            #count the tokens the players they can't play
            if tokensGoOfDominoesToken == len(dominoesTokens) or dominoesTokens == []:
                for player in playerList:
                    lenHands += len(player.hand)
                    for i in range(len(player.hand)):#count the tokens don't go 
                        if player.hand[i][0] != Table.join[0] and player.hand[i][0] != Table.join[-1] and player.hand[i][2] != Table.join[0] and player.hand[i][2] != Table.join[-1]:
                            countTokenDoesntGo += 1
                        else:
                            break#if one token goes then break the loop
                #compare if the all tokens the players can't play
                if countTokenDoesntGo == lenHands:
                    return True

def askAgainPlay(player):#Ask if you want to play again
    playAgain = input("Do you want to keep playing?, Y/N ")
    if playAgain.upper() == "Y":
        if player.points >= 200:#if one of the player reach to the 200 points asks if you want to play again and reboot the game
            os.system("python -B game.py") or os.system("python3 game.py")
        else:
            os.system("clear")
    elif playAgain.upper() == "N":
        os.system("clear")#close the game
        print('Thanks for play! :D')
        time.sleep(1.5)
        os._exit(1)
    else:
        os.system("clear")
        print("Write Y or N")
        askAgainPlay(player)

def againPlay(player): #Methd when you win a round delete the tokens what still have the others players and count the points and create the tokens again 
    os.system('clear')
    if Table.tableDomino != []:
        player.points += countPoints()
        if block():#Shows this message if you block, that means the others players can not play tokens or can take for lay
            print(f"{player.name} has block with {countPoints()} points, now has {player.points} points.")
        else: #if the list of the tokens of one player is empty that means he/she won
            print(f"{player.name} has won with {countPoints()} points, now has {player.points} points.")

    askAgainPlay(player)

    if dominoesTokens != []:#clear the box domino
        for i in range(len(dominoesTokens)):
            dominoesTokens.pop()

    Table.join = None
    Table.tableDomino = []

    generateTokens()
    random.shuffle(dominoesTokens)


    for players in playerList:
        players.hand = []
        players.TakeHand(dominoesTokens)


def start():
    global turns
    if playerList[turns-1].hand == [] or block() or int(playerList[turns-1].points) >= 200:# If palyer wins and play again return the player who won  or verify if a player have 200 points
        againPlay(playerList[turns-1])
        turns -= 1

    #shows the players hand
    playerList[turns].showHand()
    playerList[turns].dropTokens()#put a token on the table :V
    playsound('./music/golpe.mp3')

    #change the turns
    if turns+1 < int(inputNumPlayer):
        turns += 1
    else:
        turns = 0

    start()

def music():
    playsound('./music/Bachata.mp3')

createPlayer()
turns = playerTurnFirst()#The player who play first

thread1 = threading.Thread(target= start)
thread2 = threading.Thread(target= music)

thread1.start()
thread2.start()
