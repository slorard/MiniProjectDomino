from Dominoes_pieces import dominoes_tokens
from Table import table
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
            if z-1 > len(self.hand):
                table.showDominos()
                print("you don't have that token, choose a correct token")
                self.show_hand()
                self.drop_tokens()

            place = int(input('Choose what place you want to put: '))
            rotate = input('Do you want rotate?, Y or N : ')

            if place == 1 or place ==  2:#in case you put an invalid position
                table.appendTokens(self.hand.pop(z-1), place, rotate)
                print(table.join[0])
                print(table.tokensOfPlayer[-1])
            else:
                table.showDominos()
                print("wrong place, choose a place that is correct")
                self.show_hand()
                self.drop_tokens()
        
            if table.place == 1 and table.join[0] != table.tokensOfPlayer[-1] or table.place == 2 and table.join[-1] != table.tokensOfPlayer[0]:# you can't place a token in the position 1 if that token doesn't go there
                if place == 2:
                    self.hand.insert(z-1, table.tableDomino.pop(-1))
                else:
                    self.hand.insert(z-1, table.tableDomino.pop(0))
                table.showDominos()
                print(f"that token does not go there\n{self.name} these are your token")
                self.show_hand()
                self.drop_tokens()

            # if z > len(self.hand):
            #     if len(self.hand) <= 0:
            #         print('{} win with...'.format(self.name))
            #         break
        except:
            print("None")

    
   