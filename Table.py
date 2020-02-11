import os, time, random
dominoesTokens = []

file = open("./iniciodomino.txt", "r")
presentation = open("./presentation.txt", encoding= "utf8")
print(file.read())
time.sleep(1.5)
os.system("clear")
print(presentation.read())
time.sleep(1.5)
os.system("clear")

class Table:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tableDomino = []
        self.join = None

    def appendTokens(self, tokensOfPlayer, place):
        if place.upper() == "L" or place.upper() == "R":
            if place.upper() == "R":
                self.tableDomino.append(tokensOfPlayer)
            else:
                self.tableDomino.insert(0, tokensOfPlayer)
            os.system("clear")
            return self.tableDomino

    def showDominos(self):
        self.join = " ".join(self.tableDomino)
        return(self.join)

def generateTokens():
    for faceL in range(0,7):
        for faceR in range(faceL,7):
            faces = str(faceL) + '-' + str(faceR)
            dominoesTokens.append(faces)

generateTokens()
random.shuffle(dominoesTokens)
Table = Table(dominoesTokens)
