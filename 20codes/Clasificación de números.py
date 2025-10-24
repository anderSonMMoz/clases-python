Num1 = float(input("Número 1: "))
Num2 = float(input("Número 2: "))
Num3 = float(input("Número 3: "))

if Num1 == 0 or Num2 == 0 or Num3 == 0:
    print("Hay ceros")
elif Num1 > 0 and Num2 > 0 and Num3 > 0:
    print("Todos positivos")
elif Num1 < 0 and Num2 < 0 and Num3 < 0:
    print("Todos negativos")
else:
    print("Mixtos")
