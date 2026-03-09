nombre = input("Escribe tu nombre: ")
venta = input("Escribe la cantidad que vendiste: ")
venta = int(venta)

comision = venta * 0.13

print(f"Tu comision {nombre} este periodo sera de: {round(comision)}")