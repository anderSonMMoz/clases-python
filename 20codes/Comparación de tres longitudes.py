Num1 = float(input("Longitud 1: "))
Num2 = float(input("Longitud 2: "))
Num3 = float(input("Longitud 3: "))

if Num1 + Num2 > Num3 and Num1 + Num3 > Num2 and Num2 + Num3 > Num1:
    print("Pueden formar un triángulo")
else:
    print("No pueden formar un triángulo")
