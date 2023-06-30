personas = []
def verificar_nif(nif):
    if nif == "":
        return False
    return len(nif) == 10

def grabar_persona():
    nif = input("Ingrese el NIF: ")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    if verificar_nif(nif) and len(nombre) >= 8 and edad >= 0:
        persona = {"nif": nif, "nombre": nombre, "edad": edad}
        personas.append(persona)
        print("Persona grabada exitosamente.")
    else:
        print("Los datos ingresados no son validos")


def imprimir_certificado():
    certificados = ["Certificado de Nacimiento", "Estado Conyugal", "Pertenencia a la Union Europea"]
    nif = input("Ingrese el NIF de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")


    for certificado in certificados:
        print(f"nombre del certificado: {certificado}")
        print(f"NIF: {nif}")
        print(f"Nombre de la persona: {nombre}")
        print()

def buscar_persona():
    nif = input("ingrese el NIF de la persona a buscar: ")
    print("inoformacion de la persona encontrada")


while True:
    print("**-- Menu --**")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")

    opc = input("Ingrese una opcion:")

    if opc == "1":
        grabar_persona()
    elif opc == "2":
        buscar_persona()
    elif opc == "3":
        imprimir_certificado()
    elif opc == "4":
        print ("Gracias por usar el programa")
        break

