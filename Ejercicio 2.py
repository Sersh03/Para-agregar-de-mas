# agregar un metodo que identique por el precio del producto si es electrodomestico o juguete

class Producto:
    def __init__(self, precio):
        self.__precio = precio
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo")
    
    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje < 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
            print("Se aplicó el descuento correctamente")
        else:
            print("Descuento no aplicado")

class Electrodomesticos (Producto):
    def __init__(self, precio):
        super().__init__(precio)

    

    
productos = []

# para agregar uno o varios productos 
while True:
    try:
        p = int(input("¿Cuántos productos deseas agregar? "))
        break
    except ValueError:
        print("Por favor ingresa un número entero válido.\n")

for i in range(p):
    while True:
        try:
            precio = float(input(f"Ingrese el precio del producto #{i+1}: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número válido para el precio.")
    
    # Crear el objeto producto
    producto = Producto(precio)
    
    # aplicar descuento dependiendo del precio
    if precio > 50000:
        producto.aplicar_descuento(25)
        print(f"Se aplicó 25% de descuento. Nuevo precio : {producto.get_precio():.2f}")
    elif 25000 <= precio <= 50000:
        producto.aplicar_descuento(5)
        print(f"Se aplicó 5% de descuento. Nuevo precio : {producto.get_precio():.2f}")
    else:
        print("No aplica descuento.")
    
    productos.append(producto)

# mostrar resultados finales
print("\nLista de productos finales con precio actualizado:")
for i, p in enumerate(productos, start=1):
