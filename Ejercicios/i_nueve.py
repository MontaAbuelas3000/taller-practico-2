#EJERCICIO 9: Analizador de Calificaciones de Curso
# Contexto:
# Eres profesor de un curso con 30 estudiantes y necesitas un programa que analice las calificaciones y
# genere estadísticas completas. Cada estudiante tiene 4 notas parciales y un examen final que vale el 30%
# de la nota definitiva.
# Tu tarea:
# Crea un programa que:
# 1. Permita ingresar el nombre y las 5 notas de cada estudiante (4 parciales + final)
# 2. Calcule la nota definitiva: (promedio de 4 parciales × 0.70) + (examen final × 0.30)
# 3. Determine si el estudiante aprobó (nota ≥ 3.0)
# 4. Identifique al mejor estudiante y al de menor nota
# 5. Calcule el promedio general del curso
# 6. Muestre cuántos aprobaron y cuántos reprobaron
# 7. Genere una lista de estudiantes ordenados por nota (de mayor a menor)
# 8. Identifique estudiantes en riesgo (nota definitiva entre 2.5 y 2.9)

#EJERCICIO 9: Analizador de Calificaciones de Curso

# EJERCICIO 9: Analizador de Calificaciones de Curso

# EJERCICIO 9: Analizador de Calificaciones de Curso (versión básica)

estudiantes = []
notas_definitivas = []
nombres = []

cantidad = int(input("¿Cuántos estudiantes? "))

i = 0
while i < cantidad:
    print("Estudiante", i + 1)
    nombre = input("Nombre: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    nota_final = float(input("Nota examen final: "))
    
    promedio_parciales = (nota1 + nota2 + nota3 + nota4) / 4
    definitiva = (promedio_parciales * 0.7) + (nota_final * 0.3)
    
    nombres.append(nombre)
    notas_definitivas.append(definitiva)
    estudiantes.append([nombre, definitiva])
    i = i + 1

# Estadísticas
total = len(estudiantes)
suma_notas = 0
aprobados = 0
reprobados = 0
en_riesgo = 0
mejor = estudiantes[0]
peor = estudiantes[0]

i = 0
while i < total:
    nota = estudiantes[i][1]
    suma_notas = suma_notas + nota

    if nota >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

    if nota >= 2.5 and nota < 3.0:
        en_riesgo = en_riesgo + 1

    if nota > mejor[1]:
        mejor = estudiantes[i]
    elif nota < peor[1]:
        peor = estudiantes[i]
    i = i + 1

promedio = suma_notas / total

# Mostrar resultados
print("\nRESULTADOS DEL CURSO")
print("Total estudiantes:", total)
print("Promedio general:", round(promedio, 2))
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("En riesgo:", en_riesgo)
print("Mejor estudiante:", mejor[0], "-", round(mejor[1], 2))
print("Peor estudiante:", peor[0], "-", round(peor[1], 2))

print("\nLISTA DE ESTUDIANTES")
i = 0
while i < total:
    print(nombres[i], "-", round(notas_definitivas[i], 2))
    i = i + 1

