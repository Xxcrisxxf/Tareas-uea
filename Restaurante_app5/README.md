Nombre : CRISTIAN JAIR BRAVO CHIMBORAZO
El sistema restaurante es una aplicación interactiva por consola diseñada para gestionar de manera eficiente el menú de un establecimiento gastronómico. Permite registrar de manera dinámica productos clasificados en comidas  y bebidas, almacenándolos en una lista centralizada para su posterior visualización en un formato legible y estructurado.

├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── platillo.py
│   │   └── bebida.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md
Se aplica una jerarquía lógica donde la clase base Producto centraliza los atributos comunes del menú (nombre, precio, disponible), mientras que las clases hijas Platillo y Bebida heredan automáticamente estas propiedades usando el constructor super().__init__().

El atributo financiero __precio se encuentra protegido bajo un encapsulamiento estricto en la clase padre mediante el uso de un doble guion bajo, lo que restringe e impide su manipulación directa desde el exterior del objeto.

El polimorfismo se evidencia mediante la sobreescritura  del método mostrar_informacion(). La clase padre Producto define una estructura base para este método. Posteriormente, tanto Platillo como Bebida redefinen el método para incorporar sus propios detalles particulares.

La Programación Orientada a Objetos combinada con una arquitectura modular es fundamental en el desarrollo de software moderno porque transforma el código caótico en un sistema escalable, legible y fácil de mantener. Al compartimentar el software en paquetes y clases con responsabilidades únicas, se reduce drásticamente el acoplamiento; por ejemplo, modificar las propiedades de una bebida no altera en absoluto el funcionamiento del menú principal o del platillo.