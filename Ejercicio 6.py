#JUEGO 

#hacer que un oponente que quite puntos a los jugadores
#hacer que uno de los dos jugadores pueda dar puntos si asi lo desea 


class Juego:
    def __init__(self):
        self.__puntuacion = 0 

    def get_puntuacion(self):
        return self.__puntuacion

    
    def añadir_puntos(self, puntos):
        if puntos > 0:
            self.__puntuacion += puntos
            print(f" Se añadieron {puntos} puntos. Puntuación actual: {self.__puntuacion}")
        else:
            print(" No se pueden añadir puntos negativos o cero.")

    
    def restar_puntos(self, puntos):
        if puntos > 0:
            if self.__puntuacion - puntos >= 0:
                self.__puntuacion -= puntos
                print(f" Se restaron {puntos} puntos. Puntuación actual: {self.__puntuacion}")
            else:
                print("No se puede restar más de la puntuación actual.")
        else:
            print("No se pueden restar puntos negativos o cero.")

    def mostrar_puntuacion(self):
        print(f"Puntuación actual: {self.__puntuacion}")

class jugador_1 (Juego):
    def __init__(self):
        super().__init__()

class jugador_2 (Juego):
    def __init__(self):
        super().__init__()


juego = Juego()


player_a = jugador_1
juego.añadir_puntos(1000)
juego.añadir_puntos(50)


juego.restar_puntos(25)


juego.restar_puntos(200)


juego.mostrar_puntuacion()

player_b = jugador_2
juego.añadir_puntos(2000)
juego.añadir_puntos(1500)


juego.restar_puntos(250)


juego.restar_puntos(200)

juego.mostrar_puntuacion()
