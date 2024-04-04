#Importaciones de las clases 'objeto'
from queso import Queso
from maduracion import Maduracion
from camara import Camara

#Presentacion del software
print("###################################################")
print("####### Proceso de conservacion de quesos #########")
print("###################################################")
print("Tipos de quesos disponibles a produccion:\nBlandos o Cremosos, Semi duros o Duros")#tipos de quesos a produccion
print("###################################################")

# Eleccion del tipo de queso
tipo_queso = input("\nElige un tipo de queso disponible: ")
queso = Queso(tipo_queso) #Queso a produccion


# Instrucciones del correcto proceso de maduracion, dependiendo del tipo de queso
print("\n########################################################################################")
print(f"###  Rangos de humedad y temperaturas obligatorias para quesos {queso.get_queso()}:  ###")
print("########################################################################################")
if queso == "Blandos" or "Cremosos":
    print("\nHumedad adecuada de 85% a 90%\nTemperatura adecuada de 10°C a 14°C")
elif queso == "Semi duros" or "Duros":
    print("Humedad adecuada de 80% a 85%\nTemperatura adecuada de 12°C a 16°C")
    
    
# Proceso de maduracion    
humedad = float(input("\nRango de humedad: "))
temperatura = float(input("Temperatura(en grados celius): "))
print("")
maduracion = Maduracion(queso.get_queso(),humedad,temperatura)


# Camara de maduracion
print("###################################################")
camara_01 = Camara(queso.get_queso(),maduracion.elaboracion(queso.get_queso()))
camara_01.produccion()
print("###################################################")

