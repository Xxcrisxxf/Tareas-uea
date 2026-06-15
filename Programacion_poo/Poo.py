class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def mostrar_informacion(self):
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")

    def hacer_sonido(self):
        animal = self.especie.lower()
        
        if "perro" in animal:
            sonido = "¡Guau, guau!"
        elif "gato" in animal:
            sonido = "¡Miau, miau!"
        elif "loro" in animal or "pajaro" in animal:
            sonido = "¡Curi, curi! / ¡Quiii!"
        else:
            sonido = "*Sonido de mascota genérico*"
            
        print(f"{self.nombre} dice: {sonido}")