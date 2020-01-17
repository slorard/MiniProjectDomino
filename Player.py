from Dominoes_pieces import dominoes_tokens
import os, subprocess
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
        pass


player = Player('juancito')
player.TakeHand(dominoes_tokens)
player.show_hand()