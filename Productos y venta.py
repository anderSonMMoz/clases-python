CantProductos = int(input("Ingrese la cantidad de productos: "))
Productos = {}
for i in range(CantProductos):
    NombreProducto = input(f"Ingrese el nombre del producto {i+1}: ")
    PrecioProducto = float(input(f"Ingrese el precio del producto {i+1}: "))
    Productos[NombreProducto] = PrecioProducto
print("Lista de productos y sus precios:")
for Nombre, Precio in Productos.items():
    print(f"{Nombre}: ${Precio}")
