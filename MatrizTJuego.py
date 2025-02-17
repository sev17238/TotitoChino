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
# MatrizTJuego.py: Clase para el manejo de operaciones con las   #
# matrices que representan al tablero y sus estados.        #
#############################################################

class MatrizTJuego:
    def __init__(self, Mat, dimX, dimY):
        self.Mat = Mat
        self.dimX = dimX
        self.dimY = dimY

    #############################################
    # Inicializando el tablero del juego con X
    # y Y dimensiones.
    def Inicializacion(self): 
        for i in range(0, self.dimY):
            R = []
            for j in range (0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    #R.append(randint(1, 9))  # Se le asignan numeros aleatorios a las casillas como el puntaje del juego
                    R.append(1) # En este caso siempre habra 1s
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') # Los asteriscos haran el papel de puntos en el juego
                else:
                    R.append(' ') # Espacios para una mejor visualizacion
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

    ###########################################
    # Se retorna el estado actual
    def Get_currentState(self):
        return MatrizTJuego(self.Get_matrix(), self.dimX, self.dimY)

    #################################################################
    # Aplicando las acciones en el tablero realizadas por alguno de
    # de los jugadores
    def action(self, i, j): 
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
