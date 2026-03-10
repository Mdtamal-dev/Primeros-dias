nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre} este es el juego de adivina el numero")
print("Tendras 8 intentos para poder adivinar que esta dentro del 1 al 100, ¡Estas listo!")

from random import randint

aleatorio = randint(1,101)


vidas = 0

while vidas < 8:
    numero = int(input("Escribe un numero del 1 al 100: "))
    vidas += 1
    if numero == aleatorio:
        print(f"Has ganado, te ha tomado {vidas} intentos")
        break
    elif numero > 100 or numero < 0:
        print("El numero no es valido")
    elif numero > aleatorio:
        print("El numero que ingresaste es mayor")
    elif numero < aleatorio:
        print("El numero que ingresaste es menor")

    print(f"TE QUEDAN {8 - vidas} INTENTOS")
    

if vidas == 8:
    print(f"Game over, el numero era {aleatorio}")
    


