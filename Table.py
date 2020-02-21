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
        self.tokens = tokens#the tokens what the table gonna receive later
        self.tableDomino = []#the tokens what players put 
        self.join = None

    def appendTokens(self, tokensOfPlayer, place):
        if place.upper() == "L" or place.upper() == "R":
            if place.upper() == "R":
                self.tableDomino.append(tokensOfPlayer)
            else:
                self.tableDomino.insert(0, tokensOfPlayer)
            os.system("clear")
            return self.tableDomino

    def showDominos(self):#convert in a string the list of the tokens what players put on the table to delete the parenthesis
        self.join = " ".join(self.tableDomino)
        return self.join

def generateTokens():#create all the dominoes tokens that contains two faces of values
    for faceL in range(0,7):
        for faceR in range(faceL,7):
            faces = str(faceL) + '-' + str(faceR)
            dominoesTokens.append(faces)

generateTokens()
random.shuffle(dominoesTokens)
Table = Table(dominoesTokens)
