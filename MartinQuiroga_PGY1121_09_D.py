import numpy as np

list_nro_nif = []
list_nombre = []
list_edad = []
list_unioneu = []

def nro_nif_valido(nro):
    if len(nro) < 11:
        return False

    return True

def nombre_valido(nombre):
    if len(nombre) <= 8:
        return False
    
    return True

def edad_valida(edad):
    if edad <= 0:
        return False

    return True

def guardar(nro_nif, nombre, edad, unioneu):
    list_nro_nif.append(nro_nif)
    list_nombre.append(nombre)
    list_edad.append(edad)
    list_unioneu.append(unioneu)
    
def buscar_nif(valor):
    for i in range(len(list_nro_nif)):
        if list_nro_nif[i] == valor:
            return i
    return -1
    
def imprimir_ficha(index):
    print(f"NIF: {list_nro_nif[index]}")
    print(f"Nombre: {list_nombre[index]}")
    print(f"Edad: {list_edad[index]}")
    print(f"¿Pertenece a la Union EU?: {list_unioneu[index]}")

menu = True

while menu:
    print("MENU")
    print("1: Grabar")
    print("2: Buscar")
    print("3: Imprimir certificados")
    print("4: Salir")

    try:
        opcion = int(input("Escoja una opción "))
    except:
        print("Valor no valido")
        continue

    if opcion < 1 or opcion > 4:
        print("Opción no existente")
        continue

    if opcion == 1:

        nif = ""
        while nro_nif_valido(nif) == False:
            nif = input("Ingrese un NIF valido: ")

        nombre = ""
        while nombre_valido(nombre) == False:
            nombre = input("Ingrese un nombre: ")

        edad = 0
        while edad_valida(edad) == False:
            edad = int(input("Ingrese la edad: "))

        unioneu = input("¿Pertenece a la Union EU? (si/no): ")

        guardar(nif, nombre, edad, unioneu)

    if opcion == 2:
        nif_buscar = input("Ingrese el NIF que desea buscar: ")
        index_producto = buscar_nif(nif_buscar)

        if index_producto > -1:
            imprimir_ficha(index_producto)
        else:
            print(f"El NIF {nif_buscar} no se encuentra en la base de datos.")
    if opcion == 3:
        estado_conyugal = str(input("Defina su situacion conyugal: "))
        print("")
        print("1. Certificado de Nacimiento")
        print("2. Pertenece a Union Europea")
        print("3. Situacion Conyugal")
        print("")
        certificado = int(input("Escoja un certificado a imprimir: "))
        
        if certificado == 1:
            certificado = "Certificado de Nacimiento"
        elif certificado == 2:
            certificado = "Pertenencia Union Europea"
        elif certificado == 3:
            certificado = "Estado Conyugal"
        
        def imprimir_certificados():
            for i in range(len(nif)):
                monto_aleatorio = np.random.randint(1500, 3500)
                print("Certificado: ", certificado)
                print("NIF: ", nif)
                print("Nombre : ", nombre)
                print("Pertenece a Union Europea: ", unioneu)
                print("Estado Conyugal: ", estado_conyugal)
                print("Valor Certificado: ", monto_aleatorio)

    if opcion == 4:
        print("Saliendo del programa...")
        print("Programa realizado por Martin Quiroga")
        print("Version: 1.0")
        menu = False
