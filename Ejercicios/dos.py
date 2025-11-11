#EJERCICIO 2: Calculadora de Nómina Mensual
# Contexto:
# Eres el encargado de recursos humanos de una empresa y necesitas calcular el salario neto de los
# empleados. En Colombia, del salario bruto se descuentan:
# Salud: 4% del salario bruto
# Pensión: 4% del salario bruto
# Si el salario es mayor a $4,000,000, se descuenta un 1% adicional de impuesto de solidaridad
# Además, los empleados pueden tener horas extras que se pagan al 125% del valor de la hora normal.
# Tu tarea:
# Crea un programa que:
# 1. Solicite el nombre del empleado
# 2. Solicite el salario base mensual
# 3. Pregunte cuántas horas extras trabajó en el mes
# 4. Calcule el salario bruto (base + horas extras)
# 5. Calcule todos los descuentos
# 6. Muestre un desprendible de nómina completo

#EJERCICIO 2: Calculadora de Nómina Mensual

#  Función para calcular el valor de la hora
def calcular_valor_hora(salario_base):
    valor_hora = salario_base / 176 #176 segun Google porque realmente no se
    # Aca retornamos valor de hora para que se sepa que el valor de la hora sera = salario_base / 200
    return valor_hora

# Función para calcular los descuentos
def calcular_descuentos(salario_bruto):
    salud = salario_bruto * 0.04
    pension = salario_bruto * 0.04
    solidaridad = 0

    # Si gana más de 4 millones, le quitamos el 1% jajaja
    if salario_bruto > 4000000:
        solidaridad = salario_bruto * 0.01

    total_descuentos = salud + pension + solidaridad
    return salud, pension, solidaridad, total_descuentos

# Esto es lo que se va a mostrar
print("--- CALCULADORA DE NÓMINA MENSUAL ---")

# Entradas para saber la info del que solicita su salario
# Como ya comente en el primer ejercicio el int se utiliza para que la entrada sea 
# Valida con numero ya que si no se pone no daria el codigo

nombre = input("Ingrese el nombre completo del empleado: ")
salario_base = int(input("Ingrese el salario base mensual: "))
horas_extras = int(input("Ingrese las horas extras trabajadas en el mes: "))

# Cálculos
valor_hora = calcular_valor_hora(salario_base)
#llamamos la funcion para el valor de la hora
valor_hora_extra = valor_hora * 1.25
#si tiene horas extras estas se deberan multiplicar por el 125%
pago_horas_extras = valor_hora_extra * horas_extras

salario_bruto = salario_base + pago_horas_extras

salud, pension, solidaridad, total_descuentos = calcular_descuentos(salario_bruto)
#llamamos la funcion que nos dara los 4% correspondientes

salario_neto = salario_bruto - total_descuentos

# --- DESPRENDIBLE ---
print("\nDESPRENDIBLE DE NÓMINA")
print(f"Empleado: {nombre}")
print(f"Salario base: ${salario_base}")
print(f"Horas extras trabajadas: {horas_extras}")
print(f"Valor hora extra: ${valor_hora_extra}")

print("\nDEVENGADO:")
print(f"  Salario base: ${salario_base}")
print(f"  Horas extras: ${pago_horas_extras}")
print(f"  Total devengado: ${salario_bruto}")

print("\nDEDUCCIONES:")
print(f"  Salud (4%): ${salud}")
print(f"  Pensión (4%): ${pension}")

#utilizamos este condicional para que no se aplique si no es verdad
if solidaridad > 0:
    print(f"  Impuesto de solidaridad (1%): ${solidaridad}")

print(f"  Total deducciones: ${total_descuentos}")

# Y aca deberia imprimir lo que se le debe al empleado
print(f"\nNETO A PAGAR/COBRAR: ${salario_neto}")
