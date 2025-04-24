import recursos
import david

def suma_binarios():
    """Suma de numeros binarios"""
    recursos.limpiar_pantalla()
    print("==== SUMA DE NUMEROS BINARIOS ====")
    bin1 = input("Ingrese el primer número binario: ")
    bin2 = input("Ingrese el segundo número binario: ")

    try:
        # Convertimos los binarios a enteros
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)

#Sumamos los enteros
        suma = num1 + num2

#Convertimos el resultado a binario
        resultado_binario = david.convertir_decimal_a_eleccion(2, suma)

        print(f"La suma de {bin1} + {bin2} es: {resultado_binario}")
    except ValueError:
        print("Error: uno o ambos valores no son números binarios válidos.")


    recursos.pausar()