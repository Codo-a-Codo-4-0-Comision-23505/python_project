from funciones.utils import calcularArea
import sys

def main() -> int:
    """Este la funcion principal main

    Returns:
        int: si devuelve 0 el programa termino bien..
    """
    isRunning = True
    calcularArea(10,35)

    contador = 0

    while isRunning:
        print("Hello World")

        if contador >= 10:
            isRunning = False

        print(contador)
        contador += 1

    return 0
        

# Esta linea dice "si estoy ejecutando python como una app arranco por aca"
if __name__ == '__main__':
    sys.exit(main())