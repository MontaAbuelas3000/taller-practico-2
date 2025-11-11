 #EJERCICIO 1: Sistema de Descuentos de Supermercado
 #Contexto:
 #Trabajas en un supermercado y necesitas implementar el sistema de descuentos automáticos. El
 #supermercado tiene las siguientes promociones:
 #Si el total de la compra es mayor a $100,000: 10% de descuento
 #Si el total es mayor a $200,000: 15% de descuento
 #Si el total es mayor a $300,000: 20% de descuento
 #Además, si el cliente tiene la tarjeta de fidelidad, obtiene un 5% adicional sobre cualquier compra
 #Tu tarea:
 #Crea un programa que:
 #1. Solicite al usuario el total de la compra
 #2. Pregunte si tiene tarjeta de fidelidad s/n
 #3. Calcule el descuento correspondiente
 #4. Muestre el desglose: subtotal, descuento aplicado, y total a pagar

# Ejercicio 1: Sistema de Descuentos de Supermercado (SOLUCION) 

# Pedimos el total
# Utilizamos int para que lea numeros y no caracteres
total_compra = int(input("Ingrese el total de la compra: "))
tarjeta = input("¿Tienes tarjeta de fidelidad? (s/n): ")

descuento_total = 0

# Descuento por monto
# Descuento toral se maneja con += 
# para que cada vez que se haga un descuento se sume a la variable inicial
# Que seria descuento_total = 0

# Empezamos a verificar la informacion por medio del valor ingresado
if total_compra >= 300000:
    descuento_total += total_compra * 0.20
elif total_compra >= 200000:
    descuento_total += total_compra * 0.15
elif total_compra >= 100000:
    descuento_total += total_compra * 0.10

# Descuento por tarjeta
# Se utiliza el descuento_total += ya que sumamos este a los demas descuentos
if tarjeta == "s":
    descuento_total += total_compra * 0.05

# Total a pagar
total_pagar = total_compra - descuento_total

# Imprimimos el resultado
print(f"El valor a pagar es de: ${total_pagar}")







