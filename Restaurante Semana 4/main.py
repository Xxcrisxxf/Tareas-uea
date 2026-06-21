#importamos todas las clases a main
from Modelos.producto import Producto
from Modelos.cliente import Cliente
from Servicios.restaurante import Restaurante

mi_restaurante = Restaurante()


# Creamos un plato
plato1 = Producto("Maito de Pescado", 7.50, "Agua")
# Creamos otro plato o bebida
plato2 = Producto("Chicha de Chonta", 1.50,"café")

# Creo un cliente
cliente1 = Cliente("Cristian")

#Se muestra toda la informacion en la consola 
mi_restaurante.agregar_producto(plato1)
mi_restaurante.agregar_producto(plato2)

mi_restaurante.agregar_cliente(cliente1)

mi_restaurante.mostrar_informacion()