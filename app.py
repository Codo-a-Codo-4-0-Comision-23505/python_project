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

    frase = "HOla mundo en el 6 de noviembre" #Esto es un array de caracteres...

    print(frase) # Esto imprime la frase completa
    print(frase[0]) # Esto imprime la letra H
    print(frase[0:4]) # Estamos sacando solo el HOla
    print(frase[5:10]) #Mostramos la segunda la palabra
    print(frase[10:])
    print(frase[:10])
    print(frase[:5] + "World" + frase[10:])
    print(frase[::2]) # 
    print(frase[:5:-1]) #Imprime al reves
    print(frase.replace("mundo", "world"))
    
    print(list(frase))

    frase2 = ['h', 'o', 'l', 'a']
    print(frase2)
    print(str(frase2))

    diccionario = {'Juan': 56, 'Ana': 15}
    print(diccionario)
    
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