class Camara:
    def __init__(self,queso,maduracion):
        self.__queso = queso
        self.__maduracion = maduracion
        
    def produccion(self):
        print(f"En proceso de maduracion: Quesos {self.__queso} ")
        print(f"Condiciones de camara: {self.__maduracion}")