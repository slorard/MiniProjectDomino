
from Table import Table, dominoes_tokens
import os

class Player:
    def __init__(self,name):
        self.name = name
        self.hand =[]
        self.points = 0

    def TakeHand(self, tokens):# with this method the player can take tokens for his/her hand
        tokens_per_player = 7
        for _ in range(tokens_per_player):
            self.hand.append(tokens.pop())
        return tokens

    def show_hand(self):
        numtoken = []
        for i in range(len(self.hand)):
            numtoken.append(f"   {str(i+1)}  ")
        if Table.tableDomino != []:
            print(Table.showDominos())
        print(f"It's the turns of: {self.name}.")
        print("|"," | ".join(self.hand),"|")
        print("".join(numtoken))

    def maxToken(self):
        maxTokeHand = []
        if Table.tableDomino == []:
            for i in self.hand:
                maxTokeHand.append(eval(i.replace("-","+")))
            return self.hand[maxTokeHand.index(max(maxTokeHand))]

    def tokensYouCanPlay(self):
        tokensYouCanPlay = 0
        if Table.tableDomino != []:
            for hand in self.hand:
                if hand[0] != Table.join[0] and hand[0] != Table.join[-1] and hand[2] != Table.join[0] and hand[2] != Table.join[-1]:
                    tokensYouCanPlay += 1
        return tokensYouCanPlay

    def inputToken(self):
        if Table.tableDomino == []:
            print(f"You have to play {self.maxToken()},because it is your highest value token.")
        if dominoes_tokens == []:
            inputPlayerToken = input("Choose one to put in the table or write 'pass' if you don't have any token to play: ")
            return inputPlayerToken
        else:
            inputPlayerToken = input("Choose one to put in the table or 'take' if you don't have any token to play: ")
            return inputPlayerToken

    def take(self,inputPlayerToken):
        if inputPlayerToken.lower() == 'take':
            if dominoes_tokens == [] and inputPlayerToken.lower() == 'take':
                os.system("clear")
                print(f"{self.name} There is no token on the table to take.")
                self.show_hand()
                self.drop_tokens()
            if self.tokensYouCanPlay() == len(self.hand) and inputPlayerToken.lower() == "take":
                if dominoes_tokens != [] and inputPlayerToken.lower() == 'take':
                    Input = input('Want to take One token from the rest?, Y/N ')
                    if Input.upper() == 'Y':
                        os.system("clear")
                        self.hand.append(dominoes_tokens.pop())
                        self.show_hand()
                        self.drop_tokens()
                    else:
                        os.system("clear")
                        if Input.upper() != "N":
                            print("You can't take that token.")
                        self.show_hand()
                        self.drop_tokens()
            elif self.tokensYouCanPlay() != len(self.hand) and inputPlayerToken.lower() == "take":
                os.system("clear")
                print("You can't take, because you have tokens to play.")
                self.show_hand()
                self.drop_tokens()

    def playerPass(self,inputPlayerToken):
        if inputPlayerToken.lower() == "pass":
            if self.tokensYouCanPlay() == len(self.hand) and dominoes_tokens == []:
                os.system("clear")
                Player(self.name)
            else:
                if self.tokensYouCanPlay() != len(self.hand):
                    os.system("clear")
                    print("You have token to play, you can't pass.")
                    self.show_hand()
                    self.drop_tokens()
                else:
                    os.system("clear")
                    print("You can take token of the table, you can't pass.")
                    self.show_hand()
                    self.drop_tokens()

    def playMaxTokenValidation(self,inputPlayerToken):
        if Table.tableDomino == [] and self.maxToken() != self.hand[int(inputPlayerToken)-1]:
                os.system("clear")
                print(f"You have to play your highest value token, you have to play {self.maxToken()}")
                self.show_hand()
                self.drop_tokens()

    def rotateToken(self, inputPlayerToken, place):
        if place.upper() == "L" and Table.join[0] == self.hand[int(inputPlayerToken)-1][0] or place.upper() == "R" and Table.join[-1] == self.hand[int(inputPlayerToken)-1][-1]:
            Table.appendTokens(self.hand.pop(int(inputPlayerToken)-1)[::-1], place.upper())#rotate token
        else:
            os.system("clear")
            print(f"That token does not go there.")
            self.show_hand()
            self.drop_tokens()

    def drop_tokens(self):
        inputPlayerToken = self.inputToken()
        self.take(inputPlayerToken)
        self.playerPass(inputPlayerToken)
        try:
            self.playMaxTokenValidation(inputPlayerToken)
            if int(inputPlayerToken) <= len(self.hand) and int(inputPlayerToken) >= 1:
                if Table.tableDomino != []:
                    place = input('Choose what place you want to put, write L(left) or R(right): ')
                    # you can't place a token in the position 1 if that token doesn't go there
                    if place.upper() == "L" and Table.join[0] != self.hand[int(inputPlayerToken)-1][-1] or place.upper() == "R" and Table.join[-1] != self.hand[int(inputPlayerToken)-1][0]:
                        self.rotateToken(inputPlayerToken, place)
                    else:
                        if place.upper() == "L" or place.upper() == "R":#in case you put an invalid position
                            Table.appendTokens(self.hand.pop(int(inputPlayerToken)-1), place.upper())
                        else:
                            os.system("clear")
                            print("Wrong place, choose a place that is correct.")
                            self.show_hand()
                            self.drop_tokens()
                else:
                    Table.appendTokens(self.hand.pop(int(inputPlayerToken)-1), "L")
            else:
                os.system("clear")
                print("You don't have that token, choose a correct token.")
                self.show_hand()
                self.drop_tokens()
        except:
            if inputPlayerToken.lower() != "pass" and inputPlayerToken.lower() != "take":
                os.system("clear")
                print("Wrong token, choose a token that is correct.")
                self.show_hand()
                self.drop_tokens()