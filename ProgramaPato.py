print("Hola, este programa te permitirá calcular y comparar tu puntaje ponderado con el último matriculado de dos Universidades Chilenas")

Nombre_Persona = input("¿Cual es tu nombre? ")

print("Genial {}. A continuacion deberas ingresar tus puntajes.".format(Nombre_Persona))

Puntajes_Persona = []
Puntajes_Persona.append(input("NEM: "))
Puntajes_Persona.append(input("Ranking: "))
Puntajes_Persona.append(input("Comprension lectora: "))
Puntajes_Persona.append(input("Matematica: "))
Puntajes_Persona.append(input("Ciencias: "))
Puntajes_Persona.append(input("Historia: "))

print("Perfecto! Tus puntajes fueron guardados")
Nombre_Carrera = input("¿Cual es el nombre de la carrera? ")

while True:
    print("Bien! Comencemos con los datos de cada universidad")

    Nombre_Universidad_1 = input("¿Cual es el nombre de la primera universidad? ")

    print("A continuacion ingrese las ponderaciones en {}".format(Nombre_Universidad_1))

    Ponderacion_UNI1 = []
    Ponderacion_UNI1.append(input("NEM: "))
    Ponderacion_UNI1.append(input("Ranking: "))
    Ponderacion_UNI1.append(input("Comprension lectora: "))
    Ponderacion_UNI1.append(input("Matematica: "))
    Ponderacion_UNI1.append(input("Ciencias: "))
    Ponderacion_UNI1.append(input("Historia: "))

    Puntuacion_UNI1_Ultimo_Matriculado = float(input("Ingrese la cantidad de puntos del ultimo matriculado: "))

    print("Muy bien! Sigamos con los datos de la siguiente universidad.")

    Nombre_Universidad_2 = input("¿Cual es el nombre de la segunda universidad? ")

    print("A continuacion ingrese las ponderaciones en {}".format(Nombre_Universidad_2))

    Ponderacion_UNI2 = []
    Ponderacion_UNI2.append(input("NEM: "))
    Ponderacion_UNI2.append(input("Ranking: "))
    Ponderacion_UNI2.append(input("Comprension lectora: "))
    Ponderacion_UNI2.append(input("Matematica: "))
    Ponderacion_UNI2.append(input("Ciencias: "))
    Ponderacion_UNI2.append(input("Historia: "))

    Puntuacion_UNI2_Ultimo_Matriculado = float(input("Ingrese la cantidad de puntos del ultimo matriculado: "))
        
    Puntaje_Total_UNI1 = 0
    Resultados_UNI1 = []
    for Posicion_Lista in range(6):
        Resultados_UNI1.append(str(int(Puntajes_Persona[Posicion_Lista]) * (int(Ponderacion_UNI1[Posicion_Lista]) / 100)))
        Puntaje_Total_UNI1 = float(Resultados_UNI1[Posicion_Lista]) + float(Puntaje_Total_UNI1)

    Puntaje_Total_UNI2 = 0
    Resultados_UNI2 = []
    for Posicion_Lista in range(6):
        Resultados_UNI2.append(str(int(Puntajes_Persona[Posicion_Lista]) * (int(Ponderacion_UNI2[Posicion_Lista]) / 100)))
        Puntaje_Total_UNI2 = float(Resultados_UNI2[Posicion_Lista]) + float(Puntaje_Total_UNI2)

    if Puntaje_Total_UNI1 > Puntuacion_UNI1_Ultimo_Matriculado:
        Resultado_Seleccion_UNI1 = "SELECCIONADO"
    else:
        Resultado_Seleccion_UNI1 = "NO SELECCIONADO"

    if Puntaje_Total_UNI2 > Puntuacion_UNI2_Ultimo_Matriculado:
        Resultado_Seleccion_UNI2 = "SELECCIONADO"
    else:
        Resultado_Seleccion_UNI2 = "NO SELECCIONADO"


    print("{}, aqui estan sus datos:".format(Nombre_Persona))
    print("X                               " + Nombre_Universidad_1 + "                    " + Nombre_Universidad_2)
    print("NEM:                            " + Resultados_UNI1[0] + "                    " + Resultados_UNI2[0])
    print("Ranking:                        " + Resultados_UNI1[1] + "                    " + Resultados_UNI2[1])
    print("Comprension lectora:            " + Resultados_UNI1[2] + "                    " + Resultados_UNI2[2])
    print("Matematica:                     " + Resultados_UNI1[3] + "                    " + Resultados_UNI2[3])
    print("Ciencias:                       " + Resultados_UNI1[4] + "                    " + Resultados_UNI2[4])
    print("Historia:                       " + Resultados_UNI1[5] + "                    " + Resultados_UNI2[5])
    print("Puntaje del postulante:         " + str(Puntaje_Total_UNI1) + "                    " + str(Puntaje_Total_UNI2))
    print("Ultimo seleccionado:            " + str(Puntuacion_UNI1_Ultimo_Matriculado) + "                    " + str(Puntuacion_UNI2_Ultimo_Matriculado))
    print("Resultado de seleccion:         " + Resultado_Seleccion_UNI1 + "              " + Resultado_Seleccion_UNI2)

    Nueva_Comparacion = input("¿Desea realizar otra comparacion? S/N: ")
    if (Nueva_Comparacion == "N") or (Nueva_Comparacion == "n"):
        break
