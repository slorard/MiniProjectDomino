from Dominoes_pieces import dominoes_tokens
import os

class table:
    def __init__(self, tokens):
        self.tokens = tokens
        self.points = 0
        self.tableDomino = []
        self.join = None

    def appendTokens(self, tokensOfPlayer, place, reverse):
        if tokensOfPlayer == "pass" and place == None and reverse == None:
            self.tableDomino.append("")
        if place == 1:
            if reverse == "Y" or "y":
                self.tableDomino.insert(0, tokensOfPlayer[::-1])
                os.system("clear")
                return self.tableDomino
            else:
                self.tableDomino.insert(0, tokensOfPlayer)
                os.system("clear")
                return self.tableDomino

        elif place == 2:
            if reverse == "Y" or "y":
                self.tableDomino.append(tokensOfPlayer)
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
        
table = table(dominoes_tokens)