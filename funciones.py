#

from estudiantes import *

#pide una opcion
def pedir_opcion():
    opcion = int(input("seleciones una opcion (1-8): "))
    while opcion < 1 or opcion > 8:
        opcion = int(input("error,selecione una opcion (1-8): "))
    return opcion
#muestra el menu
def mostrar_menu():
    seguir = "s"
    while seguir == "s":
        print("---MENU DE OPCIONES---")
        print("1-LISTAR LOS ALUMNOS POR ORDEN ASCENDENTE DE APELLIDO\n2-OBTENER EL PROMEDIO DE NOTAS DE CADA ESTUDIANTE\n3-LISTAR LEGAJO,NOMBRE,APELLIDO Y EDAD DE LOS ESTUDIANTES QUE CURSAN EL PROGRAMA DE ING. EN INFORMATICA\n4OBTENER UN PROMEDIO DE EDAD DE LOS ESTUDIANTES\n5-INFORMAR EL ALUMNO CON MAYOR PROMEDIO DE NOTAS\n6-LISTAR NOMBRE Y APELLIDO DE LOS ALUMNOS QUE FORMAN EL GRUPO CLUB DE INFORMATICA CON SUS PROMEDIOS\n7-LISTAR LEGAJO,NOMBRE,APELLIDO Y PROGRAMA QUE CURSAN LOS ALUMNOS MAS JOVENES\n8-SALIR DE MENU") 
        opcion = pedir_opcion()
        
        if opcion == 1:
            listar_alumnos_asendente(estudiantes)
        elif opcion == 2:
            calcular_promedio_notas(estudiantes)
        elif opcion == 3:
            mostrar_alumnos_cursantes_de_ing(estudiantes)
        elif opcion == 4:
            calcular_promedio_edad(estudiantes)
        elif opcion == 5:
            mostrar_mayor_promedio(estudiantes)
        elif opcion == 6:
            mostrar_alumnos_club_informatica(estudiantes)
        elif opcion == 7:
            mostrar_alumnos_jovenes(estudiantes)
        else:
            seguir = salir_menu()



#1
def ordenar_alumnos__por_apellido_y_nombre(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i + 1,len(lista)):
            if lista[i]["apellido"] > lista[j]["apellido"]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            elif lista[i]["apellido"] == lista[j]["apellido"]:
                if lista[i]["nombre"] > lista[j]["nombre"]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista
def listar_alumnos_asendente(lista:list):
    lista_ordenada = ordenar_alumnos__por_apellido_y_nombre(lista)
    for e_estudiante in lista_ordenada:
        print(e_estudiante["legajo"],e_estudiante["nombre"],e_estudiante["apellido"],e_estudiante["edad"])


#2
def calcular_promedio_notas(lista:list):
    for e_estudiante in lista:
        suma = 0 
        cantidad = 0
        promedio = 0

        for nota in e_estudiante["notas"]:
            suma += nota
            cantidad += 1
            promedio = suma / cantidad
        print(e_estudiante["nombre"],"tiene un promedio de :",promedio)


#3
def mostrar_alumnos_cursantes_de_ing(lista:list):
    for e_estudiantes in lista:
        if e_estudiantes["programa"]["nombre"] == "Ingenieria en Informatica":
            print(e_estudiantes["legajo"],e_estudiantes["nombre"],e_estudiantes["apellido"],e_estudiantes["edad"])   


#4
def mostrar_estudiantes(lista:list):
    resultado = ""
    for e_estudiantes in lista:
        resultado += e_estudiantes['nombre'] + " " + e_estudiantes['apellido'] + "\n"
    return resultado

def calcular_promedio_edad(lista:list):
    suma = 0 
    cantidad = 0
    promedio = 0
    for e_estudiantes in lista:
        suma += e_estudiantes["edad"]
        cantidad += 1
        promedio = suma / cantidad
    lista_estudiantes = mostrar_estudiantes(lista)
    print(f"el promedio de edad de los estudiantes\n{lista_estudiantes}es de {promedio} años")

#5
def mostrar_mayor_promedio(lista:list):
    promedio_mayor = -1
    estudiante_mayor = ""
    for e_estudiantes in lista:
        suma = 0 
        cantidad = 0
        for nota in e_estudiantes["notas"]:
            suma += nota
            cantidad += 1
        promedio = suma / cantidad
        if promedio > promedio_mayor:
                promedio_mayor = promedio
                estudiante_mayor =  e_estudiantes["nombre"] + " " + e_estudiantes["apellido"]
    print(f"el alumno con mayor promedio de notas es {estudiante_mayor} con {promedio_mayor} de promedio")


#6
def calcular_promedio_informatica(dic:dict)->float:
    suma = 0 
    cantidad = 0
    for nota in dic["notas"]:
        suma += nota
        cantidad += 1
        promedio = suma / cantidad
    return promedio
def mostrar_alumnos_club_informatica(lista:list):
    for e_estudiante in lista:
        if "grupos" in e_estudiante:
            for grupo in e_estudiante["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    promedio = calcular_promedio_informatica(e_estudiante)
                    print(f"{e_estudiante['nombre']} {e_estudiante['apellido']} con el promedio de {promedio}")
                    break

#7
def mostrar_alumnos_jovenes(lista:list):
    edad_minima = 100

    for e_estudiante in lista:
        if e_estudiante["edad"] < edad_minima:
            edad_minima = e_estudiante["edad"]
    for e_estudiante in lista:
        if e_estudiante["edad"] == edad_minima:
            print(e_estudiante["nombre"],e_estudiante["apellido"],e_estudiante["legajo"],e_estudiante["programa"]["nombre"])

#8
def salir_menu():
    seguir = "n"
    return seguir