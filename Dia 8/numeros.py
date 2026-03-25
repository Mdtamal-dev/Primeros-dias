#Generadores de numeros
def generador_numero(numero):
    conteo = 1
    match numero:
        case 1:
            perfume = "P"
            
            while True:
                yield f"{perfume} - {conteo:03}"
                conteo += 1
            
        case 2:
            farmacia = "F"
            while True:
                yield f"{farmacia} - {conteo:03}"
                conteo += 1
            
        case 3:
            cosmeticos = "C"
            while True:
                yield f"{cosmeticos} - {conteo:03}"
                conteo += 1
            
def decorador_numero(turno):
    print(f"""
+--------------------------+
|       Tu turno es:       |
|                          |
|        {turno}           |
|                          |
|Ahora espere a ser llamado|
+--------------------------+
""")
