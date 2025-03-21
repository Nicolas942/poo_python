# Definimos la primera clase base
class VehiculoElectrico:
    def __init__(self, autonomia):
        self.autonomia = autonomia
    
    def cargar_bateria(self):
        print("Batería cargada al 100%")

# Definimos la segunda clase base
class VehiculoCombustible:
    def __init__(self, capacidad_tanque):
        self.capacidad_tanque = capacidad_tanque
    
    def llenar_tanque(self):
        print("Tanque lleno")

# Clase que hereda de ambas
class VehiculoHibrido(VehiculoElectrico, VehiculoCombustible):
    def __init__(self, autonomia, capacidad_tanque):
        VehiculoElectrico.__init__(self, autonomia)  # Inicializa atributos de VehiculoElectrico
        VehiculoCombustible.__init__(self, capacidad_tanque)  # Inicializa atributos de VehiculoCombustible

    def mostrar_info(self):
        print(f"Autonomía eléctrica: {self.autonomia} km")
        print(f"Capacidad del tanque: {self.capacidad_tanque} litros")

# Uso del objeto
hibrido = VehiculoHibrido(autonomia=100, capacidad_tanque=40)
hibrido.mostrar_info()
hibrido.cargar_bateria()
hibrido.llenar_tanque()
