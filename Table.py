import random 
import os

dominoes_tokens = []
class table:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tableDomino = []
        self.join = None
        self.place = None
        self.tokensOfPlayer = None

    def appendTokens(self, tokensOfPlayer, place):
        self.place = place
        self.tokensOfPlayer = tokensOfPlayer
        if place == "1" or place == "2":
            if place == "2":
                self.tableDomino.append(tokensOfPlayer)
            else:
                self.tableDomino.insert(0, tokensOfPlayer)
            os.system("clear")
            return self.tableDomino

    def showDominos(self):
        for i in self.tableDomino:
            self.join = " ".join(self.tableDomino)
        return(self.join)

def generateTokens():
    f = 0
    for a in range(0,7):
        for i in range(f,7):
            faces = str(a) + '-' + str(i)
            dominoes_tokens.append(faces)
        f+=1

generateTokens()
random.shuffle(dominoes_tokens)
table = table(dominoes_tokens)
