#EJERCICIO 6: Calculadora de Índice de Masa Corporal (IMC) Clínica
# Contexto:
# Trabajas en una clínica y necesitas un programa que calcule el IMC de los pacientes y les dé
# recomendaciones. El IMC se calcula: peso / (altura^2) donde el peso está en kg y la altura en metros.
# Clasificación de IMC:
# Menos de 18.5: Bajo peso
# 18.5 - 24.9: Peso normal
# 25.0 - 29.9: Sobrepeso
# 30.0 - 34.9: Obesidad grado I
# 35.0 - 39.9: Obesidad grado II
# 40.0 o más: Obesidad grado III
# Tu tarea:
# Crea un programa que:
# 1. Solicite nombre, peso y altura del paciente
# 2. Calcule el IMC
# 3. Determine la clasificación
# 4. Muestre recomendaciones específicas según el resultado
# 5. Calcule el peso ideal (rango saludable para su altura)
# 6. Permita procesar múltiples pacientes
# 7. Al final, muestre estadísticas de todos los pacientes atendidos (promedio de IMC, cuántos están en
# cada categoría)

#EJERCICIO 6: Calculadora de Índice de Masa Corporal (IMC) Clínica

#funcion que calculara el IMC
def calculoIMC(peso, altura):
    return peso / (altura * altura)

#ahora la que clasifica el imc
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad grado I"
    elif imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"
    
#y por ultimo las listas de recomendaciones
def dar_recomendaciones(categoria):
    if categoria == "Bajo peso":
        return [
            "Aumentar la ingesta calórica con alimentos nutritivos",
            "Realizar ejercicios de fuerza para ganar masa muscular",
            "Consultar con un nutricionista"
        ]
    elif categoria == "Peso normal":
        return [
            "Mantener una dieta equilibrada",
            "Seguir con actividad física regular",
            "Realizar controles médicos periódicos"
        ]
    elif categoria == "Sobrepeso":
        return [
            "Reducir consumo de calorías",
            "Aumentar actividad física",
            "Consultar con nutricionista",
            "Meta: Perder entre 5-10 kg"
        ]
    elif categoria == "Obesidad grado I":
        return [
            "Reducir carbohidratos refinados y azúcares",
            "Ejercicio diario (mínimo 30 minutos)",
            "Consultar con un especialista en nutrición"
        ]
    elif categoria == "Obesidad grado II":
        return [
            "Buscar acompañamiento médico para plan de pérdida de peso",
            "Aumentar actividad física gradualmente",
            "Controlar presión y glucosa"
        ]
    elif categoria == "Obesidad grado III":
        return [
            "Requiere atención médica inmediata",
            "Evaluar posibles tratamientos clínicos o quirúrgicos",
            "Evitar dietas sin supervisión profesional"
        ]


# voy a agregar una ray que almacene los IMC y defino tipo de pesos
imcs =  []

pesos = {
    "Bajo peso": 0,
    "Peso normal": 0,
    "Sobrepeso": 0,
    "Obesidad grado I": 0,
    "Obesidad grado II": 0,
    "Obesidad grado III": 0
}

# aca van las entradas
print("IMC")
while True:
    nombre = input("Nombre del paciente: ")

    peso = int(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calculoIMC(peso, altura)
    categoria = clasificar_imc(imc)
    recomendaciones = dar_recomendaciones(categoria)

    imcs.append(imc)
    pesos[categoria] += 1

    #llamo la funcion para imprimirla correctamente
    mostrar_recomendaciones = dar_recomendaciones(categoria)

    print(f"\nPaciente: {nombre}")
    print(f"IMC: {imc}")
    print(f"Clasificación: {categoria}")
    print(f"RECOMENDACIONES: {mostrar_recomendaciones}")

    # ahora preguntamos si vamos a seguir o ya salimos para hacer conteo
    seguir = input("\n¿Evaluar otro paciente? (s/n): ")
    if seguir == "n":
        break

if imcs:
    promedio_imc = sum(imcs) / len(imcs)
    total_pacientes = len(imcs)

    print("\nESTADÍSTICAS DEL DÍA")
    print(f"Total de pacientes: {total_pacientes}")
    print(f"IMC promedio: {promedio_imc}")

    print("\nSaliendo...")
else:
    print("No se registraron pacientes hoy.")
    print("\nSalinedo...")



