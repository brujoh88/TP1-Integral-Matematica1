import recursos
import david

    
#Función principal
def decimal_a_hexadecimal():
    """Convierte un número decimal a hexadecimal"""
    recursos.limpiar_pantalla()
    print("""==== DECIMAL A HEXADECIMAL ====
\nIngrese el número entero positivo que desea convertir a hexadecimal:""")  
    try:
        numero = int(input())
        if numero < 0: #De momento, el programa se limita a números positivos. Se puede ampliar a negativos en el futuro.
            print("Error. El programa solo admite enteros positivos. ")
        else:
            if numero == 0:
                hexadecimal = "0"
            elif numero > 0:
                hexadecimal = david.convertir_decimal_a_eleccion(16, numero) #Se reutiliza la función creada en la sección 2, utilizando base 16 como argumento:
            print(f"\nEl número ingresado es {hexadecimal} en hexadecimal.") #Se imprime el resultado en pantalla
    except ValueError:  #Si se ingresa un valor incorrecto, se imprime un mensaje de error en pantalla y regresa al menú principal:
         print("\nError. Valor incorrecto.")   
    recursos.pausar()


        
