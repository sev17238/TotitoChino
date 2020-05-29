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
# TotitoChino.py: Clase para el manejo de jugadas           #
# realizadas por la AI local y por quien este               #
# del otro lado del servidor.                               #
#############################################################

import collections
from MiniAlphaBeta import *
from MatrizTJuego import *
from Arbol import *

class TotitoChino:

    def __init__(self, X_dim, Y_dim, Profundidad):
        currentState = MatrizTJuego([], X_dim, Y_dim)
        currentState.Inicializacion()
        self.State = Arbol(currentState)
        self.Profundidad = Profundidad
        self.Score = 0
        self.LocalBoard = [ [ 99 for i in range(30) ] for j in range(2) ] #[[99,99,99,99,99,99,...,99][99,99,99,99,99,99,...,99]]

    #####################################
    # Metodo para debuggeo y para pruebas 
    def Pruebas(self):
        print(self.State.Current.Get_currentState())
        """
            print("current Board State Matrix horizontal: ")
            print(self.State.Current.Get_currentState().Mat[0])
            print(self.State.Current.Get_currentState().Mat[2])
            print(self.State.Current.Get_currentState().Mat[4])
            print(self.State.Current.Get_currentState().Mat[6])
            print(self.State.Current.Get_currentState().Mat[8])
            print(self.State.Current.Get_currentState().Mat[10])
            print("current Board State Matrix vertical: ")
            print(self.State.Current.Get_currentState().Mat[1])
            print(self.State.Current.Get_currentState().Mat[3])
            print(self.State.Current.Get_currentState().Mat[5])
            print(self.State.Current.Get_currentState().Mat[7])
            print(self.State.Current.Get_currentState().Mat[9])"""

        """
            print("current Board State Matrix horizontal: ")
            print(self.State.Current.Get_currentState().Mat[0])
            print(self.State.Current.Get_currentState().Mat[1])
            print(self.State.Current.Get_currentState().Mat[2])
            print(self.State.Current.Get_currentState().Mat[3])
            print(self.State.Current.Get_currentState().Mat[4])
            print(self.State.Current.Get_currentState().Mat[5])
            print(self.State.Current.Get_currentState().Mat[6])
            print(self.State.Current.Get_currentState().Mat[7])
            print(self.State.Current.Get_currentState().Mat[8])
            print(self.State.Current.Get_currentState().Mat[9])
            print(self.State.Current.Get_currentState().Mat[10])"""
        self.State.Draw()

    ##______________________________________________________________________________________________________________________________________
    
    #####################################################
    # Funcion que se encarga de recivir la jugada del
    # jugador al otro lado del server con quien se 
    # esta jugando.
    def MoveFromOther(self, otherX,otherY): 
        if (otherX, otherY) not in self.State.children:
            self.State.Make(otherX, otherY, False)
            self.State = self.State.children[(otherX, otherY)]
        else:
            self.State = self.State.children[(otherX, otherY)]

        #print("El otro jugador eligio esta coordenada:\n" + "(" ,str(otherX), ", " + str(otherY), ")", end = "\n")

    #####################################################
    # Funcion que define los movimientos de la 
    # inteligencia artificial tomando en 
    # cuenta el estado del tablero.
    def AIdotsAndBoxesMove(self): # Defining the Computer player and its actions/Choices
        move = MiniAlphaBeta.miniMax(self.State, self.Profundidad)
        self.State = self.State.children[(move[0], move[1])]

        #print("La coordenada elejida es:\n" + "(" ,str(move[0]), ", " + str(move[1]), ")", end = "\n")

        movimiento = [move[0],move[1]]
        return movimiento

    ########################################################
    # Funcion para el reseteo del tablero y el juego en si.
    def Reset(self, X_dim, Y_dim, Profundidad): 
        currentState = MatrizTJuego([], X_dim, Y_dim)
        currentState.Inicializacion()
        self.State = Arbol(currentState)
        self.Profundidad = Profundidad
        self.Score = 0
        self.LocalBoard = [ [ 99 for i in range(30) ] for j in range(2) ] #[[99,99,99,99,99,99,...,99][99,99,99,99,99,99,...,99]]

