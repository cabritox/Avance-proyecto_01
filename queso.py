
#Creacion de la clase Queso
class Queso:
    def __init__(self,queso):
        
        #Definiendo atributos privados
        self.__queso = queso
    
    #Metodo accedador al atributo 'queso'
    def get_queso(self):
        return self.__queso
        
        
