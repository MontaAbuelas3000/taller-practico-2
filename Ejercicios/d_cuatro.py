#EJERCICIO 4: Validador de Contraseñas Seguras
# Contexto:
# Estás desarrollando el sistema de registro de una aplicación y necesitas validar que las contraseñas de los
# usuarios sean seguras. Una contraseña segura debe cumplir:
# Tener al menos 8 caracteres
# Contener al menos una letra mayúscula
# Contener al menos una letra minúscula
# Contener al menos un número
# Contener al menos un carácter especial (!@#$%^&*)
# No contener espacios
# Tu tarea:
# Crea un programa que:
# 1. Solicite al usuario crear una contraseña
# 2. Valide cada uno de los requisitos
# 3. Muestre qué requisitos cumple y cuáles no
# 4. Si no cumple todos, solicite una nueva contraseña
# 5. Continúe hasta que la contraseña sea válida
# 6. Muestre un mensaje de éxito con una calificación de seguridad

#EJERCICIO 4: Validador de Contraseñas Seguras

#APLICACION DE TRUE Y FALSE

# funciones
def tiene_longitud_minima(contraseña):
    # Verifica que la contraseña tenga 8 o más caracteres
    return len(contraseña) >= 8

def tiene_mayuscula(contraseña):
    # mira si hay al menos una mayúscula 
    for caracter in contraseña:
        if caracter.isupper():  # .isupper() verifica si una letra está en mayúscula
            return True
        #estos retrun me toco averiguar en copilot porque antes de ellos no me daba el sistema
    return False

def tiene_minuscula(contraseña):
    # Recorre cada carácter y mira si hay al menos una minúscula
    for caracter in contraseña:
        if caracter.islower():  # .islower() verifica si una letra está en minúscula
            return True
    return False

def tiene_numero(contraseña):
    # Recorre cada carácter y mira si hay un número
    for caracter in contraseña:
        if caracter.isdigit():  # .isdigit() verifica si es un número (0-9)
            return True
    return False

# Para todos los .is tuve que investigar y ver como se apliaban

def tiene_caracter_especial(contraseña):
    # lista de caracteres especiales aceptados
    especiales = "!@#$%^&*"
    for caracter in contraseña:
        if caracter in especiales:  # Verifica si el carácter pertenece a la lista
            return True
    return False

def no_tiene_espacios(contraseña):
    # Si hay un espacio en blanco te jodes jajaj
    return " " not in contraseña

# Usamos un ciclo while que seguirá repitiéndose
# hasta que la contraseña cumpla todos los requisitos
while True:
    contraseña = input("Crea tu contraseña: ")  # Pedimos la contraseña al usuario

    # Verificamos cada condición por separado con las funciones creadas
    largo = tiene_longitud_minima(contraseña)
    mayus = tiene_mayuscula(contraseña)
    minus = tiene_minuscula(contraseña)
    numero = tiene_numero(contraseña)
    especial = tiene_caracter_especial(contraseña)
    sin_espacios = no_tiene_espacios(contraseña)

    # resultado de cada validación pa que el sepa si esta bien o mal
    print("Longitud mínima (8 caracteres):", "Bien" if largo else "Intente de nuevo")
    print("Contiene mayúscula:", "Bien" if mayus else "Intente de nuevo")
    print("Contiene minúscula:", "Bien" if minus else "Intente de nuevo")
    print("Contiene número:", "Bien" if numero else "Intente de nuevo")
    print("Contiene carácter especial (!@#$%^&*):", "Bien" if especial else "Intente de nuevo")
    print("No contiene espacios:", "Bien" if sin_espacios else "Intente de nuevo")

    # Si todas las condiciones son verdaderas, la contraseña es segura
    if largo and mayus and minus and numero and especial and sin_espacios:
        print("\n¡Contraseña SEGURA! Nivel de seguridad: ALTA ")
        break  # Rompe el ciclo y termina el programa
    else:
        print("\nTu contraseña NO es segura. Intenta de nuevo.\n")
