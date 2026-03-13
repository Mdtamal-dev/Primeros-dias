from random import choice

# Generar una lista con las palabras
palabras = [
    "sol",
    "montaña",
    "libro",
    "computadora",
    "perro",
    "ventana",
    "cafe",
    "nube",
    "rio",
    "camino",
    "bosque",
    "estrella",
    "puerta",
    "ciudad",
    "jardin",
    "luna",
    "tren",
    "mar",
    "silla",
    "reloj"
]

#El programa elige una palabra
palabra = choice(palabras)
vidas = 6

#se imprime el mensaje
print(f"Este es el juego del ahorcado tienes {vidas} oportunidades para adivinar la palabra")
oculto = ["_" for x in range(len(palabra))]
print(oculto)

# funcion que verifica la letra ingresada por el usuario
def elige_letra():
    letra = "-"
    while letra not in "abcdefghijklmnñopqrstuvwxyz":
        letra = input("Ingresa una letra del abecedario: ").lower()
        if letra in "".join(oculto):
            letra = input("Letra ya ingresada, coloque una nueva: ")
    return letra
    
# funcion que revisa si la letra ingresada esta en la palabra elegida
def checar_letra(letra):
    if letra in palabra:
        for i,l in enumerate(palabra):
            if letra == l:
                oculto[i] = letra
        return True
    else:
        return False
# funcion que revisa si la palabra oculta es igual a la palabra elegida
def ganar():
    if palabra == "".join(oculto):
        print(f"Felicidades has ganado la palabra era: {palabra}")
        return True
    else:
        return False


while vidas > 0:

    eleccion = elige_letra()
    verificar = checar_letra(eleccion)
    if ganar():
        break
    if not verificar:
        vidas -= 1
    print(f"Te quedan {vidas} vidas")
    if vidas == 0:
        print("PERDISTE")
        print(f"La palabra era {palabra}")
        break
    print(oculto)
    

    



    
    

    

    
