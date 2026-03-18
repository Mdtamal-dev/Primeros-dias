from pathlib import Path
from os import system
import os


def bienvenida():
    bienvenida = "BIENVENIDO AL ADMINISTRADOR DE RECETAS"
    ruta = Path.cwd()/ "Recetas"
    cantidad = 0
    n = len(bienvenida)
    n = "+" * (len(bienvenida) + 6)
    print(n)
    print("+  " + bienvenida + "  +")
    print(n + "\n")
    print(f"Las recetas se encuentran en el directorio:\n{ruta}")
    for txt in Path(ruta).glob("**/*.txt"):
        cantidad += 1
    print(f"La cantidad de recetas en el administrador es de: {cantidad}\n")

def menu_opciones():
    print("""
    Elige una opcion:
    [1]-----Leer receta
    [2]-----Crear receta
    [3]-----Crear categoria
    [4]-----Eliminar receta
    [5]-----Eliminar categoria
    [6]-----Finalizar Programa
    """)
    eleccion = "7"
    while eleccion not in ["1","2","3","4","5","6"]:
        eleccion = input("Selecciona tu opcion: ")
    
    return eleccion

def elegir_categoria():
    ruta = Path.cwd() / "Recetas"
    i = 1
    dic = {}
    for x in ruta.iterdir():
        print(f" [{i}]---{x.name}")
        dic[i] = x.name
        i += 1
    seleccion = "a"
    while seleccion not in dic.keys():
        seleccion = int(input("Elige una categoria valida: "))

    return dic[seleccion]
    
def elegir_receta(categoria):
    ruta = Path.cwd() / "Recetas" / categoria
    i = 1
    dic = {}
    for x in ruta.iterdir():
        print(f" [{i}]---{x.name}")
        dic[i] = x.name
        i += 1
    seleccion = "a"
    while seleccion not in dic.keys():
        seleccion = int(input("Elige una receta valida: "))

    return dic[seleccion]

def leer_receta(categoria,receta):
    ruta = Path.cwd() / "Recetas" / categoria / receta
    print(ruta.read_text())

def crear_receta(categoria):
    ruta = Path.cwd() / "Recetas" / categoria
    nombre = input("Elige el nombre de tu archivo: ")
    archivo = Path(ruta, nombre)
    if archivo.exists():
        print("Ese archivo ya existe, por favor elige otro nombre.")
    nombre = input("Elige el nombre de tu archivo: ")
    contenido = input("Escribe su contenido: ")
    archivo.write_text(contenido)
    
def crear_categoria():
    ruta = Path.cwd() / "Recetas"
    nombre = input("Nombre de la nueva categoria: ")
    directorio = Path(ruta,nombre)
    if directorio.exists():
        nombre = input("Elige otro nombre: ")
    Path(ruta,nombre).mkdir()

def eliminar_receta(categoria,receta):
    ruta = Path.cwd() / "Recetas" / categoria / receta
    os.remove(ruta)
    
def eliminar_categoria(categoria):
    ruta = Path.cwd() / "Recetas" / categoria

    for item in sorted(ruta.rglob("*"), reverse=True):
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            item.rmdir()
    ruta.rmdir()
#---------------------------CODIGO-------------------------------------
#elegir_categoria()

ejecutar = True
while ejecutar:
    bienvenida()
    seleccion = menu_opciones()
    match seleccion:
        case "1": # Leer receta
            categoria = elegir_categoria()
            receta = elegir_receta(categoria)
            leer_receta(categoria,receta)

        case "2": # Crear receta
            categoria = elegir_categoria()
            crear_receta(categoria)
            
        case "3": # Crear categoria
            crear_categoria()

        case "4": # Eliminar receta
            categoria = elegir_categoria()
            receta = elegir_receta(categoria)
            eliminar_receta(categoria,receta)
        case "5": # Eliminar categoria
            categoria = elegir_categoria()
            eliminar_categoria(categoria)
        case "6": # Finalizar programa
            ejecutar = False
    system("cls")
    
