#Crea una clase Banco con un atributo privado _balance. Agrega métodos depositar() y retirar() 
# que verifiquen el acceso al balance de forma controlada. 

#se que hay cosas que no pidieron en el ejercicio pero pues quise agregarlas, espero
#no haya problema :D

class banco:
    def __init__(self, balance_inicial = 0):
        self._balance = balance_inicial

    def mostrar_balance (self):
        return f"tu balance es de : {self._balance}" 
    
    def depositar (self, cantidad):
        if cantidad > 0:
            self._balance += cantidad   
            return f" dinero depositado. nuevo balance: {self._balance}"
        else:
            return f"la cantidad a depositar debe ser positiva"

    def retirar (self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva."
        elif cantidad > self._balance:
            return "fondos insuficientes"
        else:
            self._balance -= cantidad
            return f"Retiro exitoso. nuevo balance: {self._balance}"
        


cuenta = banco (1000) #FONDO INCIAL

print(" Bienvenido a tu banco de confianza ")
print(cuenta.mostrar_balance())

monto_deposito = float(input("Cuanto dinero quieres depositar? "))
print(cuenta.depositar(monto_deposito))


#en caso de fondos insuficientes
while True:
    monto_retirar = float(input("¿Cuánto dinero deseas retirar? "))
    resultado = cuenta.retirar(monto_retirar)
    print(resultado)

    # Si el resultado indica que fue exitoso, salimos del ciclo
    if "Retiro exitoso" in resultado:
        break
    else:
        print("Por favor, ingrese una cantidad válida.\n")

print(cuenta.mostrar_balance())
