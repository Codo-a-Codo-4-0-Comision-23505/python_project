from funciones.utils import calcularArea
x = 10
calcularArea(x,35)
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

unArray = [1, 3, 5, 7]
print(list(frase))
frase2 = ['h', 'o', 'l', 'a']
print(frase2)
print(str(frase2))
diccionario = {
    'Juan': 56,
    'Ana': 15
}
print(diccionario)
print(diccionario['Ana'])
## Esto que esta aca...
frase3=43 # tiene ID 1231313131
frase3=frase # ELIMINA 43
print(id(frase))
print(id(frase3))
print(id(10))
print(id(x))
print(id(10))

def printFrase():
    global frase
    frase = "Esto Es otra frase"
    print(frase)

printFrase()
print(frase)

cuadrado = lambda x :  x**2 # Equivalente a arrow functions de JavaScript
print(cuadrado(2))

listaNumeros = [ 23, 45, 67, 1]

listaNumerosx2 = list( map( lambda x: x * 2, listaNumeros) )

#[]
#for x in listaNumeros:
#    print(x*2)
#    listaNumerosx2.append(x*2)

print(listaNumerosx2)


listadePrecios = [ 1000, 2000, 2500, 50]

listadePreciosConIVA21 = list(map(lambda x: x * 1.21, listadePrecios))
listadePreciosConIVA10 = list(map(lambda x: x * 1.10, listadePrecios))
print(listadePreciosConIVA21)
print(listadePreciosConIVA10)