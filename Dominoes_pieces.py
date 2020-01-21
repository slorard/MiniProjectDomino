#From this library I use the method random to shuffle the tokens
import random
class Pieces():
    def __init__(self,Face1,Face2):
        self.Face1 = Face1 #Left side of token 
        self.Face2 = Face2 #Right side of the tokens
        self.DominosFaces = str(Face1) + '-' + str(Face2) # complete  token

dominoes_tokens = []#Put all tokens of the game here

f = 0
for a in range(7):
    for i in range(f,7):
        l = Pieces(a,i)
        dominoes_tokens.append(l.DominosFaces)
    f +=1

random.shuffle(dominoes_tokens)
            
            