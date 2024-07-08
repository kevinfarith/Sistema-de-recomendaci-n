class Menu:

    def __init__(self, nombre_producto, categoria, precio, ventas):
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.precio = precio
        self.ventas = ventas
        self.izquierda = None
        self.derecha = None

    def __repr__(self):
        return f"{self.categoria} {self.nombre_producto}, ${self.precio}"


class Arbol:

    def __init__(self):
        self.raiz = None

    def agregar_recursivo(self, nodo, producto):
        if producto.ventas < nodo.ventas:
            if nodo.izquierda is None:
                nodo.izquierda = producto
            else:
                self.agregar_recursivo(nodo.izquierda, producto)
        else:
            if nodo.derecha is None:
                nodo.derecha = producto
            else:
                self.agregar_recursivo(nodo.derecha, producto)

    def __inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo)
            self.__inorden_recursivo(nodo.derecha, resultado)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.ventas == busqueda:
            return nodo
        if busqueda < nodo.ventas:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, producto):
        if not self.raiz:
            self.raiz = producto
        else:
            self.agregar_recursivo(self.raiz, producto)

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

    def Recomendados(self, n):
        productos = []
        self.__inorden_recursivo(self.raiz, productos)
        productos.sort(key=lambda x: x.ventas, reverse=True)
        return productos[:n]


#=========================================================================================

comida = Arbol()

comida.agregar(Menu("Clasica", "Hamburguesa", 12000, 19))
comida.agregar(Menu("Doble Carne", "Hamburguesa", 16000, 3))
comida.agregar(Menu("De Pollo", "Hamburguesa", 14000, 12))
comida.agregar(Menu("Especial", "Hamburguesa", 20000, 14))
comida.agregar(Menu("Sencillo", "Perros Calientes", 12000, 50))
comida.agregar(Menu("Americano", "Perros Calientes", 14500, 15))
comida.agregar(Menu("Extra Bacon", "Perros Calientes", 17000, 27))
comida.agregar(Menu("Mexicana", "Pizza", 9000, 6))
comida.agregar(Menu("Hawaiana", "Pizza", 9000, 8))
comida.agregar(Menu("Pollo Champiñon", "Pizza", 9000, 9))

print("\nProductos recomendados:")
for producto in comida.Recomendados(5):
    print(producto)