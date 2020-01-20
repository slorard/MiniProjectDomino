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
        print(self.hand)
        
    def drop_tokens(self):
        z = input("choose one to put in the table or write pass if you fon't have any token to play.")
        if z == 'pass':
            table.appendTokens('', None, None)
        try:
            z = int(z)
            for a in range(8):
                if z == a:
                    table.appendTokens(self.hand.pop(a-1), int(input('Choose what place you want to put')), input('Do you want rotate?') )
                elif z > len(self.hand):
                    if self.hand <= 0:
                        print('{} win with...'.format(self.name))
                        break
                    else:
                        table.showDominos()
                        print("You don't have enough tokens to put, choose another.")
                        self.show_hand()
                        self.drop_tokens()
                        break


        except: 
            print('None')
    
