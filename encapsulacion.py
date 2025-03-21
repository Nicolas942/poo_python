# composición 

""""Una coordenada en dos dimenciones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje de la y, esto podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que son los cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada.
"""

#clase coordenada

class Coordenada:
    #METODO CONSTRUCTOR
    def __init__(self, x, y):
        #atributos privados
        self.__X = x
        self.__Y = y


    # metodos de lectura y escritura de cada atributo
    def __getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def setX(self, x):
        self.__X = x

    def setY(self, y):
        self.__Y = y

    # metodo para mostrar coordenada
    def MostrarCoordenada(self):
        print("(",self.__X, ",", self.__Y, ")")

# Clase cuadrado 
class Cuadrado:
    #metodo constructor
    def __init__(self, v1,v2,v3,v4):
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # metodos privados para mostrar vertices
    def __MostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), "," , self.__V1.getY(), ")")

    def __MostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), "," , self.__V2.getY(), ")")

    def __MostrarCoordenadaV3(self):
        print("(", self.__V3.getX(), "," , self.__V3.getY(), ")")

    def __MostrarCoordenadaV4(self):
        print("(", self.__V4.getX(), "," , self.__V4.getY(), ")")

    # metodo para mostrar los vertices
    def MostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.__MostrarCoordenadaV1()
        self.__MostrarCoordenadaV2()
        self.__MostrarCoordenadaV3()
        self.__MostrarCoordenadaV4()

# Metodo Principal
def main():
    #input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    c1 = Coordenada(x1,x2)
    c1.MostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    Cuadrado1 = Cuadrado(v1,v2,v3,v4)
    Cuadrado1.MostrarVertices()

coordenada = Coordenada(3,4)
print("(",coordenada.__getX() , "," , coordenada.getY(), ")")

if __name__ == "__main__":
    main()
