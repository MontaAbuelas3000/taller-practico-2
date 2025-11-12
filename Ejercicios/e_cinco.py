#EJERCICIO 5: Sistema de Reservas de Hotel
# Contexto:
# Administras un pequeño hotel con 20 habitaciones numeradas del 1 al 20. Necesitas un sistema para
# gestionar reservas. Las tarifas son:
# Habitaciones 1-5 (Estándar): $80,000 por noche
# Habitaciones 6-15 (Superior): $120,000 por noche
# Habitaciones 16-20 (Suite): $200,000 por noche
# Además, si la reserva es por más de 3 noches, hay un 10% de descuento.
# Tu tarea:
# Crea un programa que:
# 1. Muestre las habitaciones disponibles (usa una lista)
# 2. Permita al usuario elegir una habitación
# 3. Solicite el número de noches
# 4. Calcule el costo total (con descuento si aplica)
# 5. "Reserve" la habitación (márcarla como ocupada)
# 6. Muestre un resumen de la reserva
# 7. Permita hacer múltiples reservas hasta que no haya habitaciones disponibles o el usuario decida
# salir

#EJERCICIO 5: Sistema de Reservas de Hotel

numero_habitaciones = 20

# Creamos la lista de habitaciones disponibles
habitaciones_disponibles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# funciones

# esta funcion es aquella que nos va dar el valor dependiendo el tipo de habitacion
def obtener_tarifa(numero_habitacion):
    # <= => es el rango en el que debe estar la eleccion 
    if 1 <= numero_habitacion <= 5:
        return 80000, "Estándar"
    elif 6 <= numero_habitacion <= 15:
        return 120000, "Superior"
    elif 16 <= numero_habitacion <= 20:
        return 200000, "Suite"

# calcula el costo total aplicando descuento si aplica
def calcular_costo_total(tarifa, noches):
    subtotal = tarifa * noches
    descuento = 0
    if noches > 3:
        descuento = subtotal * 0.10  
    total = subtotal - descuento
    return subtotal, descuento, total


print("HOTEL X")

while True:
    # Si ya no hay habitaciones, se termina el programa para eso funciona el (not)
    if not habitaciones_disponibles:
        print("No hay más habitaciones disponibles. ¡Hotel lleno!")
        break

    # Mostrar habitaciones disponibles y su tipo
    print("\nHabitaciones disponibles:", habitaciones_disponibles)
    print("Tarifas:")
    print("Habitaciones 1-5 (Estándar): $80,000/noche")
    print("Habitaciones 6-15 (Superior): $120,000/noche")
    print("Habitaciones 16-20 (Suite): $200,000/noche")

    # Pedimos la habitacion que quiere
    habitacion = int(input("\n¿Qué habitación deseas? "))

    # Validamos si está disponible
    if habitacion not in habitaciones_disponibles:
        print("Esa habitación no está disponible")
        continue

    # Pedimos número de noches
    noches = int(input("¿Cuántas noches? "))


    # Obtenemos tarifa y tipo
    tarifa, tipo = obtener_tarifa(habitacion)

    # Calculamos costos
    subtotal, descuento, total = calcular_costo_total(tarifa, noches)

    # Mostramos resumen
    print("\n--- RESUMEN DE RESERVA ---")
    print(f"Habitación: {habitacion} ({tipo})")
    print(f"Noches: {noches}")
    print(f"Tarifa por noche: ${tarifa:,}")
    print(f"Subtotal: ${subtotal:,}")
    print(f"Descuento (10%): -${descuento:,}")
    print(f"TOTAL: ${total:,}")
    print("Reserva confirmada")

    #le decimos que borre la habitacion que se eligio
    habitaciones_disponibles.remove(habitacion)

    # por si quiere hacer otra reserva
    otra = input("¿Hacer otra reserva? (s/n): ")
    if otra == "n":
        print("Saliendo...")
        print("\nSobraron esatas Habitaciones disponibles:", habitaciones_disponibles)
        break