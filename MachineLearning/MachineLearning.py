import numpy as np

class tictactoe:
    plansza = np.zeros((3,3), dtype=int)
    znak = [' ', 'X', 'O']
    x = 0
    y = 0

    def inputXY_X(self,gracz):
        x = input("Podaj x: ")
        y = input("Podaj y: ")
        self.plansza[int(x),int(y)] = gracz
        self.printMap(self)

    def printMap(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.znak[self.plansza[i,j]],end=' ')
            print("\n")



gra = tictactoe
gra.printMap(gra)
gra.inputXY_X(gra,1)
gra.inputXY_X(gra,2)

        
    
