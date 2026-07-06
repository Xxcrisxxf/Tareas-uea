from Modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, disponible: bool, tipo_bebida: str, tamano: str):
        # Enviamos los atributos comunes al padre Producto
        super().__init__(nombre, precio, disponible)
        self.tipo_bebida = tipo_bebida
        self.tamano = tamano

    #aplicamos Polimorfismo
    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tipo de Bebida: {self.tipo_bebida} | Tamaño: {self.tamano}"