from Dominoes_pieces import dominoes_tokens
from Table import table
import os
class Player:
    
    def __init__(self,name):
        self.name = name
        self.hand =[]
    
    def TakeHand(self, tokens, tokens_per_player = 7):
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
            for a in range(7):
                if z == a:
                    table.appendTokens(sel.hand.pop(a-1), input('Choose what place you want to put'), input('Do you want rotate?') )


        except: 
            print('None')