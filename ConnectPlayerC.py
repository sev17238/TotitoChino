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
# ConnectPlayerC.py: CONEXION DE CLIENTE                    #
#############################################################

# Libreria para la conexion con el servidor
import socketio 

#Clases para la inteligencia artificial
from TotitoChino import *
from ConvAI import *

#Datos para conectarse al torneo
nombre_usuario = ""
id_torneo = ""
id_partida = ""

#socket para conectarse al servidor
socket_io = socketio.Client()


####_________________________________________________________CONEXION___________________________________________________________####

#########################################
# Metodo para la conexion con el servidor
@socket_io.on('connect')
def connect():
    ## Client has connected
    print("" + nombre_usuario + " conectado. ")
    print('conexion establecida')

    ## Signin signal
    socket_io.emit('signin', {
        'user_name' : nombre_usuario,
        'tournament_id' : id_torneo,
        'user_role' : 'player'
    })

#########################################
# Metodo para jugar de nuevo luego de 
# terminar alguna partida con un 
# adversario.
@socket_io.on('ready')
def ready(info):
    #print("Tablero que viene del servidor")
    #print(info['board'])
    print("   (#############¡¡Jugando!!############)")
    print("   (####################################)")
    print("   (------------------------------------)")
    print(" _(           oooO         Oooo          )_")
    print("(          ________       ________         )")
    print("(_           ~~     _| |_     ~~          _)")
    print("  (                |     |               )")
    print("  (                  ---                 )")
    print("    (             \_______/            )")
    print("      (                              )")
    print("        (            ___           )")
    print("             (                )")

    ##AQUI SE VERIFICA LA JUGADA (coordenada) QUE HIZO EL JUGADOR DEL OTRO LADO DEL SERVER
    #si el tablero ya tiene alguna jugada entonces se debe verificar la coordenada y responder acorde a eso
    i = 0
    pos_arr1 = 0
    pos_arr2 = 0
    horver = 2
    different_pos = 99 #sera la posicion en la cual el tablero que viene del server se diferencia con el que se tenia
    pos_value = 0
    while (i <= 29):
        pos_arr1 = info['board'][0][i]
        pos_arr2 = Match.LocalBoard[0][i]
        if(pos_arr1 != pos_arr2):
            different_pos=pos_arr1
            horver = 0
            pos_value = i
            i=29
        i=i+1
    if(horver == 2): #to start again if there are no equal values
        i=0
    while (i <= 29):
        pos_arr1 = info['board'][1][i]
        pos_arr2 = Match.LocalBoard[1][i]
        if(pos_arr1 != pos_arr2):
            different_pos=pos_arr1
            horver = 1
            pos_value = i
            i=29
        i=i+1

    #if(horver != 2 and different_pos != -2  and different_pos != -1 and different_pos != 1 and different_pos != 99): #si se encontro alguna diferencia entonces se recive la jugada 
    if(horver != 2): #si se encontro alguna diferencia entonces se recibe la jugada 
        #different_pos = 0
        #conv1 = ConvAI.convSIOtoAI(horver,different_pos)
        conv1 = ConvAI.convSIOtoAI(horver,pos_value)
        #print("horver:"+str(horver)+" different_pos:"+str(different_pos))
        #print("conv1: x:"+str(conv1[0])+" y:"+str(conv1[1]))
        Match.MoveFromOther(conv1[0],conv1[1])
        ##print("jugada del otro: x:" +str(conv1[0]) + " y:" + str(conv1[1]))
        AImove = Match.AIdotsAndBoxesMove()
        conv2 = ConvAI.convAItoSIO(AImove[0],AImove[1])

        horver = conv2[0]
        posicion = conv2[1]
        movimiento = [horver, posicion]

    else: #sino, entonces se juega primero
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

    Match.LocalBoard = info['board']
    if(movimiento[0]==0): #Horizontal
        if(Match.LocalBoard[0][posicion] != -1 and Match.LocalBoard[0][posicion] != 1 and Match.LocalBoard[0][posicion] != -2 and Match.LocalBoard[0][posicion] != 2):
            Match.LocalBoard[0][posicion] = 0
    elif(movimiento[0]==1): #Vertical
        if(Match.LocalBoard[1][posicion] != -1 and Match.LocalBoard[1][posicion] != 1 and Match.LocalBoard[1][posicion] != -2 and Match.LocalBoard[1][posicion] != 2):
            Match.LocalBoard[1][posicion] = 0

    #print("Tablero con la nueva jugada local: ")
    #print(Match.LocalBoard)

#########################################
# Metodo para finalizar la partida contra
# algun adversario.
#########################################
# En este metodo se resetea el objeto de 
# tipo TotitoChino que se utiliza para 
# llevar el control del juego de forma
# local. 
@socket_io.on('finish')
def finish(info):
    print("La paltida: ", info['game_id'], "ha telminado!")
    if info['player_turn_id'] == info['winner_turn_id']:
        print("Has alazado con tu oponente! Ahola eles el papa de Lei Gong, Guan Yu, Shou-Hsing y todos los otlos dioses chinos!")
    else:
        print("Te han delotado! Molilas en la velguenza y te ilas al infielno con los Yaoguai!")

    print("\n¡¡Listo pala jugal de nuevo!!")
    Match.Reset(11,11,2)
    socket_io.emit('player_ready',{
        'tournament_id': id_torneo,
        'game_id': info['game_id'],
        'player_turn_id': info['player_turn_id']
    })


####_________________________________________________________Inicializacion_______________________________________________________________
print("\nBIENVENIDO!! Estas listo pala plesencial el mejol juego del mundo! ")
print(" ¿PLEPALADO? ")
print("¡¡TOTITOOOOOO CHINOOOOOOOOOOOOO!!!\n")

nombre_usuario = input("Inglese su nomble de usualio: \n")
id_torneo = input("Inglese la id pala unilse al tolneo: \n")
host = input("Inglese el link pala la conexion: ")

## inicializacion del tablero y de la profundidad con la que el arbol jugara
X_dimension = 5 * 2 + 1
Y_dimension = 5 * 2 + 1
Profundidad = 2
Match = TotitoChino(X_dimension, Y_dimension, Profundidad)

print("Campos y valiables inicializados.")

##socket_io.connect('http://localhost:'+host)
socket_io.connect(host)
socket_io.wait()


