import random 
import os
import time
dominoesTokens = []

file = open("./iniciodomino.txt", "r")
print(file.read())
time.sleep(1.5)
os.system("clear")

class Table:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tableDomino = []
        self.join = None
        self.tokensOfPlayer = None

    def appendTokens(self, tokensOfPlayer, place):
        self.tokensOfPlayer = tokensOfPlayer
        if place.upper() == "L" or place.upper() == "R":
            if place.upper() == "R":
                self.tableDomino.append(tokensOfPlayer)
            else:
                self.tableDomino.insert(0, tokensOfPlayer)
            os.system("clear")
            return self.tableDomino

    def showDominos(self):
        for _ in self.tableDomino:
            self.join = " ".join(self.tableDomino)
        return(self.join)

def generateTokens():
    for a in range(0,7):
        for i in range(a,7):
            faces = str(a) + '-' + str(i)
            dominoesTokens.append(faces)

generateTokens()
random.shuffle(dominoesTokens)
Table = Table(dominoesTokens)
