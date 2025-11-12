#EJERCICIO 8: Simulador de Cajero Automático Completo
# Contexto:
# Necesitas crear un simulador realista de cajero automático. El cajero tiene las siguientes características:
# Saldo inicial: $1,000,000
# Límite de retiro por transacción: $400,000
# Costo por retiro: $2,500 (si retira más de 3 veces al mes)
# Se puede consignar dinero sin límite
# Se puede transferir a otros números de cuenta
# Genera un número de referencia único para cada transacción
# Tu tarea:
#Crea un programa que:
# 1. Solicite un PIN de 4 dígitos para acceder (intenta usar 1234)
# 2. Muestre un menú con opciones: consultar saldo, retirar, consignar, transferir, salir
# 3. Valide cada operación (saldo suficiente, límites, etc.)
# 4. Cobre la comisión después del tercer retiro del mes
# 5. Genere un número de referencia aleatorio de 10 dígitos para cada transacción
# 6. Muestre un comprobante después de cada operación
# 7. Permita máximo 3 intentos de PIN incorrectos antes de bloquear

#EJERCICIO 8: Simulador de Cajero Automático Completo

saldo = 1000000
pin_correcto = "1234"
retiros_del_mes = 0
contador_referencia = 1000000000  # Comienza desde este número


#funciones

def validar_pin():
    #Valida el PIN del usuario con máximo 3 intentos.
    intentos = 0
    while intentos < 3:
        pin = input("Ingresa tu PIN de 4 dígitos: ")
        if pin == pin_correcto:
            print("\nPIN correcto\n")
            return True
        else:
            intentos += 1
            print("PIN incorrecto. Intento", intentos, "de 3.")
    print("\nCuenta bloqueada por exceso de intentos.")
    return False


def consultar_saldo(saldo):
    #Muestra el saldo disponible.
    print(f"\nTu saldo actual es: ${saldo}\n")


def generar_referencia():
    #Genera una referencia única de transacción sin usar random.
    global contador_referencia
    contador_referencia += 1
    return contador_referencia


def retirar_dinero(saldo, retiros):
    #Permite retirar dinero validando límites y comisión.
    LIMITE_RETIRO = 400000
    COMISION = 2500

    try:
        monto = int(input("Monto a retirar (múltiplo de 10,000): "))
    except ValueError:
        print("Monto inválido.")
        return saldo, retiros

    if monto % 10000 != 0:
        print("El monto debe ser múltiplo de $10,000.")
        return saldo, retiros

    if monto > LIMITE_RETIRO:
        print("No puedes retirar más de $400,000 por transacción.")
        return saldo, retiros

    if monto > saldo:
        print("Saldo insuficiente.")
        return saldo, retiros

    retiros += 1
    comision = COMISION if retiros > 3 else 0
    saldo_final = saldo - monto - comision

    if saldo_final < 0:
        print("No tienes suficiente saldo para cubrir la comisión.")
        return saldo, retiros - 1

    referencia = generar_referencia()
    generar_comprobante("RETIRO", monto, referencia, saldo, saldo_final, comision, retiros)
    return saldo_final, retiros


def consignar_dinero(saldo):
    #Permite consignar dinero al saldo.
    try:
        monto = int(input("Monto a consignar: "))
    except ValueError:
        print( "Monto inválido.")
        return saldo

    if monto <= 0:
        print("El monto debe ser positivo.")
        return saldo

    saldo_final = saldo + monto
    referencia = generar_referencia()
    generar_comprobante("CONSIGNACIÓN", monto, referencia, saldo, saldo_final)
    return saldo_final


def transferir(saldo):
    """Permite transferir dinero a otra cuenta."""
    cuenta_destino = input("Número de cuenta destino: ")
    try:
        monto = int(input("Monto a transferir: "))
    except ValueError:
        print("Monto inválido.")
        return saldo

    if monto % 10000 != 0:
        print("El monto debe ser múltiplo de $10,000.")
        return saldo

    if monto > saldo:
        print("Saldo insuficiente.")
        return saldo

    saldo_final = saldo - monto
    referencia = generar_referencia()
    generar_comprobante("TRANSFERENCIA", monto, referencia, saldo, saldo_final, 0, 0, cuenta_destino)
    return saldo_final


def generar_comprobante(tipo, monto, referencia, saldo_anterior, saldo_final, comision=0, retiros=0, cuenta_destino=None):
    # Muestra un comprobante de la transacción sin usar fecha real.
    # Fecha simulada: podríamos ir sumando “días” cada vez
    generar_comprobante.fecha_falsa += 1
    fecha = f"2025-11-{generar_comprobante.fecha_falsa:02d} 14:30"

    print("\nCOMPROBANTE DE TRANSACCIÓN")
    print(f"Tipo: {tipo}")
    print(f"Monto: ${monto}")
    if cuenta_destino:
        print(f"Cuenta destino: {cuenta_destino}")
    print(f"Comisión: ${comision}")
    print(f"Referencia: {referencia}")
    print(f"Fecha: {fecha}")
    print(f"Saldo anterior: ${saldo_anterior}")
    print(f"Saldo actual: ${saldo_final}")
    if tipo == "RETIRO":
        print(f"Retiros este mes: {retiros}/3 gratis")
    print("")
    print("\nGracias por usar nuestro cajero\n")

# Atributo para manejar la fecha simulada
generar_comprobante.fecha_falsa = 8  # Empieza desde el día 8, por ejemplo


# --- PROGRAMA PRINCIPAL ---

if validar_pin():
    while True:
        print(" MENÚ ")
        print("\n1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Consignar dinero")
        print("4. Transferir")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo, retiros_del_mes = retirar_dinero(saldo, retiros_del_mes)
        elif opcion == "3":
            saldo = consignar_dinero(saldo)
        elif opcion == "4":
            saldo = transferir(saldo)
        elif opcion == "5":
            print("\nSaliendo del sistema... ¡Gracias por usar nuestro cajero! 👋")
            break
        else:
            print("⚠️ Opción inválida, intenta de nuevo.")

        continuar = input("¿Deseas realizar otra transacción? (s/n): ").lower()
        if continuar != "s":
            print("\nSesión finalizada. 🏧")
            break