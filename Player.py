
from Table import table, dominoes_tokens
import os


class Player:

    def __init__(self,name):
        self.name = name
        self.hand =[]#  lterally the player's hand :B
        self.points = 0

    def TakeHand(self, tokens, tokens_per_player = 7):# with this method the player can take tokens for his/her hand
        for a in range(tokens_per_player):
            self.hand.append(tokens.pop())
        return tokens

    def show_hand(self):
        numtoken = []
        for i in range(len(self.hand)):
            numtoken.append(f"   {str(i+1)}  ")
        if table.tableDomino != []:
            print(table.showDominos())
        print(f"Points of player {self.points}.")
        print(f"It's the turns of: {self.name}.")
        print("|"," | ".join(self.hand),"|")
        print("".join(numtoken))

    def drop_tokens(self):
        inputPlayerToken = input("Choose one to put in the table or write pass if you don't have any token to play or take: ")

        if dominoes_tokens != [] and inputPlayerToken == 'take':
            Input = input('Want to take One token from the rest?, Y/N ')
            if Input == 'Y':
                os.system("clear")
                self.hand.append(dominoes_tokens.pop())
                self.show_hand()
                self.drop_tokens()
            else:
                os.system("clear")
                self.show_hand()
                self.drop_tokens()
        elif dominoes_tokens == [] and inputPlayerToken == 'take':
            os.system("clear")
            print(f"{self.name} there is no token on the table to take.")
            self.show_hand()
            self.drop_tokens()

        try:
            inputPlayerToken = int(inputPlayerToken)
            if inputPlayerToken > len(self.hand) or inputPlayerToken < 1:
                os.system("clear")
                print("You don't have that token, choose a correct token.")
                self.show_hand()
                self.drop_tokens()

            place = input('Choose what place you want to put, write L(left) or R(right) : ')

            if place == "L" or place == "R":#in case you put an invalid position
                if table.tableDomino != []:
                    if place == "L" and table.join[0] == self.hand[inputPlayerToken-1][0] or place == "R" and table.join[-1] == self.hand[inputPlayerToken-1][-1]:
                        table.appendTokens(self.hand.pop(inputPlayerToken-1)[::-1], place)
                    else:
                        table.appendTokens(self.hand.pop(inputPlayerToken-1), place)
                else:
                    table.appendTokens(self.hand.pop(inputPlayerToken-1), place)
            else:
                os.system("clear")
                print("Wrong place, choose a place that is correct.")
                self.show_hand()
                self.drop_tokens()

            if place == "L" and table.join[0] != table.tokensOfPlayer[-1] or place == "R" and table.join[-1] != table.tokensOfPlayer[0]:# you can't place a token in the position 1 if that token doesn't go there
                    if place == "R":
                        self.hand.insert(inputPlayerToken-1, table.tableDomino.pop(-1))
                    else:
                        self.hand.insert(inputPlayerToken-1, table.tableDomino.pop(0))
                    print(f"That token does not go there\n{self.name} these are your token.")
                    self.show_hand()
                    self.drop_tokens()
        except:
            os.system("clear")
            if inputPlayerToken == "":
                print("Wrong token, choose a token that is correct.")
                self.show_hand()
                self.drop_tokens()

    def takeOneToken(self):
        Input = input('Want to take One token from the rest? ')
        if Input == 'Y':
            self.hand.append(dominoes_tokens.pop())
        else:
            table.showDominos()
            self.show_hand()
            self.drop_tokens()

