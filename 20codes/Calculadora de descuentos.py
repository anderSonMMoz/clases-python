precio = float(input("Precio del producto: "))

if precio < 50:
    descuento = 0
elif precio <= 100:
    descuento = 0.05
else:
    descuento = 0.10

total = precio - (precio * descuento)
print("Precio final:", total)
