
# EJERCICIO 1

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print("Ejercicio 1:", asignaturas)



# EJERCICIO 2

print("\nEjercicio 2:")
for asignatura in asignaturas:
    print("Yo estudio", asignatura)



# EJERCICIO 3

print("\nEjercicio 3:")
notas = []

for asignatura in asignaturas:
    nota = input(f"¿Qué nota sacaste en {asignatura}? ")
    notas.append(nota)

for asignatura, nota in zip(asignaturas, notas):
    print(f"En {asignatura} has sacado {nota}")



# EJERCICIO 4

print("\nEjercicio 4:")
numeros = input("Introduce los números ganadores separados por espacios: ")
numeros = sorted([int(n) for n in numeros.split()])
print("Números ganadores ordenados:", numeros)



# EJERCICIO 5

print("\nEjercicio 5:")
numeros_1_10 = list(range(1, 11))
numeros_1_10.reverse()
print("Orden inverso:", *numeros_1_10, sep=",")



# EJERCICIO 6

print("\nEjercicio 6:")
repetir = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota sacaste en {asignatura}? "))
    if nota < 70:  # Cambia a <5 si usas escala 0-10
        repetir.append(asignatura)

print("Tienes que repetir:", repetir)



# EJERCICIO 7

print("\nEjercicio 7:")
abecedario = list("abcdefghijklmnopqrstuvwxyz")
resultado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]
print("Abecedario sin posiciones múltiplos de 3:", resultado)



# EJERCICIO 8

print("\nEjercicio 8:")
palabra = input("Introduce una palabra: ")

if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")



# EJERCICIO 9

print("\nEjercicio 9:")
palabra = input("Escribe una palabra: ").lower()
vocales = "aeiou"

for vocal in vocales:
    print(f"{vocal}: {palabra.count(vocal)}")



# EJERCICIO 10

print("\nEjercicio 10:")
precios = [50, 75, 46, 22, 80, 65, 8]
print("Menor precio:", min(precios))
print("Mayor precio:", max(precios))



# EJERCICIO 11

print("\nEjercicio 11:")
v1 = [1, 2, 3]
v2 = [-1, 0, 2]

producto_escalar = sum(a*b for a, b in zip(v1, v2))
print("Producto escalar:", producto_escalar)



# EJERCICIO 12

print("\nEjercicio 12:")
import math

numeros = input("Introduce números separados por comas: ")
lista = [float(n) for n in numeros.split(",")]

media = sum(lista) / len(lista)
desv = math.sqrt(sum((x - media)**2 for x in lista) / len(lista))

print("Media:", media)
print("Desviación típica:", desv)
