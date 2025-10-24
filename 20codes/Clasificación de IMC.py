peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc <= 24.9:
    print("Normal")
elif imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
print("IMC:", imc)
