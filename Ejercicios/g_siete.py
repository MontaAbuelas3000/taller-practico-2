#EJERCICIO 7: Sistema de Turnos para Banco
# Contexto:
# Trabajas en un banco y necesitas automatizar el sistema de turnos. El banco tiene 3 tipos de servicios:
# Caja (C): Tiempo estimado 10 minutos, atención rápida
# Asesoría (A): Tiempo estimado 20 minutos
# Créditos (R): Tiempo estimado 30 minutos
# El sistema debe generar turnos en formato: C001, A001, R001, etc.
# Tu tarea:
# Crea un programa que:
# 1. Muestre un menú para que los clientes elijan su servicio
# 2. Genere un turno con el formato correcto (letra + número de 3 dígitos)
# 3. Muestre el turno asignado y el tiempo estimado de espera
# 4. Mantenga un contador separado para cada tipo de servicio
# 5. Muestre cuántas personas están esperando por cada servicio
# 6. Permita "llamar" al siguiente turno (eliminar el primero de la cola)
# 7. Muestre estadísticas del día (total de turnos generados por servicio)

#EJERCICIO 7: Sistema de Turnos para Banco

# Función para generar el turno 
def generar_turno(tipo, contador):
    return f"{tipo}{contador}"

# Función para calcular el tiempo de espera
def calcular_tiempo_espera(cola, tiempo_servicio):
    return len(cola) * tiempo_servicio

# Defino el valor de las variables
cola_caja = []
cola_asesoria = []
cola_creditos = []

contador_caja = 1
contador_asesoria = 1
contador_creditos = 1

tiempo_caja = 10
tiempo_asesoria = 20
tiempo_creditos = 30

# Contadores 
total_caja = 0
total_asesoria = 0
total_creditos = 0

print("BIENVENIDO AL BANCO")
while True:
    print("\n1. Solicitar turno para CAJA")
    print("2. Solicitar turno para ASESORÍA")
    print("3. Solicitar turno para CRÉDITOS")
    print("4. Llamar siguiente turno")
    print("5. Ver estado de colas")
    print("6. Cerrar sistema")

    opcion = input("Opción: ")

    if opcion == "1":

        turno = generar_turno("C", contador_caja)
        cola_caja.append(turno)
        tiempo_espera = calcular_tiempo_espera(cola_caja, tiempo_caja)
        print(f"\nTurno asignado: {turno}")
        print(f"Tiempo estimado de espera: {tiempo_espera} minutos")
        print(f"Hay {len(cola_caja) - 1} personas delante de ti")

        # Pa que sume
        contador_caja += 1
        total_caja += 1

    elif opcion == "2":

        turno = generar_turno("A", contador_asesoria)
        cola_asesoria.append(turno)
        tiempo_espera = calcular_tiempo_espera(cola_asesoria, tiempo_asesoria)
        print(f"\nTurno asignado: {turno}")
        print(f"Tiempo estimado de espera: {tiempo_espera} minutos")
        print(f"Hay {len(cola_asesoria) - 1} personas delante de ti")

        contador_asesoria += 1
        total_asesoria += 1

    elif opcion == "3":
        turno = generar_turno("R", contador_creditos)
        cola_creditos.append(turno)
        tiempo_espera = calcular_tiempo_espera(cola_creditos, tiempo_creditos)
        print(f"\nTurno asignado: {turno}")
        print(f"Tiempo estimado de espera: {tiempo_espera} minutos")
        print(f"Hay {len(cola_creditos) - 1} personas delante de ti")

        contador_creditos += 1
        total_creditos += 1

    elif opcion == "4":
        tipo = input("¿Qué tipo de turno llamar? (C/A/R): ").upper()

        if tipo == "C":
            if cola_caja:
                turno_llamado = cola_caja.pop(0)
                print(f"Llamando a turno: {turno_llamado}")
            else:
                print("No hay turnos pendientes en CAJA.")
        elif tipo == "A":
            if cola_asesoria:
                turno_llamado = cola_asesoria.pop(0)
                print(f"Llamando a turno: {turno_llamado}")
            else:
                print("No hay turnos pendientes en ASESORÍA.")
        elif tipo == "R":
            if cola_creditos:
                turno_llamado = cola_creditos.pop(0)
                print(f"Llamando a turno: {turno_llamado}")
            else:
                print("No hay turnos pendientes en CRÉDITOS.")
        else:
            print("Tipo inválido. Usa C, A o R.")
    
    elif opcion == "5":
        print("\n--- ESTADO DE COLAS ---")

        # Caja
        print(f"CAJA: {len(cola_caja)} personas esperando ({calcular_tiempo_espera(cola_caja, tiempo_caja)} min de espera)")
        if cola_caja:
            for t in cola_caja:
                print(f"  - {t}")

        # Asesoría
        print(f"ASESORÍA: {len(cola_asesoria)} personas esperando ({calcular_tiempo_espera(cola_asesoria, tiempo_asesoria)} min de espera)")
        if cola_asesoria:
            for t in cola_asesoria:
                print(f"  - {t}")

        # Créditos
        print(f"CRÉDITOS: {len(cola_creditos)} personas esperando ({calcular_tiempo_espera(cola_creditos, tiempo_creditos)} min de espera)")
        if cola_creditos:
            for t in cola_creditos:
                print(f"  - {t}")

    elif opcion == "6":
        total_general = total_caja + total_asesoria + total_creditos
        print("\n--- ESTADÍSTICAS DEL DÍA ---")
        print(f"Total turnos CAJA: {total_caja}")
        print(f"Total turnos ASESORÍA: {total_asesoria}")
        print(f"Total turnos CRÉDITOS: {total_creditos}")
        print(f"TOTAL GENERAL: {total_general} clientes atendidos")
        print("\n Saliendo...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")