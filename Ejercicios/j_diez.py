#EJERCICIO 10: Sistema de Inventario de Tienda
# Contexto:
# Administras una pequeña tienda de tecnología y necesitas un sistema para controlar tu inventario. Tienes
# 5 productos diferentes con stock limitado. El sistema debe permitir ventas, reabastecimientos y consultas.
# Productos iniciales:
# Mouse inalámbrico: 15 unidades, $35,000 c/u
# Teclado mecánico: 8 unidades, $180,000 c/u
# Audífonos Bluetooth: 12 unidades, $120,000 c/u
#Webcam HD: 5 unidades, $95,000 c/u
# USB 32GB: 25 unidades, $15,000 c/u
# Tu tarea:
# Crea un programa que:
# 1. Muestre el inventario completo con stock y precios
# 2. Permita realizar ventas (validando que haya stock)
# 3. Calcule el total de la venta (con IVA del 19%)
# 4. Actualice el inventario después de cada venta
# 5. Permita reabastecer productos
# 6. Genere alertas cuando un producto tenga menos de 3 unidades
# 7. Muestre el valor total del inventario
# 8. Muestre un reporte de ventas del día (productos vendidos, cantidad, ingresos totales)
# 9. Identifique el producto más vendido

# Productos iniciales
mouse = 15
teclado = 8
audifonos = 12
webcam = 5
usb = 25

precio_mouse = 35000
precio_teclado = 180000
precio_audifonos = 120000
precio_webcam = 95000
precio_usb = 15000

vendido_mouse = 0
vendido_teclado = 0
vendido_audifonos = 0
vendido_webcam = 0
vendido_usb = 0

opcion = 0
while opcion != 5:
    print("\n TIENDA ")
    print("1. Vender producto")
    print("2. Reabastecer producto")
    print("3. Ver inventario")
    print("4. Ver reporte de ventas")
    print("5. Salir")

    opcion = int(input("Elija una opción: "))

    # VENDER 
    if opcion == 1:
        print("\n1. Mouse inalámbrico\n2. Teclado mecánico\n3. Audífonos Bluetooth\n4. Webcam HD\n5. USB 32GB")
        prod = int(input("¿Qué producto desea vender (1-5)? "))
        cant = int(input("¿Cuántas unidades? "))

        if prod == 1 and cant <= mouse:
            mouse -= cant
            vendido_mouse += cant
            total = int(precio_mouse * cant * 1.19)
            print("Venta exitosa. Total con IVA:", total)
        elif prod == 2 and cant <= teclado:
            teclado -= cant
            vendido_teclado += cant
            total = int(precio_teclado * cant * 1.19)
            print("Venta exitosa. Total con IVA:", total)
        elif prod == 3 and cant <= audifonos:
            audifonos -= cant
            vendido_audifonos += cant
            total = int(precio_audifonos * cant * 1.19)
            print("Venta exitosa. Total con IVA:", total)
        elif prod == 4 and cant <= webcam:
            webcam -= cant
            vendido_webcam += cant
            total = int(precio_webcam * cant * 1.19)
            print("Venta exitosa. Total con IVA:", total)
        elif prod == 5 and cant <= usb:
            usb -= cant
            vendido_usb += cant
            total = int(precio_usb * cant * 1.19)
            print("Venta exitosa. Total con IVA:", total)
        else:
            print("No hay suficiente stock o el producto no existe.")

    elif opcion == 2:
        print("\n1. Mouse\n2. Teclado\n3. Audífonos\n4. Webcam\n5. USB")
        prod = int(input("¿Qué producto desea reabastecer (1-5)? "))
        cant = int(input("¿Cuántas unidades desea agregar? "))

        if prod == 1:
            mouse += cant
        elif prod == 2:
            teclado += cant
        elif prod == 3:
            audifonos += cant
        elif prod == 4:
            webcam += cant
        elif prod == 5:
            usb += cant
        print("Reabastecido correctamente.")

    #  INVENTARIO 
    elif opcion == 3:
        print("\n--- INVENTARIO ---")
        print("Mouse inalámbrico:", mouse, "unidades - Precio:", precio_mouse)
        print("Teclado mecánico:", teclado, "unidades - Precio:", precio_teclado)
        print("Audífonos Bluetooth:", audifonos, "unidades - Precio:", precio_audifonos)
        print("Webcam HD:", webcam, "unidades - Precio:", precio_webcam)
        print("USB 32GB:", usb, "unidades - Precio:", precio_usb)

        total_inventario = (mouse * precio_mouse) + (teclado * precio_teclado) + (audifonos * precio_audifonos) + (webcam * precio_webcam) + (usb * precio_usb)
        print("Valor total del inventario: $", total_inventario)

        if mouse < 3:
            print("Mouse con stock bajo:", mouse)
        if teclado < 3:
            print("Teclado con stock bajo:", teclado)
        if audifonos < 3:
            print("Audífonos con stock bajo:", audifonos)
        if webcam < 3:
            print("Webcam con stock bajo:", webcam)
        if usb < 3:
            print("USB con stock bajo:", usb)

    # REPORTE DE VENTAS
    elif opcion == 4:
        print("\n REPORTE DE VENTAS ")
        total_ventas = (vendido_mouse * precio_mouse) + (vendido_teclado * precio_teclado) + (vendido_audifonos * precio_audifonos) + (vendido_webcam * precio_webcam) + (vendido_usb * precio_usb)
        print("Mouse vendidos:", vendido_mouse)
        print("Teclados vendidos:", vendido_teclado)
        print("Audífonos vendidos:", vendido_audifonos)
        print("Webcams vendidas:", vendido_webcam)
        print("USB vendidos:", vendido_usb)
        print("Total de ventas con IVA:", int(total_ventas * 1.19))

        # Detectar cuál fue el más vendido
        mayor = 0
        producto_mas = ""
        if vendido_mouse > mayor:
            mayor = vendido_mouse
            producto_mas = "Mouse inalámbrico"
        if vendido_teclado > mayor:
            mayor = vendido_teclado
            producto_mas = "Teclado mecánico"
        if vendido_audifonos > mayor:
            mayor = vendido_audifonos
            producto_mas = "Audífonos Bluetooth"
        if vendido_webcam > mayor:
            mayor = vendido_webcam
            producto_mas = "Webcam HD"
        if vendido_usb > mayor:
            mayor = vendido_usb
            producto_mas = "USB 32GB"

        if mayor > 0:
            print("Producto más vendido:", producto_mas, "con", mayor, "unidades.")
        else:
            print("Aún no se han realizado ventas.")

    elif opcion == 5:
        print("Saliendo...")
    else:
        print("Opción no válida.")
