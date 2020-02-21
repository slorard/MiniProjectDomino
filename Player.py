from Table import Table, dominoesTokens
import os,time

class Player:
    def __init__(self,name):
        self.name = name#name of the player
        self.hand =[]#the list of tokens of the players
        self.points = 0

    def TakeHand(self, tokens):# with this method the player can take tokens for his/her hand
        tokensPerPlayer = 7
        for _ in range(tokensPerPlayer):
            self.hand.append(tokens.pop())
        return tokens

    def showHand(self): #Shows the list that contains the tokens of the players
        numToken = []
        for i in range(len(self.hand)):
            numToken.append(f"   {str(i+1)}  ")

        if Table.tableDomino != []:
            print(Table.showDominos())

        print(f"It's the turns of: {self.name}.")
        print("|"," | ".join(self.hand),"|")
        print("".join(numToken))#Shows the number of each token 

    def maxToken(self): #Search the value of the highest token and return the player hand that contains the max token 
        maxTokeHand = []
        for i in self.hand:
            maxTokeHand.append(eval(i.replace("-","+")))
        return self.hand[maxTokeHand.index(max(maxTokeHand))]

    def tokensYouCantPlay(self): #Verify if there's a token you can't put in the table it other case it means you have tokens to play
        tokensYouCantPlay = 0
        if Table.tableDomino != []:
            for hand in self.hand:
                if hand[0] != Table.join[0] and hand[0] != Table.join[-1] and hand[2] != Table.join[0] and hand[2] != Table.join[-1]:
                    tokensYouCantPlay += 1
                else:
                    break
        return tokensYouCantPlay

    def inputToken(self):#The entrace of the answers
        if Table.tableDomino == []:
            print(f"You have to play {self.maxToken()},because it is your highest value token.")
        if dominoesTokens == []:
            inputPlayerToken = input("Choose one to put in the table or write 'pass' if you don't have any token to play or write exit to close the game: ")
            return inputPlayerToken
        else:
            inputPlayerToken = input("Choose one to put in the table or 'take' if you don't have any token to play or write exit to close the game: ")
            return inputPlayerToken

    def take(self,inputPlayerToken):# To take tokens of the rest in the dominoes box
        if dominoesTokens == []: #verify is the box of dominoes is empty, is this is true you can't take tokens from the box
            os.system("clear")
            print(f"{self.name} There is no token on the table to take.")
            self.showHand()
            self.dropTokens()

        if self.tokensYouCantPlay() == len(self.hand):
            if dominoesTokens != []:
                Input = input('Want to take One token from the rest?, Y/N ')
                if Input.upper() == 'Y':#Take a token if you write "Y"
                    os.system("clear")
                    self.hand.append(dominoesTokens.pop())
                    self.showHand()
                    self.dropTokens()
                else:
                    os.system("clear")
                    if Input.upper() != "N":
                        print("Write Y or N.")
                    self.showHand()
                    self.dropTokens()
        else:
            os.system("clear")#if you have tokens to play you can't take
            print("You can't take, because you have tokens to play.")
            self.showHand()
            self.dropTokens()

    def playerPass(self,inputPlayerToken):#Change the player if write "pass"
        if self.tokensYouCantPlay() == len(self.hand) and dominoesTokens == []: #change if the player can pass
            os.system("clear")
            Player(self.name)
        else:
            if self.tokensYouCantPlay() != len(self.hand): # Verify if you have tokens to play, that means you can't pass
                os.system("clear")
                print("You have token to play, you can't pass.")
                self.showHand()
                self.dropTokens()
            else:
                os.system("clear")#if the dominoes box is not empty you can take, that means you can't pass
                print("You can take token of the table, you can't pass.")
                self.showHand()
                self.dropTokens()

    def close(self): # Method that close the game if you write "exit"
        os.system("clear")
        print("Thanks for play! :D")
        os._exit(1)

    def playMaxTokenValidation(self,inputPlayerToken): #Validate if you play the max token in the start of the game 
        if Table.tableDomino == [] and self.maxToken() != self.hand[int(inputPlayerToken)-1]:
            os.system("clear")
            print(f"You have to play your highest value token, you have to play {self.maxToken()}")
            os.remove("__pycache__")
            self.showHand()
            self.dropTokens()

    def rotateToken(self, inputPlayerToken, place):#rotate the token to the if this token is the correct but needs to be fit in 
        if place.upper() == "L" and Table.join[0] == self.hand[int(inputPlayerToken)-1][0] or place.upper() == "R" and Table.join[-1] == self.hand[int(inputPlayerToken)-1][-1]:
            Table.appendTokens(self.hand.pop(int(inputPlayerToken)-1)[::-1], place.upper())
        else:
            os.system("clear")#If one token doesn't go on the place the player put the token 
            print(f"That token does not go there.")
            self.showHand()
            self.dropTokens()

    def dropTokens(self):#Sends a token to the table 
        inputPlayerToken = self.inputToken()
        if inputPlayerToken.lower() == 'exit':#Verify if in the input you write "exit: to send you to the method "Close"
            self.close()
        if inputPlayerToken.lower() == 'take':#Verify if in the input you write "exit: to send you to the method take
            self.take(inputPlayerToken)
        if inputPlayerToken.lower() == "pass":#Verify if in the input you write "exit: to send you to the method "playerPass"
            self.playerPass(inputPlayerToken)
        try:
            if int(inputPlayerToken) <= len(self.hand) and int(inputPlayerToken) >= 1:
                self.playMaxTokenValidation(int(inputPlayerToken))#Verify if the token played in the first turn is the hightest
                if Table.tableDomino != []:
                    place = input('Choose what place you want to put, write L(left) or R(right): ')
                    # you can't place a token in the position 1 if that token doesn't go there
                    if place.upper() == "L" and Table.join[0] != self.hand[int(inputPlayerToken)-1][-1] or place.upper() == "R" and Table.join[-1] != self.hand[int(inputPlayerToken)-1][0]:
                        self.rotateToken(inputPlayerToken, place)#rotate the token to fit in the table 
                    else:
                        if place.upper() == "L" or place.upper() == "R":
                            Table.appendTokens(self.hand.pop(int(inputPlayerToken)-1), place.upper())
                        else:
                            os.system("clear")#in case you put a token doesn't go in the right place
                            print("Wrong place, choose a place that is correct.")
                            self.showHand()
                            self.dropTokens()
                else:
                    Table.appendTokens(self.hand.pop(int(inputPlayerToken)-1), "L")#Put the first movr in the table without asking 
            else:
                os.system("clear")#Verify if you write a token you don't have
                print("You don't have that token, choose a correct token.")
                self.showHand()
                self.dropTokens()
        except:#Catch the errors in the input
            if inputPlayerToken != "pass" and inputPlayerToken != "take" and inputPlayerToken != "exit":
                os.system("clear")
                print("Wrong token, choose a token that is correct.")
                self.showHand()
                self.dropTokens()