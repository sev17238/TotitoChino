#############################################################
# Guatemala, mayo del 2020                                  #
# Diego Sevilla 17238                                       #
# Inteligencia artificial                                   #
# Samuel Chavez                                             #
#############################################################
# En este proyecto se emplea el uso de minimax y alpha-beta #
# para la resolucion de un tablero de 6 * 6 del famoso      # 
# juego Dots and Boxes (O totito chino).                    #
#############################################################
# Tablero.py: Clase para el manejo de operaciones con las   #
# matrices que representan al tablero.                      #
#############################################################

class Tablero: #A class for managing different situations and states happening in the game and on the board
    def __init__(self, Mat, dimX, dimY):
        self.Mat = Mat
        self.dimX = dimX
        self.dimY = dimY

    #############################################
    # Inicializando el tablero del juego con X
    # y Y dimensiones.
    def Inicializacion(self): #initiating the game board with X and Y dimensions
        for i in range(0, self.dimY):
            R = []
            for j in range (0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    #R.append(randint(1, 9))  # Assigning a random number from 1 to 9 to the spots in the board as the points
                    R.append(1) # there will be always a point for each good move
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') # printing asterisks as the dots in the board
                else:
                    R.append(' ') # adding extra space for actions in the game
            self.Mat.append(R)

    #############################################
    # Matriz que respresenta al tablero del juego
    def Get_matrix(self): 
        ans = []
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                R.append(self.Mat[i][j])
            ans.append(R)
        return ans

    ###############################################
    # Drawing the board marix as dots and lines
    def Draw_mat(self):
        
        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX):
            print(str(i), end='  ')
        print()

        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX + 1):
            print("___", end='')
        print()
        for j in range(self.dimY):
            if self.dimX > 9 and j < 10:
                print(" ", end='')
            print(str(j) + "| ", end='')
            for z in range(self.dimX):
                print(str(self.Mat[j][z]), end='  ')
            print()
        print("   _________________________\n")

    def Get_currentState(self):
        return Tablero(self.Get_matrix(), self.dimX, self.dimY)

    def action(self, i, j): # Applying the actions made by the human or the computer
        Sum = 0

        if j % 2 == 0 and i % 2 == 1:
            self.Mat[j][i] = '-'
            if j < self.dimY - 1:
                if self.Mat[j+2][i] == '-' and self.Mat[j+1][i+1] == '|' and self.Mat[j+1][i-1] == '|':
                    Sum += self.Mat[j+1][i]
            if j > 0:
                if self.Mat[j-2][i] == '-' and self.Mat[j-1][i+1] == '|' and self.Mat[j-1][i-1] == '|':
                    Sum += self.Mat[j-1][i]

        else:
            self.Mat[j][i] = '|'
            if i < self.dimX - 1:
                if self.Mat[j][i+2] == '|' and self.Mat[j+1][i+1] == '-' and self.Mat[j-1][i+1] == '-':
                    Sum += self.Mat[j][i+1]
            if i > 0:
                if self.Mat[j][i-2] == '|' and self.Mat[j+1][i-1] == '-' and self.Mat[j-1][i-1] == '-':
                    Sum += self.Mat[j][i-1]
        return Sum
