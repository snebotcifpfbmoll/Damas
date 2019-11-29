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
        return comprobacion
    if tablero[origenC][origenF]== D_NEGRA and tablero[destinoC][destinoF]==D_BLANCA :
        comprobacion=True
        return comprobacion


def comprobarMovimiento(origen,destino,tablero):
    origenC, origenF = indiceCoordenada(origen)
    destinoC, destinoF = indiceCoordenada(destino)

    if tablero[origenC,origenF]==3:
        if destinoC==(origenC+2):
            fichaIntermediaC=(destinoC-1)
            fichaIntermediaF=(destinoF+1)
            fichaIntermedia=(fichaIntermediaC,fichaIntermediaF)
            comprobacion=comprobarColor(origen,fichaIntermedia,tablero)
            if comprobacion==True:
                mover(origen,destino,tablero)
            else:
                print('No se puede mover')

        if destinoC==(origenC-2):
            fichaIntermediaC=(destinoC+1)
            fichaIntermediaF=(destinoF+1)
            comprobacion=comprobarColor(origen,fichaIntermedia,tablero)
            if comprobacion==True:
                mover(origen,destino,tablero)
            else:
                print('No se puede mover')

    if tablero[origenC,origenF]==2:
        if destinoC==(origenC+2):
            fichaIntermediaC=(destinoC-1)
            fichaIntermediaF=(destinoF-1)
            fichaIntermedia=(fichaIntermediaC,fichaIntermediaF)
            comprobacion=comprobarColor(origen,fichaIntermedia,tablero)
            if comprobacion==True:
                mover(origen,destino,tablero)
            else:
                print('No se puede mover')

        if destinoC==(origenC-2):
            fichaIntermediaC=(destinoC+1)
            fichaIntermediaF=(destinoF-1)
            comprobacion=comprobarColor(origen,fichaIntermedia,tablero)
            if comprobacion==True:
                mover(origen,destino,tablero)
            else:
                print('No se puede mover')



