#!/usr/bin/env python3

# Importar dependencias
import os
from sys import platform
from tablero import *
from coordenadas import *
from movimientos import *
from colores import cambiarColor
from util import obtenerDimensiones

# Constantes del programa
MENU_WIDTH = 25

# Tablero
tablero = []

def clear():
    if platform == "win32":
        os.system("cls")
    elif platform == "darwin" or platform == "linux" or platform == "linux2":
        os.system("clear")

# Mostrar las noramas del juego
def normas():
    clear()
    menu_border = cambiarColor("█", "fg-red")
    print("%s\n" % (menu_border * MENU_WIDTH))
    print("- Las damas se juegan entre dos personas en un tablero de ajedrez.Cada jugador dispone de 12 piezas de un mismo  color (blancas i negras).")
    print("- Se juega por turnos alternos. Empieza a jugar el que juega con las blancas. En su  turno cada jugador mueve una pieza própia. Las piezas se mueven una posición adelante en diagonal.")
    print("- Cuando se come,las piezas saltan por encima de una pieza contraria en diagonal i van a parar a la casilla siguiente,que es obligatoria que este vacia.")
    print("- Las capturas se pueden encadenar,eso pasa si al comer una pieza y colocarte en la posición pertinente puedes volver a comer.")
    print("- Al llegar al otro extremo del tablero con una ficha,esta se convierte en DAMA,las damas pueden mover hacia adelante y hacia  atrás hacia las  cuatro direcciones en diagonal, una o varias casillas.")
    print("\n%s\n" % (menu_border * MENU_WIDTH))
    input("PULSA CUALQUIER TECLA PARA VOLVER AL MENÚ")

def menu():
    clear()
    menu_border = cambiarColor("█", "fg-blue")
    print("%s" % (menu_border * MENU_WIDTH))
    print("%s%s%s" % (menu_border * 2, " " * (MENU_WIDTH - 4), menu_border * 2))
    print("%s%s%s" % (menu_border * 2, cambiarColor("MENÚ".center(MENU_WIDTH - 4), "fg-yellow"), menu_border * 2))
    print("%s%s%s" % (menu_border * 2, " " * (MENU_WIDTH - 4), menu_border * 2))
    print("%s" % (menu_border * MENU_WIDTH))
    print("")
    print("\t%s" % (cambiarColor(cambiarColor("1) Normas", "fg-white"), "bg-red")))
    print("\t%s" % (cambiarColor(cambiarColor("2) Empezar Partida", "fg-white"), "bg-blue")))
    print("\t%s" % (cambiarColor(cambiarColor("3) Salir", "fg-white"), "bg-bright-black")))
    opcion = int(input("> "))
    return opcion

def comprobarMovimientoJugador(coord, turno, contador):
    if ":" in coord:
        origen, destino = separarCoordenada(coord)
        if comprobarCoordenada(origen) and comprobarCoordenada(destino):
            # Comprobar turnos
            if (contador % 2 == 0 and (valorCoordenada(origen, tablero) == D_NEGRA or valorCoordenada(origen, tablero) == D_REINA_NEGRA) or (contador % 2 != 0 and (valorCoordenada(origen, tablero) == D_BLANCA or valorCoordenada(origen, tablero) == D_REINA_BLANCA))):
                # Comprobar movimiento
                movimiento_correcto, matanza = comprobarMovimiento(origen, destino, tablero)
                if movimiento_correcto:
                    ficha = valorCoordenada(origen, tablero)
                    mover(origen, destino, tablero)
                    if matanza == False:
                        contador += 1
                    # Comprobar reina
                    if ficha != D_REINA_BLANCA and ficha != D_REINA_NEGRA:
                        dst_f, dst_c = indiceCoordenada(destino)
                        if comprobarFinalTablero(dst_f):
                            if ficha == D_BLANCA:
                                cambiarFicha(dst_f, dst_c, D_REINA_BLANCA, tablero)
                            elif ficha == D_NEGRA:
                                cambiarFicha(dst_f, dst_c, D_REINA_NEGRA, tablero)
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
    return contador

# Programa principal
width, height = obtenerDimensiones()
if width != 0:
    MENU_WIDTH = width
opcion = 0
while opcion != 3:
    opcion = menu()
    if opcion == 1:
        normas()
    elif opcion == 2:
        # Tablero inical:
        tablero = [
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [3, 0, 3, 0, 3, 0, 3, 0],
                [0, 3, 0, 3, 0, 3, 0, 3],
                [3, 0, 3, 0, 3, 0, 3, 0]]
        # Contador de turnos:
        # Cada vez que un movimiento sea valida el contador va a subir +1
        # Si el contador es un numero par va a ser el turno de las negras, si es impar va a ser el turno de las blancas
        contador_turnos = 1
        ganador = ""
        while ganador == "":
            # Comprobar final partida
            if comprobarFinalPartida(D_BLANCA, tablero):
                ganador = cambiarColor(cambiarColor("ROJAS", "fg-white"), "bg-red")
            elif comprobarFinalPartida(D_NEGRA, tablero):
                ganador = cambiarColor(cambiarColor("AZULES", "fg-white"), "bg-cyan")
            else:
                clear() # Limpiar la pantalla
                turno = ""
                color = ""
                if contador_turnos % 2 == 0:
                    turno = "Rojas"
                    color = "bg-red"
                else:
                    turno = "Azules"
                    color = "bg-cyan"
                print(cambiarColor(cambiarColor("TURNO: %s" % (turno), color), "bg-red")) # Colores!
                mostrarTablero(tablero)
                # Pedir un movimiento
                print("\nIntroduce la coordenada de la ficha que quieres mover y la de destino. (<Origen>:<Destino>)")
                coord = input("> ")
                if coord != "":
                    # Modo "dios" usado durante el desarrollo
                    if coord == "/mododios":
                        op = ""
                        while op != "q":
                            clear()
                            mostrarTablero(tablero)
                            op = input("# ").lower()
                            if op != "":
                                if ":" in op:
                                    org, dst = separarCoordenada(op)
                                    if comprobarCoordenada(org) and comprobarCoordenada(dst):
                                        mover(org, dst, tablero)
                                elif op[0] == "/":
                                    cmd = op[1:].split(" ")
                                    if len(cmd) > 1:
                                        if cmd[0] == "reina":
                                            tmp_coord = cmd[1].upper()
                                            if comprobarCoordenada(tmp_coord):
                                                ficha = valorCoordenada(tmp_coord, tablero)
                                                if ficha == D_NEGRA or ficha == D_BLANCA:
                                                    fila, col = indiceCoordenada(tmp_coord)
                                                    cambiarFicha(fila, col, ficha + 2, tablero)
                                        elif cmd[0] == "kill":
                                            coords = cmd[1].split(",")
                                            for tmp_coord in coords:
                                                tmp_coord = tmp_coord.upper()
                                                if comprobarCoordenada(tmp_coord):
                                                    ficha = valorCoordenada(tmp_coord, tablero)
                                                    if ficha == D_NEGRA or ficha == D_BLANCA:
                                                        fila, col = indiceCoordenada(tmp_coord)
                                                        cambiarFicha(fila, col, E_NEGRO, tablero)
                    else:
                        # Comprobar que el movimiento
                        contador_turnos = comprobarMovimientoJugador(coord, turno, contador_turnos)
        print("Las fichas %s han ganado!" % (ganador), end="")
        input()
    elif opcion == 3:
        # El bucle va a terminar (no hacer nada)
        print("", end="")
    else:
        print("La opcion %d no es válida." % (opcion), end="")
        input()
