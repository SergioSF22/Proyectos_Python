class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class Cliente(Persona):
    def __init__(self, nombre, apellidos, numero_cuenta, saldo):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"""------DATOS CLIENTE------
NOMBRE: {self.nombre}
APELLIDOS: {self.apellidos}
Nº CUENTA: {self.numero_cuenta}
SALDO: {self.saldo}
------------------------"""

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Ingreso realizado con éxito.")
        print(f"Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("La cantidad indicada es mayor al saldo actual.")
            print("Operación NO realizada.")
        else:
            self.saldo -= cantidad
            print("Retirada realizada con éxito.")
            print(f"Saldo actual: {self.saldo}")


def crear_cliente():
    nombre = input("Introduce el nombre del cliente: ")
    apellidos = input("Introduce los apellidos del cliente: ")
    numero_cuenta = input("Introduce número de cuenta del cliente: ")
    saldo = int(input("Introduce el saldo del cliente: "))
    return Cliente(nombre, apellidos, numero_cuenta, saldo)


def inicio():
    cliente = crear_cliente()
    salir = False
    while not salir:
        print("""------MENÚ------
1. MOSTRAR DATOS
2. INGRESAR 
3. RETIRAR
4. SALIR
----------------""")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                print(cliente)
                pass
            case "2":
                cantidad = int(input("Introduzca la cantidad a ingresar: "))
                cliente.depositar(cantidad)
                pass
            case "3":
                cantidad = int(input("Introduzca la cantidad a retirar: "))
                cliente.retirar(cantidad)
                pass
            case "4":
                salir = True
                print("Has salido")
                pass
            case _:
                print("Opción no válida")

inicio()