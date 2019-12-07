#!/usr/bin/env python3
from tablero import letras

def separarCoordenada(coord):
    # Separar las coordenadas <origen>:<destino>
    # .split(":") para separar origen de destino
    # [n] para sacar la primera o segunda coordenada
    # .upper() para convertirlas en mayusculas
    return (coord.split(":")[0].upper(), coord.split(":")[1].upper())

def crearCoordenada(fila, col):
    return "%s%d" % (letras[fila], col)

def comprobarIndiceCoordenada(fila, col):
    return fila < len(letras) and col in range(0, 8)

def comprobarCoordenada(coord):
    # Si la coordenada esta dentro de letras (coordenadas de la izquierda del tablero) y si la coordenada esta en el rango [0..7] (las coordenadas de arriba del tablero) sera correcta
    return (coord[0] in letras) and (int(coord[1:]) in range(0, 8))

def indiceCoordenada(coord):
    return (letras.index(coord[0]), int(coord[1]))

def valorCoordenada(coord, tablero):
    # Va a asumir que las coordenadas son correctas (se debe llamar a comprobarCoordenada() antes)
    i, j = indiceCoordenada(coord)
    return tablero[i][j]
