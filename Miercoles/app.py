from Modelos import clase as c
from dao import operciones as o
from dao import persistencia as p

prod1 = c.productos("Cafe",100,2)
prod2 = c.productos("Helado",55,4)
prod3 = c.productos("Gaseosa",30,5)

carrito = o.ProductoDao()

mi_archivo = p.persistenciaDao("carrito.txt")
mi_archivo.abrir_archivo()

carrito.agregar(prod1)
carrito.agregar(prod2)
carrito.agregar(prod3)

for p in carrito.mostrar():
    print(p)

buscar = "Cafes"
print(f"Dato a buscar {buscar}")
datos = carrito.buscar_por_nombre(buscar)

for p in datos:
    print(p)
else:
    print("Registro no encontrado")

mi_archivo = p.persistenciaDao("carrito.txt")
for p in carrito.mostrar():
    mi_archivo.guardar_archivo(p)