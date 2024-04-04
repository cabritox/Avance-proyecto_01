"""

"""
class Maduracion:
    def __init__(self,queso,humedad,temperatura):
        self.__queso = queso
        self.__humedad = humedad
        self.__temperatura = temperatura
        
    def queso(self):
        print(self.__queso)
        
    def elaboracion(self,queso):
        if queso == "Blandos" or queso == "Cremoso":
            if 10<= self.__temperatura <= 14 and 85 <= self.__humedad <= 90 :
                return f"Temperatura y humedad adecuada"
            else:
                return "Temperatura o humedad inadecuada"
            
        elif queso == "Semi duros" or queso == "Duros":
            if 12 <=self.__temperatura <= 16 and 80 <= self.__humedad <= 85 :
                return f"Temperatura y humedad adecuada"
            else:
                return "Temperatura o humedad inadecuada"
        else:
            return "No encontrado en inventario"
         