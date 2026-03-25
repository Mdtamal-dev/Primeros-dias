from random import randint

class Persona():

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def info_cliente(self):
        print(f"""
Cliente: {self.nombre} {self.apellido}
Num. de cuenta: {self.numero_cuenta}
Balance: {self.balance}
""")
        
    def depositar(self,monto):
        self.balance += monto
        return self.balance

    def retirar(self,monto):
        self.balance -= monto
        return self.balance

def crear_cliente():
    nombre = input("Ingresa tu nombre: ").upper()
    apellido = input("Ingrese su apellido: ").upper()
    print("Estamos generando tu numero de cuenta...")
    num_cuenta = "1234"
    num_cuenta2 = "5678"
    num_cuenta3 = str(randint(1000,9999))
    num_cuenta4 = str(randint(1000,9999))
    numero_cuenta = f"{num_cuenta} {num_cuenta2} {num_cuenta3} {num_cuenta4}"
    saldo = 0
    cliente = Cliente(nombre,apellido,numero_cuenta,saldo)
    print("Listo tu cuenta a sido creada estos son los datos de tu cuenta: ")
    print(f"""
Cliente: {nombre} {apellido}
Num. de cuenta: {numero_cuenta}
Balance: {saldo}
""")
    
    return(cliente)
    

def inicio():
    print("Hola bienvenido al banco ABC te gustaria ser un cliente?: ")
    print("[1] - si")
    print("[2] - no")
    print("[3] - Ya soy cliente")
    opcion = int(input())
    if opcion == 1:
        cliente = crear_cliente()
    else:
        return print("Gracias por visitar banco ABC")
    comenzar = True
    
    while comenzar:
        print("""Que deseas hacer?: 
              [1] - Depositar
              [2] - retirar
              [3] - salir""")
        
        opcion2 = int(input())

        match opcion2:
            case 1:
                print("Ingrese la cantidad que desea depositar: ")
                cliente.depositar(int(input()))
                print(f"Listo, saldo actualizado a : {cliente.balance}")
            case 2:
                print("Ingrese la cantidad que desea retirar: ")
                retirar = int(input())
                if retirar > cliente.balance:
                    print("No tiene la cantidad suficiente para retirar: ")
                else:
                    cliente.retirar(retirar)
                    print(f"Listo, saldo actualizado a : {cliente.balance}")
            case 3:
                print("Gracias por visitar banco ABC")
                comenzar = False
    
        




inicio()
