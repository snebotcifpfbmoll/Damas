#!/usr/bin/env python3
import sys
from util import *
from colores import cambiarColor,comprobarColorama

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
    elif ficha == D_REINA_BLANCA:
        print(cambiarColor(cambiarColor(" ██ ", "fg-cyan"), "bg-bright-cyan"), end="")
    elif ficha == D_REINA_NEGRA:
        print(cambiarColor(cambiarColor(" ██ ", "fg-red"), "bg-bright-red"), end="")
    else:
        print(ficha, end="")

def cambiarFicha(fila, columna, ficha, tablero):
    tablero[fila][columna] = ficha

def comprobarFinalTablero(indice):
    return indice == 0 or indice == len(letras) - 1

def comprobarFinalPartida(comprobarFicha, tablero):
    for i in tablero:
        for j in i:
            if j == comprobarFicha:
                return False
    return True

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
            imprimirColor(j)
            indice_2 += 1
        print("\n")
        indice_1 += 1
