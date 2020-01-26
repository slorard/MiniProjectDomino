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

    def appendTokens(self, tokensOfPlayer, place, reverse):
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
        print(self.join)

    def countPoints(self):
        join = " ".join(self.tableDomino).replace("-", "+").replace(" ", "+")
        totalPoint = (abs(int(eval(join))) + abs(int(eval(" ".join(dominoes_tokens).replace("-","+").replace(" ", "+")))))
        return int(168 - totalPoint)
         
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
