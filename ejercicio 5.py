# crear un methofo que identifique atraves de un listado con varios vehiculos, que tipo es cada vehhiculo 

# Crea una clase Vehiculo con atributos privados __velocidad_maxima y __marca. Agrega métodos get_marca() 
# y set_velocidad_maxima() que aseguren la integridad de los datos y limiten la velocidad máxima a 200. 

#Sergio Duarte
#Grupo: 2034

class Vehiculo:
    def __init__(self, marca, Vel_Max):
        self.__marca = marca

        if Vel_Max > 200 :
            print(f"El vehiculo sobrepasa la Velocidad Maxima, se reajuastara a 200 Km/h")
            self.__Vel_Max = 200
        else:
            Vel_Max <= 200
            print(f"El vehiculo no sobre pasa la Velocidad Maxima")
            self.__Vel_Max = Vel_Max
    
    def get_marca (self):
       return self.__marca

    def set_VelMax(self, nueva_VelMax):
        if 0 < nueva_VelMax < 200:
            self.__Vel_Max = nueva_VelMax
            print(f"Velocidad maxima ha sido corregida a : {self.__Vel_Max} km/h")

        else:
            print(f"La velocicdad debe estar en el rango de 1 - 200 Km/h")

    def mostrar_informacion(self):
        print(f"marca: {self.__marca} \. Vel_Max: {self.__Vel_Max} Km/h")

#Ejemplo
auto1 = Vehiculo("Ford explorer", 180)
auto1.mostrar_informacion()

auto1.set_VelMax(210)  # velocidad inválida
auto1.set_VelMax(190)  # velocidad válida
auto1.mostrar_informacion()

print("Marca del vehículo:", auto1.get_marca())
