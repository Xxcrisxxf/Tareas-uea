class Producto:
    #Constructor para los productos
    def __init__(self , nombre , precio, bebida):
        self.nombre = nombre
        self.precio = precio
        self.bebida = bebida
    #Creamos un metodo  especial para representar la clase como texto
    def __str__(self):
        return f"Producto : {self.nombre} / Precio : {self.precio} / Bebida : {self.bebida}"