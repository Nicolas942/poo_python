# clase Persona

class Persona:

    #método constructor
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad

    #método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))
    
# método principal
def main():
    p1 = Persona("Nicolás", "Cabrera", 15)
    p1.MostrarPersona()
    p2 = Persona("Sofía", "Cabrera", 19)
    p2.MostrarPersona()
    p1.Edad = 20
    p1.MostrarPersona()


if __name__== "__main__":
    main()