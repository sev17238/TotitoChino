###################################
# Guatemala, mayo del 2020
# Diego Sevilla 17238
# Inteligencia artificial
####################################
# CONEXION DE CLIENTE
####################################

##6*6 board

# Para la conexion con el servidor
import socketio 
# Para la representacion de la matriz del juego y su manejo
#import numpy as np
#import random

#Para la inteligencia
from Algorithm import *
from DotsNBoxes import *
from Board import *
from Nodes import *
from ConvAI import *

#DATOS PARA INGRESAR AL TORNEO
nombre_usuario = ""
id_torneo = ""
id_partida = ""

#Variables globales
#all99 = True
#newBoard = []

#socket para conectarse al servidor
socket_io = socketio.Client()

####_________________________________________________________CONEXION_______________________________________________________________
@socket_io.on('connect')
def connect():
    ## Client has connected
    print("" + nombre_usuario + " conectado. ")
    print('coneccion establecida')
    
    ## Signin signal
    socket_io.emit('signin', {
        'user_name' : nombre_usuario,
        'tournament_id' : id_torneo,
        'user_role' : 'player'
    })

@socket_io.on('ready')
def ready(info):
    print("Tablero con la jugada del otro jugador")
    print(info['board'])
    
    #ran = random.randint(0, 1)
    #ran2 = random.randint(0, 29)
    #horver = ran
    #posicion = ran2

    ##AQUI SE VERIFICA LA JUGADA (coordenada) QUE HIZO EL JUGADOR DEL OTRO LADO DEL SERVER
    if(all99 == 0): #si el tablero ya tiene alguna jugada entonces se debe verificar la coordenada y responder acorde a eso
        i = 0
        pos_arr1 = 0
        pos_arr2 = 0
        horver = 2
        different_pos = [] #sera la posicion en la cual el tablero que viene del server se diferencia con el que se tenia
        while (i <= 29):
            pos_arr1 = info['board'][0][i]
            pos_arr2 = newBoard[0][i]
            if(pos_arr1 != pos_arr2):
                different_pos[0]=pos_arr1
                horver = 0
        while (i <= 29):
            pos_arr1 = info['board'][1][i]
            pos_arr2 = newBoard[1][i]
            if(pos_arr1 != pos_arr2):
                different_pos[0]=pos_arr1
                horver = 1
        conv1 = ConvAI.convSIOtoAI(horver,different_pos[0])
        Match.MoveFromOther(conv1[0],conv1[1])
        AImove = Match.AIdotsAndBoxesMove()
        conv2 = ConvAI.convAItoSIO(AImove[0],AImove[1])

        horver = conv2[0]
        posicion = conv2[1]
        movimiento = [horver, posicion]
        
    elif(all99 == 1): #Si el tablero esta "vacio", osea con 99s, entonces el que empieza a jugar es la inteligencia.
        all99 = 0

        AImove = Match.AIdotsAndBoxesMove()
        fstconv = ConvAI.convAItoSIO(AImove[0],AImove[1])

        horver = fstconv[0]
        posicion = fstconv[1]
        movimiento = [horver, posicion]


    socket_io.emit('play', {
        'player_turn_id' : info['player_turn_id'],
        'tournament_id' : id_torneo,
        'game_id' : info['game_id'],
        'movement': movimiento
    })

    newBoard = info['board']
    if(movimiento[0]==0): #Horizontal
        if(newBoard[0][posicion] != -1 and newBoard[0][posicion] != 1 and newBoard[0][posicion] != -2 and newBoard[0][posicion] != 2):
            newBoard[0][posicion] = 0
    elif(movimiento[0]==1): #Vertical
        if(newBoard[1][posicion] != -1 and newBoard[1][posicion] != 1 and newBoard[1][posicion] != -2 and newBoard[1][posicion] != 2):
            newBoard[1][posicion] = 0

    print("Tablero con la nueva jugada local: ")
    print(newBoard)



@socket_io.on('finish')
def finish(info):
    print("La partida: ", info['game_id'], "ha terminado!")
    if info['player_turn_id'] == info['winner_turn_id']:
        print("Felicidades, arrasaste con tu oponente! Ahora eres el papa de ZEUS!")
        all99 = 1
    else:
        print("Te han derrotado! Moriras en la verguenza y la deshonra!")
        all99 = 1

    socket_io.emit('player_ready',{
        'tournament_id': id_torneo,
        'game_id': info['game_id'],
        'player_turn_id': info['player_turn_id']
    })


####_________________________________________________________Inicializacion_______________________________________________________________
nombre_usuario = input("Ingrese su nombre de usuario: \n")
id_torneo = input("Ingrese la id para unirse al torneo: \n")
host = input("Ingrese el link para conexion: ")

## inicializacion del tablero y de la profundidad con la que el arbol jugara
X_dimension = 5 * 2 + 1
Y_dimension = 5 * 2 + 1
Profundidad = 2
Match = DotsNBoxes(X_dimension, Y_dimension, Profundidad)

print("Campos y variables inicializados.")

##socket_io.connect('http://localhost:'+host)
socket_io.connect(host)
socket_io.wait()


