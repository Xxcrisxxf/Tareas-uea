class Cliente:
    #creamos un atributo con el nombre de nuestro cliente 
    def __init__(self,nombre):
        self.nombre = nombre
    #creamos otro metodo  especial para representar la clase como texto
    def __str__(self):
        return f"Cliente: {self.nombre}"