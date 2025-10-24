nota = float(input("Calificación (0-100): "))

if 90 <= nota <= 100:
    print("A")
elif 80 <= nota <= 89:
    print("B")
elif 70 <= nota <= 79:
    print("C")
elif 60 <= nota <= 69:
    print("D")
else:
    print("F")
