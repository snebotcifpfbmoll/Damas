#!/usr/bin/env python3
from util import *
from coordenadas import *

def mover(origen, destino, tablero):
    org_1, org_2 = indiceCoordenada(origen)
    dst_1, dst_2 = indiceCoordenada(destino)
    tablero[dst_1][dst_2] = tablero[org_1][org_2]
    tablero[org_1][org_2] = E_NEGRO
