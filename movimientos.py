#!/usr/bin/env python3
from util import *
from coordenadas import *
from tablero import cambiarFicha

def mover(origen, destino, tablero):
    org_1, org_2 = indiceCoordenada(origen) #1 colmuna 2 fila.
    dst_1, dst_2 = indiceCoordenada(destino)
    cambiarFicha(dst_1, dst_2, tablero[org_1][org_2], tablero)
    cambiarFicha(org_1, org_2, E_NEGRO, tablero)

# Comprobar si el movimiento es correcto. Va a suponer que las coordenadas son correctas (estan dentro del tablero)
def comprobarMovimiento(origen, destino, tablero):
    # Obtener el valor de las coordenadas
    forigen = valorCoordenada(origen, tablero)
    fdestino = valorCoordenada(destino, tablero)
    # Solo se podra mover al destino si la casilla es negra
    if fdestino != E_NEGRO:
        return (False, False)

    org_f, org_c = indiceCoordenada(origen)
    dst_f, dst_c = indiceCoordenada(destino)
    coordFichaIntermedia = "" # En caso de matar a una ficha esta va a ser la coordenada de la ficha a matar
    fichaContraria = 0
    # Comprobar tipo de ficha
    if forigen == D_BLANCA:
        # Las fichas blancas solo se pueden mover hacia arriba
        if dst_f == org_f - 1:
            # movimiento normal
            if dst_c == org_c - 1 or dst_c == org_c + 1:
                return (True, False)
        elif dst_f == org_f - 2:
            # matar
            if dst_c == org_c - 2:
                coordFichaIntermedia = crearCoordenada(org_f - 1, org_c - 1)
                fichaContraria = D_NEGRA
            elif dst_c == org_c + 2:
                coordFichaIntermedia = crearCoordenada(org_f - 1, org_c + 1)
                fichaContraria = D_NEGRA
    elif forigen == D_NEGRA:
        # Las fichas negras solo se pueden mover hacia abajo
        if dst_f == org_f + 1:
            # movimiento normal
            if dst_c == org_c - 1 or dst_c == org_c + 1:
                return (True, False)
        elif dst_f == org_f + 2:
            # matar
            if dst_c == org_c - 2:
                coordFichaIntermedia = crearCoordenada(org_f + 1, org_c - 1)
                fichaContraria = D_BLANCA
            elif dst_c == org_c + 2:
                coordFichaIntermedia = crearCoordenada(org_f + 1, org_c + 1)
                fichaContraria = D_BLANCA
    elif forigen == D_REINA_BLANCA or forigen == D_REINA_NEGRA:
        if dst_f == org_f + 1 or dst_f == org_f - 1:
            # movimiento normal
            if dst_c == org_c - 1 or dst_c == org_c + 1:
                return (True, False)
        elif dst_f == org_f + 2:
            # matar
            if dst_c == org_c - 2:
                coordFichaIntermedia = crearCoordenada(org_f + 1, org_c - 1)
                if forigen == D_REINA_BLANCA:
                    fichaContraria = D_NEGRA
                elif forigen == D_REINA_NEGRA:
                    fichaContraria = D_BLANCA
            elif dst_c == org_c + 2:
                coordFichaIntermedia = crearCoordenada(org_f + 1, org_c + 1)
                if forigen == D_REINA_BLANCA:
                    fichaContraria = D_NEGRA
                elif forigen == D_REINA_NEGRA:
                    fichaContraria = D_BLANCA
        elif dst_f == org_f - 2:
            # matar
            if dst_c == org_c - 2:
                coordFichaIntermedia = crearCoordenada(org_f - 1, org_c - 1)
                if forigen == D_REINA_BLANCA:
                    fichaContraria = D_NEGRA
                elif forigen == D_REINA_NEGRA:
                    fichaContraria = D_BLANCA
            elif dst_c == org_c + 2:
                coordFichaIntermedia = crearCoordenada(org_f - 1, org_c + 1)
                if forigen == D_REINA_BLANCA:
                    fichaContraria = D_NEGRA
                elif forigen == D_REINA_NEGRA:
                    fichaContraria = D_BLANCA
    if coordFichaIntermedia != "" and fichaContraria != 0:
        if comprobarCoordenada(coordFichaIntermedia):
            fichaIntermedia = valorCoordenada(coordFichaIntermedia, tablero)
            if fichaIntermedia == fichaContraria or fichaIntermedia == fichaContraria + 2:
                fila, col = indiceCoordenada(coordFichaIntermedia)
                cambiarFicha(fila, col, E_NEGRO, tablero)
                return (True, True)

    return (False, False)

