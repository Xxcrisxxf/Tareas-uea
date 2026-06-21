#importamos las clases producto y cliente para usarlos 
from Modelos.producto import Producto
from Modelos.cliente import Cliente
class Restaurante():
    #creamos un constructor para inicializar las listas de productos y clientes
    def __init__(self):
        self.producto = []
        self.cliente = []
    #Muesta la informacion en pantalla de nuestros productos    
    def mostrar_informacion (self):
        for producto in self.producto:
            print(producto)
        print("==== Clientes ====)")
    #Muesta a los clientes en pantalla
        for cliente in self.cliente:
            print(cliente)
    #agrgamos los prodcutos a una lista
    def agregar_producto (self, producto):
        self.producto.append(producto)
    #igualmente con los clientes los agregamos a una lista
    def agregar_cliente (self , cliente):
        self.cliente.append(cliente)