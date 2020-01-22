from random import shuffle
import os

dominoes_tokens = []
class table:
    def __init__(self, tokens):
        self.tokens = tokens
        self.points = 0
        self.tableDomino = []
        self.join = None
        self.place = None
        self.tokensOfPlayer = None

    def appendTokens(self, tokensOfPlayer, place, reverse):
        self.place = place
        self.tokensOfPlayer = tokensOfPlayer
        if place == 1:
            if reverse == "Y":
                self.tableDomino.insert(0, tokensOfPlayer[::-1])
                os.system("clear")
                return self.tableDomino
            else:
                self.tableDomino.insert(0, tokensOfPlayer)
                os.system("clear")
                return self.tableDomino

        elif place == 2:
            if reverse == "Y":
                self.tableDomino.append(tokensOfPlayer[::-1])
                os.system("clear")
                return self.tableDomino
            else:
                self.tableDomino.append(tokensOfPlayer)
                os.system("clear")
                return self.tableDomino

    def showDominos(self):
        for i in self.tableDomino:
            self.join = " ".join(self.tableDomino)
        print(self.join)

    def countPoints(self):
        self.join = self.join.replace("-", "+").replace(" ", "+")
        totalPoint = eval(self.join)
        print(totalPoint)
        
def generate():
    f = 0
    for a in range(0,7):
        for i in range(f,7):
            faces = str(a) + '-' + str(i)
            dominoes_tokens.append(faces)
        f+=1

generate()
random.shuffle(dominoes_tokens)
table = table(dominoes_tokens)