import sys

# Variable para comprobar que Windows es compatible con ANSI colors
windows_colors = False

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

# Solo funciona con Mac (Windows es una mierda)
def cambiarColor(string, color):
    if sys.platform == "win32" and windows_colors == False:
        try:
            import colorama
            colorama.init()
            windows_colors == True
        except:
            windows_colors = False
    if sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2" or windows_colors:
        # Comprobar que el color existe
        if color in colors:
            return ("%s%s%s" % (colors[color], string, colors["reset"]))
    return string
