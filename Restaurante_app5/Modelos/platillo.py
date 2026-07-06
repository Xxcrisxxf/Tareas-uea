from Modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio: float, tipo_platillo: str, calorias: int):
        # Enviamos los atributos comunes al padre Producto
        super().__init__(nombre, precio)
        self.tipo_platillo = tipo_platillo
        self.calorias = calorias

    #aplicamos Polimorfismo
    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tipo: {self.tipo_platillo} | Calorías: {self.calorias} kcal"