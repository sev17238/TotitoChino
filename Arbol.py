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
# Arbol.py: Clase para operaciones relacionadas con nodos   #
#############################################################

class Arbol: 
    def __init__(self, currentState):
        self.Current = currentState
        self.CurrentScore = 0
        self.children = {}

    def Make(self, i, j, player): # Function for generating a child node
        self.children[(i, j)] = Arbol(self.Current.Get_currentState())
        mul = 1
        if player:
            mul *= -1
        self.children[(i, j)].CurrentScore = (self.children[(i, j)].Current.action(i, j) * mul) + self.CurrentScore

    def Populate(self, i, j, Child): # Function for adding a node
        self.children[(i,j)] = Child

    def Draw(self): # function for drawing the board
        self.Current.Draw_mat()
