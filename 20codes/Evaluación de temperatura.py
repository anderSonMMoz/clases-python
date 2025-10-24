temp = float(input("Temperatura en Grados celcius (C°): "))

if temp < 0:
    print("Hace mucho frío")
elif temp <= 20:
    print("Clima fresco")
elif temp <= 30:
    print("Clima agradable")
else:
    print("Hace mucho calor")
