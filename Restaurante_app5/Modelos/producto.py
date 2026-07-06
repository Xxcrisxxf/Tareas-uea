class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.__precio = precio  #  encapsulamiento


    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor a cero.")

    # Método  para motrar la información
    def mostrar_informacion(self) -> str:
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f}"