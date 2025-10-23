angulo = float(input("Ingrese el valor del ángulo en grados: "))
if angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif 90 < angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
    print("El ángulo es llano.")
else:  
    print("El valor ingresado no es un ángulo válido.")