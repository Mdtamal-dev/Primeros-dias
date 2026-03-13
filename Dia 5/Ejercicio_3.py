"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas
"""

def ceros(*args):
    for n in range(0,len(args)-1):
        if args[n] == 0 and args[n+1] == 0:
            return True
        n += 1

    return False
        

    



print(ceros(0,1,3,4,0,1,1,1,1,1,11,1,1,0,0))