salario = float(input("Ingrese su salario mensual: "))
if salario < 10000:
    impuesto = 0
elif 10000 <= salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20
salario_neto = salario - impuesto
print(f"El impuesto aplicado es: {impuesto}")
print(f"El salario neto después de impuestos es: {salario_neto}")

