#!/usr/bin/env python3

# Importar dependencias
import os
from sys import platform
from tablero import mostrarTablero
from coordenadas import *
from movimientos import *
from colores import cambiarColor

# Constantes del programa
MENU_WIDTH = 25

# Tablero inicial (posicion de las damas)
tablero = [
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [3, 0, 3, 0, 3, 0, 3, 0],
        [0, 3, 0, 3, 0, 3, 0, 3],
        [3, 0, 3, 0, 3, 0, 3, 0]]

def clear():
    if platform == "win32":
        os.system("cls")
    elif platform == "darwin" or platform == "linux" or platform == "linux2":
        os.system("clear")

# Mostrar las noramas del juego
def normas():
    clear()
    print("%s" % ("=" * MENU_WIDTH))
    print("Las damas se juegan entre dos personas en un tablero de ajedrez.Cada jugador dispone de 12 piezas de un mismo  color (blancas i  negras).")
    print("Se juega por turnos alternos. Empieza a jugar el que juega con las blancas. En su  turno cada jugador mueve una pieza própia. Las piezas se mueven una posición adelante en diagonal.")
    print("Cuando se come,las piezas saltan por encima de una pieza contraria en diagonal i van a parar a la casilla siguiente,que es obligatoria que este vacia.")
    print("Las capturas se pueden encadenar,eso pasa si al comer una pieza y colocarte en la posición pertinente puedes volver a comer.")
    print("Al llegar al otro extremo del tablero con una ficha,esta se convierte en DAMA,las damas pueden mover hacia adelante y hacia  atrás hacia las  cuatro direcciones en diagonal, una o varias casillas.")
    print("%s" % ("=" * MENU_WIDTH))
    input("PULSA CUALQUIER TECLA PARA VOLVER AL MENÚ")

def menu():
    clear()
    print("%s" % ("=" * MENU_WIDTH))
    print("=%s=" % ("MENÚ".center(MENU_WIDTH - 2)))
    print("%s" % ("=" * MENU_WIDTH))
    print("\t1) Normas")
    print("\t2) Empezar partida")
    print("\t3) Salir")
    opcion = int(input("> "))
    return opcion

# Programa principal
opcion = 0
while opcion != 3:
    opcion = menu()
    if opcion == 1:
        normas()
    elif opcion == 2:
        # partida
        contador_turnos = 1
        while True:
            clear()
            turno = ""
            color = ""
            if contador_turnos % 2 == 0:
                turno = "Rojas"
                color = "bg-red"
            else:
                turno = "Azules"
                color = "bg-cyan"
            print(cambiarColor(cambiarColor("TURNO: %s" % (turno), color), "bg-red"))
            mostrarTablero(tablero)
            print("\nIntroduce la coordenada de la ficha que quieres mover y la de destino. (<Origen>:<Destino>)")
            coord = input("> ")
            if ":" in coord:
                origen, destino = separarCoordenada(coord)
                if comprobarCoordenada(origen) and comprobarCoordenada(destino):
                    # Comprobar turnos
                    if (contador_turnos % 2 == 0 and valorCoordenada(origen, tablero) == D_NEGRA) or (contador_turnos % 2 != 0 and valorCoordenada(origen, tablero) == D_BLANCA):
                        # Comprobar movimiento
                        movimiento_correcto, matanza = comprobarMovimiento(origen, destino, tablero)
                        if movimiento_correcto:
                            mover(origen, destino, tablero)
                            if matanza:
                                print("Sa matao paco!", end="")
                                input()
                            else:
                                contador_turnos += 1
                        else:
                            print("No se puede mover la ficha al lugar indicado.", end="")
                            input()
                    elif valorCoordenada(origen, tablero) == E_BLANCO or valorCoordenada(origen, tablero) == E_NEGRO:
                        print("No hay ninguna ficha en esa coordenada.", end="")
                        input()
                    else:
                        print("No es su turno. Payaso.", end="")
                        input()
                else:
                    print("Las coordenadas indicadas no son correctas.", end="")
                    input()
            else:
                print("Las coordenadas indicadas no son correctas.", end="")
                input()
    elif opcion == 3:
        # El bucle va a terminar
        print("", end="")
    else:
        print("La opcion %d no es válida." % (opcion), end="")
        input()
