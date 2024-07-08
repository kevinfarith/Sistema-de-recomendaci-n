class Menu:

    def __init__(self, nombre_producto, categoria, precio, ventas):
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.precio = precio
        self.ventas = ventas
        self.siguiente = None

class Recomendacion:

    def __init__ (self):
        self.cabeza = None

    def ListaVacia(self):
        return self.cabeza is None

    def contar_elementos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def ImprimirElementos(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.data, end=" ")
            actual = actual.siguiente

    def Agregar(self,nombreProducto, categoria, precio, ventas):
        nuevo_nodo = Menu(nombreProducto, categoria, precio, ventas)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return 
        
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            
    def buscarElemento(self, nombreProducto):
        actual = self.cabeza
        while actual:
            if actual.data == nombreProducto:
                return True
            actual = actual.siguiente
        return False

    

    def MasVendido(self, n=5):
        productos = []
        actual = self.cabeza

        while actual:
            productos.append(actual)
            actual = actual.siguiente

        productos.sort(key=lambda x: x.ventas, reverse=True)
        top_n_productos = productos[:n]

        print("\nRecomendaciones del mes: \n")
        for producto in top_n_productos:
            print(f" {producto.categoria} {producto.nombre_producto}, ${producto.precio}")






#=========================================================================================

Comida = Recomendacion()

Comida.Agregar("Clasica", "Hamburguesa", 12000, 19)
Comida.Agregar("Doble Carne", "Hamburguesa", 16000, 3)
Comida.Agregar("De Pollo", "Hamburguesa", 14000, 12)
Comida.Agregar("Especial", "Hamburguesa", 20000, 14)
Comida.Agregar("Sencillo", "Perros Calientes", 12000, 10)
Comida.Agregar("Americano", "Perros Calientes", 14500, 15)
Comida.Agregar("Extra Bacon", "Perros Calientes", 17000, 27)
Comida.Agregar("Mexicana", "Pizza", 9000, 6)
Comida.Agregar("Hawaiana", "Pizza", 9000, 8)
Comida.Agregar("Pollo Champiñon", "Pizza", 9000, 9)

Comida.MasVendido(5)
