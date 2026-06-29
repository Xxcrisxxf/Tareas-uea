#importamos todas las clases a main
from Modelos.producto import Producto
from Modelos.cliente import Cliente
from Servicios.restaurante import Restaurante

mi_restaurante = Restaurante()


# Creamos un plato
plato1 = Producto("Encebollado", 5, "Agua" , True ,13)
# Creamos otro plato o bebida
plato2 = Producto("Chaulafan", 3,"café",False , 3)

# Creo un cliente
cliente1 = Cliente("Cristian")

#Se muestra toda la informacion en la consola 
mi_restaurante.agregar_producto(plato1)
mi_restaurante.agregar_producto(plato2)

mi_restaurante.agregar_cliente(cliente1)

mi_restaurante.mostrar_informacion()