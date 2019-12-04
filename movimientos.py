#!/usr/bin/env python3
from util import *
from coordenadas import *

def mover(origen, destino, tablero):
    org_1, org_2 = indiceCoordenada(origen) #1 colmuna 2 fila.
    dst_1, dst_2 = indiceCoordenada(destino)
    tablero[dst_1][dst_2] = tablero[org_1][org_2]
    tablero[org_1][org_2] = E_NEGRO

def comprobarColor(x,y,tablero):
    origenC, origenF = indiceCoordenada(x)
    destinoC, destinoF = indiceCoordenada(y)
    comprobacion=False
    if tablero[origenC][origenF]== D_BLANCA  and tablero[destinoC][destinoF]==D_NEGRA:
        comprobacion=True
    if tablero[origenC][origenF]== D_NEGRA and tablero[destinoC][destinoF]==D_BLANCA :
        comprobacion=True
    return comprobacion

def comprobarMatanza(origen,destino,tablero):
    origenC, origenF = indiceCoordenada(origen)
    destinoC, destinoF = indiceCoordenada(destino)
    
    if tablero[origenC][origenF]==3:
        if destinoC==(origenC+2):
            fichaIntermediaC=(destinoC-1)
            fichaIntermediaF=(destinoF+1)
            fichaIntermedia=(fichaIntermediaC,fichaIntermediaF)
            return comprobarColor(origen,fichaIntermedia,tablero)
        elif destinoC==(origenC-2):
            fichaIntermediaC=(destinoC+1)
            fichaIntermediaF=(destinoF+1)
            return comprobarColor(origen,fichaIntermedia,tablero)
    
    elif tablero[origenC][origenF]==2:
        if destinoC==(origenC+2):
            fichaIntermediaC=(destinoC-1)
            fichaIntermediaF=(destinoF-1)
            fichaIntermedia=(fichaIntermediaC,fichaIntermediaF)
            return comprobarColor(origen,fichaIntermedia,tablero)
    
        if destinoC==(origenC-2):
            fichaIntermediaC=(destinoC+1)
            fichaIntermediaF=(destinoF-1)
            comprobacion=comprobarColor(origen,fichaIntermedia,tablero)
            return comprobarColor(origen,fichaIntermedia,tablero)
    return False

#def comprobarFichaIntermedia(fila, columna, tablero):

# Comprobar si el movimiento es correcto. Va a suponer que las coordenadas son correctas (estan dentro del tablero)
def comprobarMovimiento(origen, destino, tablero):
    # Obtener el valor de las coordenadas
    forigen = valorCoordenada(origen, tablero)
    fdestino = valorCoordenada(destino, tablero)
    # Comprobar direccion del movimiento
    if forigen == D_BLANCA:
        # Se va a mover hacia arriba
        if fdestino == E_BLANCO:
            return (False, False)
        elif fdestino == D_BLANCA:
            return (False, False)
        # Comprobar que el destino es valido
        origen_f, origen_c = indiceCoordenada(origen)
        destino_f, destino_c = indiceCoordenada(destino)
        if destino_f == origen_f - 1 and (destino_c == origen_c - 1 or destino_c == origen_c + 1):
            return (True, False)
        elif destino_f == origen_f - 2 and (destino_c == origen_c - 2 or destino_c == origen_c + 2):
            # Comprobar direccion (izquierda o derecha)
            fichaIntermedia = 0
            if destino_c == origen_c - 2:
                fichaIntermedia = tablero[origen_f - 1][origen_c - 1]
                # Comprobar si la ficha es enemiga
                if fichaIntermedia == D_NEGRA:
                    tablero[origen_f - 1][origen_c - 1] = E_NEGRO
                    return (True, True)
            elif destino_c == origen_c + 2:
                fichaIntermedia = tablero[origen_f - 1][origen_c + 1]
                # Comprobar si la ficha es enemiga
                if fichaIntermedia == D_NEGRA:
                    tablero[origen_f - 1][origen_c + 1] = E_NEGRO
                    return (True, True)
            else:
                return (False, False)
        return (False, False)
    elif forigen == D_NEGRA:
        # Se va a mover hacia abajo
        if fdestino == E_BLANCO:
            return (False, False)
        elif fdestino == D_NEGRA:
            return (False, False)
        # Comprobar que el destino es valido
        origen_f, origen_c = indiceCoordenada(origen)
        destino_f, destino_c = indiceCoordenada(destino)
        if destino_f == origen_f + 1 and (destino_c == origen_c - 1 or destino_c == origen_c + 1):
            return (True, False)
        elif destino_f == origen_f + 2 and (destino_c == origen_c - 2 or destino_c == origen_c + 2):
            # Comprobar direccion (izquierda o derecha)
            fichaIntermedia = 0
            if destino_c == origen_c - 2:
                fichaIntermedia = tablero[origen_f + 1][origen_c - 1]
                # Comprobar si la ficha es enemiga
                if fichaIntermedia == D_BLANCA:
                    tablero[origen_f + 1][origen_c - 1] = E_NEGRO
                    return (True, True)
            elif destino_c == origen_c + 2:
                fichaIntermedia = tablero[origen_f + 1][origen_c + 1]
                # Comprobar si la ficha es enemiga
                if fichaIntermedia == D_BLANCA:
                    tablero[origen_f + 1][origen_c + 1] = E_NEGRO
                    return (True, True)
            else:
                return (False, False)
        return (False, False)
    return (False, False)
