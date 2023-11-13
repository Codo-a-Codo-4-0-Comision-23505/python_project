# definimos la class persona
class Persona:   
    piernas = 2
    id = None
    #def constructor(self, id, nombre):
    def __init__(self, id, nombre) -> None: 
        self.id = id
        self.nombre = nombre

    def saltar(self):
        print("Estoy saltando... en " + str(self.piernas) + " piernas ")

    def __str__(self) -> str:
        #return "Soy una persona, llamada: " + self.nombre + " con " + str(self.piernas) + " piernas"
        return "{ 'nombre': '" + self.nombre + "'," + " 'piernas': " + str(self.piernas) + "}"

alumno1 = Persona(400000, "Ale") # ahora estamos obligados a contruirlo de esta forma..
#alumno1.constructor(400000, "Ale")
print(alumno1.piernas)
alumno1.saltar()
alumno1.piernas = 1
print(alumno1.nombre)
print(alumno1.id)

print(alumno1.piernas)
alumno1.saltar()

#a partir de aca TODAS las personas construidas tiene 4 piernas...
Persona.piernas = 4

alumno2 = Persona()
alumno2.constructor(100000, "Pepe")
print(alumno2.piernas)
alumno2.saltar()

print(alumno2)