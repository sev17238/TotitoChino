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
# Algoritmos.py: Clase la definicion de los algoritmos      #
# empleados: Minimax y Alpha-Beta                           #
#############################################################
# A class for defining algorithms used (minimax and alpha-beta pruning)
#
class Algoritmos: 
    
    ######################################################
    # Funcion para la definicion del algoritmo de minimax.
    def miniMax(State, Ply_num): 
        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)
                    if Ply_num < 2:
                        return (i, j)
        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algoritmos.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
                i = k[0]
                j = k[1]
        return (i, j)

    #################################################################
    # Funcion de Alpha-beta que toma en cuenta los valores de Alpha
    def Maximum(State, Ply_num, Alpha): 
        if Ply_num == 0:
            return State.CurrentScore
        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, False)
        Maximum_Score = -1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algoritmos.Minimum(z, Ply_num - 1, Maximum_Score)
            if Maximum_Score < Result:
                Maximum_Score = Result
            if Result > Alpha:
                return Result
        return Maximum_Score

    #################################################################
    # Funcion de Alpha-beta que toma en cuenta los valores de beta
    def Minimum(State, Ply_num, Beta):
        if Ply_num == 0:
            return State.CurrentScore
        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)
        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algoritmos.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
            if Result < Beta:
                return Result
        return Minimum_Score
