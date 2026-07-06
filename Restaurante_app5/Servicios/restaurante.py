from Modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.productos = []  # Lista de los productos del restaurante
        
    def mostrar_informacion(self):
    # Recorre la lista ejecutando mostrar_informacion() 
        print("\n==== Menú del Restaurante ====")
        if not self.productos:
            print("No hay productos registrados aún.")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    # Agrega un platillo o bebida a la lista general
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)