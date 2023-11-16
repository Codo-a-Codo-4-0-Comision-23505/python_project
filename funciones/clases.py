# definimos la class persona
class Persona:   
    piernas = 2
    #def constructor(self, id, nombre):
    def __init__(self, id, nombre, money) -> None: 
        self.__id = id
        self.nombre = nombre
        self.__money = money # atributo privado

    #Salvo que expresamente la clase permita devolver informacion privada..
    def cuantaMoney(self):
        return self.__money
    
    #Esto solo modifica
    def tenesMoney(self, money):
        if money > 0:   
           self.__money = money

    def saltar(self):
        print("Estoy saltando... en " + str(self.piernas) + " piernas ")

    @property
    def json(self) -> str:
        return "{ 'nombre': '" + self.nombre + "'," + " 'piernas': " + str(self.piernas) + "}"

    def __str__(self) -> str:
        #return "Soy una persona, llamada: " + self.nombre + " con " + str(self.piernas) + " piernas"
        return "{ 'nombre': '" + self.nombre + "'," + " 'piernas': " + str(self.piernas) + "}"

alumno1 = Persona(400000, "Ale", 100) # ahora estamos obligados a contruirlo de esta forma..
#alumno1.constructor(400000, "Ale")
print(alumno1.piernas)
alumno1.saltar()
alumno1.piernas = 1
print(alumno1.nombre)
#print(alumno1.id)
print(alumno1.piernas)
print(alumno1.cuantaMoney()) # se cuanta plata tiene...
alumno1.tenesMoney(40)
print(alumno1.cuantaMoney()) # se cuanta plata tiene...
alumno1.saltar()
self = "yomismo"

print(alumno1.json)

#a partir de aca TODAS las personas construidas tiene 4 piernas...
Persona.piernas = 4

alumno2 = Persona(100000, "Pepe", 50)
print(alumno2.piernas)
alumno2.saltar()

print(alumno2)