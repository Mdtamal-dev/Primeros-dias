from numeros import *
from os import system


def bienvenida():
    mensaje = " Bienvenido a Farmacias ABC "
    cantidad_letras = len(mensaje)
    print("+" + ("-" * cantidad_letras) + "+")
    print("|" + mensaje + "|" )
    print("+" + ("=" * cantidad_letras) + "+")


def elegir_area():
    print("""Para asignar un turno primero eliga el area a la cual desea ir:
        [1] - Perfumeria
        [2] - Farmacia
        [3] - Cosmeticos""")
    eleccion = "x"
    while eleccion not in ["1","2","3"]:
        eleccion = input("Selecciona tu area: ")
    return int(eleccion)

def elegir_seguir():
    eleccion = "x"
    while eleccion not in ["1","2"]:
        eleccion = input("Desea elegir otro turno: ")
    return int(eleccion)
    
encendido = True
p = generador_numero(1)
f = generador_numero(2)
c = generador_numero(3)
while encendido:
    bienvenida()
    x = elegir_area()
    if x == 1:
        decorador_numero(next(p))
    elif x == 2:
        decorador_numero(next(f))
    elif x == 3:
        decorador_numero(next(c))
    continuar = elegir_seguir()
    if continuar == 2:
        encendido = False
    system("cls")
    
