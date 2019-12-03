#!/usr/bin/env python3
import sys
from util import *

# Tipos de colores para el output
colors = {
        "reset": "\033[0m",
        "fg-black": "\033[30m",
        "fg-red": "\033[31m",
        "fg-green": "\033[32m",
        "fg-yellow": "\033[33m",
        "fg-blue": "\033[34m",
        "fg-magenta": "\033[35m",
        "fg-cyan": "\033[36m",
        "fg-white": "\033[37m",
        "fg-bright-black": "\033[90m",
        "fg-bright-red": "\033[91m",
        "fg-bright-green": "\033[92m",
        "fg-bright-yellow": "\033[93m",
        "fg-bright-blue": "\033[94m",
        "fg-bright-magenta": "\033[95m",
        "fg-bright-cyan": "\033[96m",
        "fg-bright-white": "\033[97m",
        "bg-black": "\033[40m",
        "bg-red": "\033[41m",
        "bg-green": "\033[42m",
        "bg-yellow": "\033[43m",
        "bg-blue": "\033[44m",
        "bg-magenta": "\033[45m",
        "bg-cyan": "\033[46m",
        "bg-white": "\033[47m",
        "bg-bright-black": "\033[100m",
        "bg-bright-red": "\033[101m",
        "bg-bright-green": "\033[102m",
        "bg-bright-yellow": "\033[103m",
        "bg-bright-blue": "\033[104m",
        "bg-bright-magenta": "\033[105m",
        "bg-bright-cyan": "\033[106m",
        "bg-bright-white": "\033[107m"
        }

# Lista para las coordenadas
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Solo funciona con Mac (Windows es una mierda)
def cambiarColor(string, color):
    # Comprobar que el color existe
    if color in colors:
        return ("%s%s%s" % (colors[color], string, colors["reset"]))
    return string

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
