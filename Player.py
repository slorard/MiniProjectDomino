
from Table import table, dominoes_tokens
import os


class Player:

    def __init__(self,name):
        self.name = name
        self.hand =[]#  lterally the player's hand :B

    def TakeHand(self, tokens, tokens_per_player = 7):# with this method the player can take tokens for his/her hand
        for a in range(tokens_per_player):
            self.hand.append(tokens.pop())
        return tokens

        
    def show_hand(self):
        numtoken = []
        for i in range(len(self.hand)):
            numtoken.append(f"   {str(i+1)}  ")
        print("|"," | ".join(self.hand),"|")
        print("".join(numtoken))

    def drop_tokens(self):
        z = input("choose one to put in the table or write pass if you don't have any token to play: ")
        try:
            z = int(z)
            for a in range(8):
                if z == a:
                    place = int(input('Choose what place you want to put: '))
                    rotate = input('Do you want rotate?, Y or N : ')

                    if place == 1 or place ==  2:#in case you put an invalid position
                        table.appendTokens(self.hand.pop(a-1), place, rotate)
                
                    if table.place == 1 and table.join[0] != table.tokensOfPlayer[-1]:# you can't place a token in the position 1 if that token doesn't go there
                        self.hand.insert(a-1, table.tableDomino.pop(0))
                        table.showDominos()
                        print(f"that token does not go there\n{self.name} these are your token")
                        self.show_hand()
                        self.drop_tokens()

                    if table.place == 2 and table.join[-1] != table.tokensOfPlayer[0]:#you can't place a token in the position 2 if that token doesn't go there
                        self.hand.insert(a-1, table.tableDomino.pop(-1))
                        table.showDominos()
                        print(f"that token does not go there\n{self.name} these are your token")
                        self.show_hand()
                        self.drop_tokens()

                elif z > len(self.hand):
                    if len(self.hand) <= 0:
                        print('{} win with...'.format(self.name))
                        
                        break
                    else:
                        table.showDominos()
                        print("You don't have enough tokens to put, choose another: ")
                        self.show_hand()
                        self.drop_tokens()
                        break
        except:
            if len(table.tableDomino) > 1:
                table.showDominos()
                self.show_hand()
                self.drop_tokens()
print(dominoes_tokens)