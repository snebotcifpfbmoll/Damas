#!/usr/bin/env python3

# Importar dependencias
from tablero import mostrarTablero
from coordenadas import *
from movimientos import mover

# Constantes del programa
E_BLANCO = 0
E_NEGRO = 1
D_NEGRA = 2
D_BLANCA = 3

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

# Programa principal
# TESTS
mostrarTablero(tablero)
# Preguntar por una cooredenadad
print("\nIntroduce la coordenada de la ficha que quieres mover y la de destino. (<Origen>:<Destino>)")
coord = input("> ")
if ":" in coord:
    c1, c2 = separarCoordenada(coord)
    if comprobarCoordenada(c1) and comprobarCoordenada(c2):
        mover(c1, c2, tablero)
        mostrarTablero(tablero)
