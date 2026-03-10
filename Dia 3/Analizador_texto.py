# Ingreso de las variables por el usuario, se pasan a minusculas para no generar errores
texto = input("Ingresa un texto: ").lower()
l1 = input("Ingrese una letra: ").lower()
l2 = input("Ingrese una letra: ").lower()
l3 = input("Ingrese una letra: ").lower()

# Se utiliza count() para contar las veces que aparece la letra en el texto
vecesl1 = texto.count(l1)
vecesl2 = texto.count(l2)
vecesl3 = texto.count(l3)

print(f"La cantidad de veces que aparece la letra {l1} es: {vecesl1} ")
print(f"La cantidad de veces que aparece la letra {l2} es: {vecesl2} ")
print(f"La cantidad de veces que aparece la letra {l3} es: {vecesl3}\n ")

#El texto separa cada palabra como elemento de una lista
palabras = texto.split()
#Se cuenta el numero de palabras
cantidad_palabras = len(palabras)
print(f"La cantidad de palabras en el texto es de: {cantidad_palabras}\n")

#Indice 0 para la primera letra del texto y -1 para saber la ultima
primeral = texto[0]
ultimal = texto[-1]



print(f"La primera letra del texto es: {primeral} y la ultima es: {ultimal}\n")

#La lista palabra se invierte
palabras.reverse()

#se guarda en una variable los elementos de la lista invertida a manera de string
texto_inverso = " ".join(palabras)
print(f"Tu texto al reves es: {texto_inverso}\n")

#Se crea un diccionario donde las claves son valores booleanos
opciones = {1:"si",0:"no"}

#se guarda en una variable si la palabra python esta en la lista palabras
seleccion = "python" in palabras

#Se utiliza el valor de la variable seleccion como clave para buscarla en el diccionario creado
print(f"La palabra python {opciones[seleccion]} aparece en el texto\n")

