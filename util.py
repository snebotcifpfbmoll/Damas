#!/usr/bin/env python3

# Constantes comunes para el programa
E_BLANCO = 0
E_NEGRO = 1
D_NEGRA = 2
D_BLANCA = 3
D_REINA_NEGRA = 4
D_REINA_BLANCA = 5

# Obtener las dimensiones de la consola (windows no funciona)
def obtenerDimensiones():
    try:
        import fcntl, termios, struct
        th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
        return tw, th
    except:
        return 0, 0
