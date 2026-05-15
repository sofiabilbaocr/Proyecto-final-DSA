# Proyecto-final-DSA
Repo del proyecto final de la clase de DSA, double stack
Sofia Bilbao 20250048
Dhidel Osorio 20250642

## Descripción del proyecto

Este proyecto simula un reproductor de música usando una estructura de datos de double stack. El usuario puede agregar canciones, avanzar a la siguiente pista y retroceder a la anterior. La interfaz muestra en todo momento el estado de ambos stacks y la canción que está sonando.

## Estructura de datos (Double Stack)

El double stack consiste en dos stacks lógicos que comparten un mismo array de tamaño fijo, creciendo desde extremos opuestos.
- Stack_prev: almacena las canciones ya reproducidas. Su tope (top_prev) empieza en -1 y crece hacia la derecha.
- Stack_next: almacena las canciones por reproducir. Su tope (top_next) empieza en size y crece hacia la izquierda.
- Cuando top_prev + 1 == top_next: el array está lleno (Stack Overflow).

### Métodos y complejidad temporal

Todos los métodos son O(1) porque operan directamente sobre índices, sin recorrer el array.

push_prev(song): Agrega una canción al stack de anteriores (O(1))
pop_prev(): Saca la canción más reciente de anteriores (O(1))
peek_prev(): Consulta la canción más reciente de anteriores sin sacarla (O(1))
push_next(song): Agrega una canción al stack de siguientes (O(1))
pop_next(): Saca la canción más cercana de siguientes (O(1))
peek_next(): Consulta la canción más cercana de siguientes sin sacarla (O(1))

Complejidad espacial
O(n) donde n es el tamaño del array. La ventaja del double stack es que los dos stacks comparten ese mismo O(n), en vez de usar O(2n) con dos arrays separados.


## Funcionalidades del reproductor

1. Agregar canción: Agrega una nueva canción al stack de siguientes
2. Siguiente: Avanza a la siguiente canción, la actual pasa a anteriores
3. Anterior: Retrocede a la canción anterior, la actual regresa a siguientes
4. Ver siguiente: Muestra cuál es la próxima canción sin avanzar
5. Ver anterior: Muestra cuál fue la última canción sin retroceder



## Instrucciones para ejecutar el proyecto


### 1. Clonar el repositorio
git clone https://github.com/sofiabilbaocr/Proyecto-final-DSA.git

### 2. Dependencias
Debes tener instalado flask. Si no lo tienes instalalo con este código en la terminal:
pip install flask

### 3. Correr la interfaz
Aplicar el sigueinte código en la terminal estando en la ruta /Proyecto-final-DSA:
    python app.py (Importante que sea en la terminal y no con "Go live" o parecidos.)

### 4. Link
Copiar y pegar el link dado en el navegador. Esto correra la aplicación web con todas sus funcionalidades de manera local

### 5. Probar Unit testing
Aplicar el siguiente código en la terminal estando en la ruta /Proyecto-final-DSA:
    python -m unittest -v .\Unit_testing.py
    Este código muestra de manera detallada cada uno de los escenarios.
