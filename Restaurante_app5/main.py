from Modelos.platillo import Platillo
from Modelos.bebidas import Bebida
from Servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("========================================")
    print("1. Registrar Platillo ")
    print("2. Registrar Bebida")
    print("3. Mostrar Menú Completo")
    print("4. Salir")
    print("========================================")

def registrar_platillo(restaurante):
    print("\n=== REGISTRAR PLATILLO ===")
    nombre = input("Nombre del plato: ")
    try:
        precio = float(input("Precio: $"))
        tipo_platillo = input("Tipo de plato (ej: Entrada, segundo): ")
        calorias = int(input("Número de calorías (kcal): "))

        # Instanciamos la clase hija Platillo pasando las variables correctamente
        platillo = Platillo(
            nombre=nombre,
            precio=precio,
            tipo_platillo=tipo_platillo,
            calorias=calorias
        )
        restaurante.agregar_producto(platillo)
        print(f"\nPlatillo {nombre} registrado con exito")
    except ValueError:
        print("\nError: El precio debe ser un numero decimal y las calorias un numero entero.")

def registrar_bebida(restaurante):
    print("\n=== REGISTRAR BEBIDA ===")
    nombre = input("Nombre de la bebida: ")
    try:
        precio = float(input("Precio: $"))
        tipo_bebida = input("Tipo de bebida (ej: Natural, Gaseosa): ")
        tamano = input("Tamaño (ej: Grande, Mediano): ")

        # Instanciamos la clase hija Bebida pasando las variables correctamente
        bebida = Bebida(
            nombre=nombre,
            precio=precio,
            tipo_bebida=tipo_bebida,
            tamano=tamano
        )
        restaurante.agregar_producto(bebida)
        print(f"\n¡Bebida {nombre} registrada con exito")
    except ValueError:
        print("\nError: El precio debe ser un numero decimal.")

def main():
    mi_restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_platillo(mi_restaurante)
        elif opcion == "2":
            registrar_bebida(mi_restaurante)
        elif opcion == "3":
            mi_restaurante.mostrar_informacion()
        elif opcion == "4":
            print("\nSistema cerrado.")
            break
        else:
            print("\nOpcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    main()