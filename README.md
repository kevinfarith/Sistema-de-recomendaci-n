
# Sistema de recomendación de productos para restaurante de comida rápida

# *Resumen del Proyecto*

Este proyecto tiene como objetivo implementar un sistema de recomendación de productos para un restaurante de comida rápida. El sistema recomienda productos a los clientes basándose en las preferencias de usuarios similares, utilizando estructuras de datos como listas enlazadas, árboles binarios y grafos para mejorar la eficiencia y precisión de las recomendaciones.


# *Etapas del Desarrollo*

*Primera Entrega : Implementación de Listas Enlazadas*

En la primera etapa del proyecto, se estableció la base del sistema de recomendación utilizando listas enlazadas. Esta estructura de datos se seleccionó debido a su simplicidad y eficiencia en operaciones básicas de inserción y búsqueda. Las listas enlazadas se utilizaron para almacenar información detallada sobre los productos disponibles en el restaurante, incluyendo:

* Nombre: El nombre del producto.
* Categoría: La categoría a la que pertenece el producto (por ejemplo, hamburguesa, pizza, perro caliente, etc.).
* Precio: El precio del producto.
* Ventas: El número de ventas del producto, utilizado como indicador de popularidad.

Las funcionalidades desarrolladas en esta etapa incluyeron:

* Agregar productos a la lista: Permite la inclusión de nuevos productos en el menú del restaurante.
* Contar el número de productos: Proporciona el número total de productos disponibles.
* Buscar productos específicos: Facilita la búsqueda de productos particulares basándose en diferentes criterios.
* Recomendar los productos más vendidos: Sugiere productos a los usuarios basándose en las estadísticas de ventas.

*Segunda Entrega: Incorporación de Árboles Binarios*

En la segunda etapa del proyecto, se mejoró la estructura del sistema utilizando árboles binarios, una estructura de datos más avanzada que permite una organización jerárquica y eficiente de los productos. Los árboles binarios se utilizaron para representar la jerarquía de popularidad de los productos, lo que facilitó una búsqueda y recomendación más rápida y precisa. Las funcionalidades adicionales desarrolladas en esta etapa incluyeron:

* Insertar productos en el árbol: Permite agregar nuevos productos al árbol, manteniendo la estructura de datos ordenada.
* Eliminar productos del árbol: Facilita la eliminación de productos del árbol cuando ya no están disponibles o se desean retirar del menú.
* Buscar productos en el árbol: Proporciona una búsqueda eficiente de productos dentro del árbol, utilizando la estructura jerárquica para acelerar el proceso.

*Tercera Entrega: Implementación de Grafos*

En la tercera y última etapa del proyecto, se incorporaron grafos para modelar las relaciones entre usuarios y productos, permitiendo así recomendaciones basadas en las preferencias de usuarios similares. Esta estructura de datos avanzada permitió capturar relaciones complejas entre usuarios y productos, mejorando significativamente la precisión de las recomendaciones. Las funcionalidades desarrolladas en esta etapa incluyeron:

* Agregar productos y usuarios como nodos en el grafo: Representa tanto a los productos como a los usuarios como nodos en un grafo, facilitando la modelización de sus relaciones.
* Agregar preferencias como aristas en el grafo: Conecta usuarios y productos mediante aristas que representan las preferencias de los usuarios.
* Eliminar productos, usuarios y preferencias del grafo: Facilita la actualización dinámica del grafo, permitiendo agregar y eliminar nodos y aristas según sea necesario.
* Obtener recomendaciones basadas en usuarios similares: Utiliza algoritmos de análisis de grafos para identificar usuarios con preferencias similares y recomendar productos que ellos han preferido, pero que el usuario actual aún no ha probado.
