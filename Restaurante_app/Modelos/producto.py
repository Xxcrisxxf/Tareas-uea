class Producto:
    #Constructor para los productos
    def __init__(self , nombre:str , precio:float, bebida:str, disponible:bool,num_mesa:int ):
        self.nombre = nombre
        self.precio = precio
        self.bebida = bebida
        self.disponible = disponible
        self.num_mesa = num_mesa
    #Creamos un metodo  especial para representar la clase como texto
    def __str__(self):
        return f"Producto : {self.nombre} / Precio : {self.precio} / Bebida : {self.bebida} \n Se encuentra disponible ? : {self.disponible} \n Numero de mesa : {self.num_mesa}"