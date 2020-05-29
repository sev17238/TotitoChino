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
# ConvAI.py: Clase para conversiones.                       #
#############################################################

from TotitoChino import *


class ConvAI:
    #######################################
    # Metodo para la conversion del totito
    # en vectores horizontal y vertical al
    # totito chino convencional en forma de
    # de una tabla (matriz).
    def convAItoSIO(x, y):
        horver = 2      ##2 y 99 nunca seran utilizados, pero se usan para el inicio de las variables
        posicion = 99 
        if(x % 2 == 0):
            horver = 1 #entonces se modificara el array de rayas verticales
            if(x == 2):
                if(y==1):
                    posicion = y -1
                elif(y==3):
                    posicion = y -2
                elif(y==5):
                    posicion = y -3
                elif(y==7):
                    posicion = y -4
                elif(y==9):            
                    posicion = y -5
                posicion += 5
            elif(x == 4):
                if(y==1):
                    posicion = 0
                elif(y==3):
                    posicion = 1
                elif(y==5):
                    posicion = 2
                elif(y==7):
                    posicion = 3
                elif(y==9):            
                    posicion = 4
                posicion += 10
            elif(x == 6):
                if(y==1):
                    posicion = 0
                elif(y==3):
                    posicion = 1
                elif(y==5):
                    posicion = 2
                elif(y==7):
                    posicion = 3
                elif(y==9):            
                    posicion = 4
                posicion += 15
            elif(x == 8):
                if(y==1):
                    posicion = 0
                elif(y==3):
                    posicion = 1
                elif(y==5):
                    posicion = 2
                elif(y==7):
                    posicion = 3
                elif(y==9):            
                    posicion = 4
                posicion += 20
            elif(x == 10):
                if(y==1):
                    posicion = 0
                elif(y==3):
                    posicion = 1
                elif(y==5):
                    posicion = 2
                elif(y==7):
                    posicion = 3
                elif(y==9):            
                    posicion = 4
                posicion += 25
            else: # x == 0
                if(y==1):
                    posicion = 0
                elif(y==3):
                    posicion = 1
                elif(y==5):
                    posicion = 2
                elif(y==7):
                    posicion = 3
                elif(y==9):            
                    posicion = 4
        else:
            horver = 0 #entonces se modificara el array de rayas horizontales
            if(y == 2):
                if(x==1):
                    posicion = x -1
                elif(x==3):
                    posicion = x -2
                elif(x==5):
                    posicion = x -3
                elif(x==7):
                    posicion = x -4
                elif(x==9):            
                    posicion = x -5
                posicion += 5
            elif(y == 4):
                if(x==1):
                    posicion = 0
                elif(x==3):
                    posicion = 1
                elif(x==5):
                    posicion = 2
                elif(x==7):
                    posicion = 3
                elif(x==9):            
                    posicion = 4
                posicion += 10 
            elif(y == 6):
                if(x==1):
                    posicion = 0
                elif(x==3):
                    posicion = 1
                elif(x==5):
                    posicion = 2
                elif(x==7):
                    posicion = 3
                elif(x==9):            
                    posicion = 4
                posicion += 15
            elif(y == 8):
                if(x==1):
                    posicion = 0
                elif(x==3):
                    posicion = 1
                elif(x==5):
                    posicion = 2
                elif(x==7):
                    posicion = 3
                elif(x==9):            
                    posicion = 4
                posicion += 20 
            elif(y == 10):
                if(x==1):
                    posicion = 0
                elif(x==3):
                    posicion = 1
                elif(x==5):
                    posicion = 2
                elif(x==7):
                    posicion = 3
                elif(x==9):            
                    posicion = 4
                posicion += 25
            else: # y == 0
                if(x==1):
                    posicion = 0
                elif(x==3):
                    posicion = 1
                elif(x==5):
                    posicion = 2
                elif(x==7):
                    posicion = 3
                elif(x==9):            
                    posicion = 4

        movimiento = [horver,posicion]
        return movimiento

    #######################################
    # Metodo para la conversion del totito
    # en forma convencional (matriz) a 
    # vectores horizontal y vertical.
    def convSIOtoAI(horver,posicion):
        x=99 ## el valor de 99 nunca sera utilizado, pero se usan para el inicio de las variables
        y=99
        if(horver == 1): #en el array vertical
            if(posicion <= 4):
                if(posicion == 0):
                    y=posicion+1
                elif(posicion == 1):
                    y=posicion+2
                elif(posicion == 2):
                    y=posicion+3
                elif(posicion == 3):
                    y=posicion+4
                elif(posicion == 4):
                    y=posicion+5
                x=0
                y=posicion
            elif(posicion > 4 and posicion <= 9):
                if(posicion == 5):
                    y=1
                elif(posicion == 6):
                    y=3
                elif(posicion == 7):
                    y=5
                elif(posicion == 8):
                    y=7
                elif(posicion == 9):
                    y=9
                x=2
            elif(posicion > 9 and posicion <= 14):
                if(posicion == 10):
                    y=1
                elif(posicion == 11):
                    y=3
                elif(posicion == 12):
                    y=5
                elif(posicion == 13):
                    y=7
                elif(posicion == 14):
                    y=9
                x=4
            elif(posicion > 14 and posicion <= 19):
                if(posicion == 15):
                    y=1
                elif(posicion == 16):
                    y=3
                elif(posicion == 17):
                    y=5
                elif(posicion == 18):
                    y=7
                elif(posicion == 19):
                    y=9
                x=6
            elif(posicion > 19 and posicion <= 24):
                if(posicion == 20):
                    y=1
                elif(posicion == 21):
                    y=3
                elif(posicion == 22):
                    y=5
                elif(posicion == 23):
                    y=7
                elif(posicion == 24):
                    y=9
                x=8
            elif(posicion > 24 and posicion <= 29):
                if(posicion == 25):
                    y=1
                elif(posicion == 26):
                    y=3
                elif(posicion == 27):
                    y=5
                elif(posicion == 28):
                    y=7
                elif(posicion == 29):
                    y=9
                x=10
        else: # horver == 0 ##en el array horizontal
            if(posicion <= 4):
                if(posicion == 0):
                    x=posicion+1
                elif(posicion == 1):
                    x=posicion+2
                elif(posicion == 2):
                    x=posicion+3
                elif(posicion == 3):
                    x=posicion+4
                elif(posicion == 4):
                    x=posicion+5
                y=0
            elif(posicion > 4 and posicion <= 9):
                if(posicion == 5):
                    x=1
                elif(posicion == 6):
                    x=3
                elif(posicion == 7):
                    x=5
                elif(posicion == 8):
                    x=7
                elif(posicion == 9):
                    x=9
                y=2
            elif(posicion > 9 and posicion <= 14):
                if(posicion == 10):
                    x=1
                elif(posicion == 11):
                    x=3
                elif(posicion == 12):
                    x=5
                elif(posicion == 13):
                    x=7
                elif(posicion == 14):
                    x=9
                y=4
            elif(posicion > 14 and posicion <= 19):
                if(posicion == 15):
                    x=1
                elif(posicion == 16):
                    x=3
                elif(posicion == 17):
                    x=5
                elif(posicion == 18):
                    x=7
                elif(posicion == 19):
                    x=9
                y=6
            elif(posicion > 19 and posicion <= 24):
                if(posicion == 20):
                    x=1
                elif(posicion == 21):
                    x=3
                elif(posicion == 22):
                    x=5
                elif(posicion == 23):
                    x=7
                elif(posicion == 24):
                    x=9
                y=8
            elif(posicion > 24 and posicion <= 29):
                if(posicion == 25):
                    x=1
                elif(posicion == 26):
                    x=3
                elif(posicion == 27):
                    x=5
                elif(posicion == 28):
                    x=7
                elif(posicion == 29):
                    x=9
                y=10

        coordenadaXY = [x,y]
        return coordenadaXY


"""
def Pruebas():
    while True:
        HumanX = int(input("Please enter the 'X' coordinate of your choice (an integer such as 4): "))
        HumanY = int(input("Please enter the 'Y' coordinate of your choice (an integer such as 4): "))
        conv = convAItoSIO(HumanX,HumanY)
        print("conversion: horver: " + str(conv[0]) + " posicion: " + str(conv[1]) )

        horver = int(input("Linea:\n 0. Horizontal\n 1. Vertical\n"))
        posicion = int(input("Ingresar una posición entre 0 y 29: "))

        conv2 = convSIOtoAI(horver,posicion)
        print("conversion: X: " + str(conv2[0]) + " Y: " + str(conv2[1]))
    
        LocalBoard = [ [ 99 for i in range(30) ] for j in range(2) ]
        print("The matrix after initializing : " + str(LocalBoard))

Pruebas()
"""