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
import random

nombre_usuario = ""
id_torneo = ""
id_partida = ""
#tablero = []

socket_io = socketio.Client()

'''@sio.event
def conn():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    socket_io.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')
'''

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

@socket_io.event
def error():
    print("Connection failed")


@socket_io.on('ready')
def ready(info):
    print("Estado del board.")
    print(info['board'])

    ran = random.randint(0, 1)
    ran2 = random.randint(0, 29)
    horver = ran
    posicion = ran2

    #horver = int(input("Linea:\n 0. Horizontal\n 1. Vertical\n"))
    #posicion = int(input("Ingresar una posición entre 0 y 29: "))
    movimiento = [horver, posicion]
    #

    #conversion de vuelta

    socket_io.emit('play', {
        'player_turn_id' : info['player_turn_id'],
        'tournament_id' : id_torneo,
        'game_id' : info['game_id'],
        'movement': movimiento
    })


@socket_io.on('finish')
def finish(info):
    print("La partida: ", info['game_id'], "ha terminado!")
    if info['player_turn_id'] == info['winner_turn_id']:
        print("Felicidades, arrasaste con tu oponente! Ahora eres el papa de ZEUS!")
        started = False
    else:
        print("Te han derrotado! Moriras en la verguenza y la deshonra!")
        started = False

    socket_io.emit('player_ready',{
        'tournament_id': id_torneo,
        'game_id': info['game_id'],
        'player_turn_id': info['player_turn_id']
    })


nombre_usuario = input("Ingrese su nombre de usuario: \n")
id_torneo = input("Ingrese la id para unirse al torneo: \n")
host = input("Ingrese el link para conexion: ")

##socket_io.connect('http://localhost:'+host)
socket_io.connect(host)
socket_io.wait()