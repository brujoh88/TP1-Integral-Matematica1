import recursos  # Importamos el módulo de recursos del equipo

def entero_a_hexadecimal(numero):
    """Convierte un número entero a su representación hexadecimal"""
    caracteres_hex = "0123456789ABCDEF"
    resultado = ""

    if numero == 0:
        return "0"

    while numero > 0:
        residuo = numero % 16
        resultado = caracteres_hex[residuo] + resultado
        numero //= 16

    return resultado

def decimal_a_hexadecimal():
    """Convierte un número entero a hexadecimal y muestra el resultado"""
    recursos.limpiar_pantalla()
    print("==== DECIMAL A HEXADECIMAL ====")

    entrada = input("Introduce un número entero: ")

    if not entrada:
        print("Error: La entrada no puede estar vacía.")
        recursos.pausar()
        return
    
    if not entrada.isdigit():  # Verifica que la entrada sea un número entero
        print("Error: Debes ingresar un número entero válido.")
        recursos.pausar()
        return

    numero_entero = int(entrada)
    hex_entero = entero_a_hexadecimal(numero_entero)

    print(f"El número {numero_entero} en hexadecimal es: {hex_entero}")

    recursos.pausar()
