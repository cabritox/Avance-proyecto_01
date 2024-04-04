#Creacion de la clase objeto 'Camara'
class Camara:
    def __init__(self,queso,maduracion):
        #Definiendo atributos privados
        self.__queso = queso
        self.__maduracion = maduracion

    #Metodo de simulacion de 'camara de maduracion'
    def produccion(self):
        print(f"En proceso de maduracion: Quesos {self.__queso} ")
        print(f"Condiciones de camara: {self.__maduracion}")
