import recursos

#Función que permite convertir números del sistema decimal a sistema binario, octal o hexadecimal, y devuelve el valor como cadena:
#argumento "sistema" debe ser la base del sistema numérico al que se convertirá(2, 8 o 16). "numero" es el número decimal a convertir.
def convertir_decimal_a_eleccion(sistema, numero):  
    conversion = ""
    while numero > 0:
        resto = (numero % sistema)
        caracteres = "0123456789ABCDEF"
        numero = numero // sistema
        conversion = caracteres[resto] + conversion
    return conversion

#Funcion a usar si es un número positivo
def positivo_a_binario(numero):
    binario = convertir_decimal_a_eleccion(2, numero)
    return binario

#Función principal que solicita el dato al usuario y al final mostrará el resultado en pantalla.
def decimal_a_binario():
    recursos.limpiar_pantalla()
    print("""====SISTEMA DECIMAL A BINARIO ==== 
\nIngrese el número entero positivo que desea convertir a binario:""")  
    try: 
        numero = int(input())
        if numero < 0:
            print("Error. De momento el programa solo acepta números positivos.")
        else:
            if numero == 0:
                binario = "0"
            else:
                binario = positivo_a_binario(numero)       
            print(f"\nEl número decimal {numero}  es {binario} en binario.")
    except ValueError:
         print("\nError. Valor incorrecto.")   
    recursos.pausar()
    

