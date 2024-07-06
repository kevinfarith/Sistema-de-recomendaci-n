import networkx as nx
import random

class Producto:
    def __init__(self, id_producto, nombre):
        self.id_producto = id_producto
        self.nombre = nombre

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

class SistemaRecomendacion:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_producto(self, producto):
        self.grafo.add_node(producto.id_producto, tipo='producto', nombre=producto.nombre)

    def agregar_usuario(self, usuario):
        self.grafo.add_node(usuario.id_usuario, tipo='usuario', nombre=usuario.nombre)

    def agregar_preferencia(self, id_usuario, id_producto):
        if self.grafo.nodes[id_usuario]['tipo'] == 'usuario' and self.grafo.nodes[id_producto]['tipo'] == 'producto':
            self.grafo.add_edge(id_usuario, id_producto, tipo='preferencia')

    def eliminar_producto(self, id_producto):
        if self.grafo.nodes[id_producto]['tipo'] == 'producto':
            self.grafo.remove_node(id_producto)

    def eliminar_usuario(self, id_usuario):
        if self.grafo.nodes[id_usuario]['tipo'] == 'usuario':
            self.grafo.remove_node(id_usuario)

    def eliminar_preferencia(self, id_usuario, id_producto):
        if self.grafo.has_edge(id_usuario, id_producto):
            self.grafo.remove_edge(id_usuario, id_producto)

    def obtener_recomendaciones(self, id_usuario, top_n=5):
        if self.grafo.nodes[id_usuario]['tipo'] != 'usuario':
            return []

        productos_usuario = set(self.grafo.neighbors(id_usuario))
        usuarios_similares = set()
        for producto in productos_usuario:
            for otro_usuario in self.grafo.neighbors(producto):
                if otro_usuario != id_usuario:
                    usuarios_similares.add(otro_usuario)

        recomendaciones = set()
        for otro_usuario in usuarios_similares:
            for producto in self.grafo.neighbors(otro_usuario):
                if producto not in productos_usuario:
                    recomendaciones.add(producto)

        return list(recomendaciones)[:top_n]

# Crear el sistema de recomendación
sistema_rec = SistemaRecomendacion()

# Datos simulados
datos_productos = [
    {'id_producto': 'p1', 'nombre': 'Laptop'},
    {'id_producto': 'p2', 'nombre': 'Smartphone'},
    {'id_producto': 'p3', 'nombre': 'Auriculares'},
    {'id_producto': 'p4', 'nombre': 'Monitor'},
    {'id_producto': 'p5', 'nombre': 'Teclado'}
]

datos_usuarios = [
    {'id_usuario': 'u1', 'nombre': 'Alicia'},
    {'id_usuario': 'u2', 'nombre': 'Bob'},
    {'id_usuario': 'u3', 'nombre': 'Carlos'},
    {'id_usuario': 'u4', 'nombre': 'David'},
    {'id_usuario': 'u5', 'nombre': 'Eva'}
]

datos_preferencias = [
    {'id_usuario': 'u1', 'id_productos': ['p1', 'p2', 'p3']},
    {'id_usuario': 'u2', 'id_productos': ['p2', 'p3', 'p4']},
    {'id_usuario': 'u3', 'id_productos': ['p1', 'p4', 'p5']},
    {'id_usuario': 'u4', 'id_productos': ['p1', 'p3', 'p5']},
    {'id_usuario': 'u5', 'id_productos': ['p2', 'p4', 'p5']}
]

# Agregar productos
for datos_producto in datos_productos:
    producto = Producto(datos_producto['id_producto'], datos_producto['nombre'])
    sistema_rec.agregar_producto(producto)

# Agregar usuarios 
for datos_usuario in datos_usuarios:
    usuario = Usuario(datos_usuario['id_usuario'], datos_usuario['nombre'])
    sistema_rec.agregar_usuario(usuario)

# Agregar preferencias
for preferencia in datos_preferencias:
    id_usuario = preferencia['id_usuario']
    for id_producto in preferencia['id_productos']:
        sistema_rec.agregar_preferencia(id_usuario, id_producto)

# Mostrar las recomendaciones para cada usuario
for datos_usuario in datos_usuarios:
    id_usuario = datos_usuario['id_usuario']
    recomendaciones = sistema_rec.obtener_recomendaciones(id_usuario)
    productos_recomendados = [sistema_rec.grafo.nodes[id_producto]['nombre'] for id_producto in recomendaciones]
    print(f"Recomendaciones para {datos_usuario['nombre']}: {productos_recomendados}")
