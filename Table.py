import random 
import os
import time
dominoes_tokens = []

file = open("./iniciodomino.txt", "r")
print(file.read())
time.sleep(2.5)
os.system("clear")


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
        if place == "L" or place == "R":
            if place == "R":
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
