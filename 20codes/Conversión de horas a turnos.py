hora = int(input("Hora (0-23): "))

if 6 <= hora <= 11:
    print("Mañana")
elif 12 <= hora <= 17:
    print("Tarde")
elif 18 <= hora <= 23:
    print("Noche")
else:
    print("Madrugada")
