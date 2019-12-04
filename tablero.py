#!/usr/bin/env python3
import sys
from util import *
from colores import cambiarColor

# Lista para las coordenadas
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def imprimirColor(ficha):
    if ficha == E_NEGRO:
        print(cambiarColor(" ██ ", "fg-black"), end="")
    elif ficha == E_BLANCO:
        print(cambiarColor(" ██ ", "fg-white"), end="")
    elif ficha == D_NEGRA:
        print(cambiarColor(" ██ ", "fg-red"), end="")
    elif ficha == D_BLANCA:
        print(cambiarColor(" ██ ", "fg-cyan"), end="")
    else:
        print(ficha, end="")

def mostrarTablero(tablero):
    # Imprimir las coordenadas de arriba
    print("   ", end="") # Alinear numeros
    for i in range(0, 8):
        print("  %s " % (i), end="")
    print("")

    indice_1 = 0 # La utilizaremos para acceder a la lista de letras
    for i in tablero:
        indice_2 = 0 # La utilizaremos para saber en que fila nos encontramos
        for j in i:
            # Imprimir coordenadas laterales
            if indice_2 == 0:
                print("%s: " % (letras[indice_1]), end="")
            # Comprobar si la plataforma es darwin (Mac) o linux. Si es Windows o otro lo imprimimos de forma normal.
            if sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2":
                imprimirColor(j)
            elif sys.platform == "win32":
                try:
                    import colorama
                    colorama.init()
                    imprimirColor(j)
                except:
                    print(j, end="")
            else:
                print(j, end="")
            indice_2 += 1
        print("\n")
        indice_1 += 1
