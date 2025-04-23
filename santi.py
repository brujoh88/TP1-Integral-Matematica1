import recursos
import david  # Asegúrate que david.py tiene la función convertir_decimal_a_eleccion

def decimal_a_octal():
    recursos.limpiar_pantalla()
    print("""==== SISTEMA DECIMAL A OCTAL ====
\nIngrese el número entero que desea convertir a octal:""")  

    try: 
        numero = int(input())

        if numero < 0:
            print("\nError. Por favor, ingrese un número entero positivo.")
            recursos.pausar()
            return

        if numero == 0:
            octal = "0"
        else:
            octal = david.convertir_decimal_a_eleccion(8, numero)

        print(f"\nEl número ingresado es {octal} en octal.")
    except ValueError:
        print("\nError. Valor incorrecto.")   

    recursos.pausar()

