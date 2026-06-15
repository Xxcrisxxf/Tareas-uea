def registrar_mascota():
    raza = input("Raza de su mascota: ")
    nombre = input("Nombre de su mascota: ")
    edad = input("Edad de su mascota: ")
    return raza, nombre, edad
def mostrar_info(raza, nombre, edad):
    print("       INFORMACIÓN DE LA MASCOTA       ")
    print(f"Nombre : {nombre}")
    print(f"Raza   : {raza}")
    print(f"Edad   : {edad}")
    print("=======================================")


raza, nombre, edad = registrar_mascota()
mostrar_info(raza, nombre, edad)