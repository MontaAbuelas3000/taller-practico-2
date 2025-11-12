#EJERCICIO 3: Control de Asistencia Escolar
# Contexto:
# Eres profesor y necesitas llevar control de asistencia de tus estudiantes. La institución tiene las siguientes
# reglas:
# Si un estudiante falta más del 20% de las clases, reprueba automáticamente por inasistencia
# Si falta entre 15% y 20%, recibe una advertencia
# Si falta menos del 15%, está bien
# El semestre tiene 80 clases totales.
# Tu tarea:
# Crea un programa que:
# 1. Solicite el nombre del estudiante
# 2. Pregunte cuántas clases ha faltado
# 3. Calcule el porcentaje de inasistencia
# 4. Determine el estado del estudiante
# 5. Muestre cuántas clases más puede faltar antes de recibir advertencia o reprobar
# 6. Permita consultar múltiples estudiantes hasta que el usuario decida salir

#EJERCICIO 3: Control de Asistencia Escolar

# Funciones

def calculoFaltas(faltas_clases, total_clases):
    porcentaje = (faltas_clases / total_clases) * 100
    return porcentaje 

# Defino cantidad de clases
total_clases = 80

while True:
    # Entradas
    nombre_estudiante = input("Ingrese el nombre completo del estudiante: ")
    faltas_clases = int(input("Cuantas faltas a tenido el estudiante?: "))
    
    # llamo la funcion para saber cuanto me dio el porcentaje
    porcentaje_de_faltas = calculoFaltas(faltas_clases, total_clases)

    print(f"\nEl estudiante a faltado a un: %{porcentaje_de_faltas}")

    # dependiendo lo que dio le decimos como va
    if porcentaje_de_faltas > 20.0: 
        print("\nEl estudiante a reprobado por inasistencia")
    elif porcentaje_de_faltas >= 15:
        print("\nEl estudiante esta apunto de reprobar por inasistencia")
    elif porcentaje_de_faltas < 15.0:
        print("\nEl estudiante esta melo")

    # vamos a calcular a cuantas clases puede faltar
    limite_advertencia = (total_clases * 0.15) - faltas_clases
    limite_reprobado = (total_clases * 0.20) - faltas_clases

    # para que no diga que podemos faltar -1 calse jaja
    if limite_advertencia < 0:
        limite_advertencia = 0
    if limite_reprobado < 0:
        limite_reprobado = 0

    # avisamos 
    print(f"Puede faltar {limite_advertencia} clases más antes de la advertencia")
    print(f"Puede faltar {limite_reprobado} clases antes de perder")
    print("\nSi estan en 0 te jodiste mi hermano, ya perdiste. Sino es el caso vas bien")

    # le damos la instruccion al ciclo pra que sepa donde debe terminar
    continuar = input("\n¿Consultar otro estudiante? (s/n): ")
    if continuar != "s":
        print("\nFin ¡Buen trabajo, profe!")
        break