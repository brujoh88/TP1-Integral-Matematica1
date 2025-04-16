import recursos
import flor

#Funcion a usar si es un número positivo
def positivo_a_binario(numero):
    binario = ""
    while numero > 0:
            resto = str(numero % 2)
            numero = numero // 2
            binario = resto + binario
    return binario

#Funcion a usar si es negativo (falta la funcion de complemento a2)
#def negativo_a_binario(numero):
    bits = int(input("Ingrese la cantidad de bits: "))
    bin_del_absoluto = positivo_a_binario(abs(numero))
    while len(bin_del_absoluto) < bits:    #Se agregan ceros hasta completar la cantidad de bits
         bin_del_absoluto = "0" + str(bin_del_absoluto)
    binario = flor.binario_a_complemento_dos(bin_del_absoluto)
    return binario

#Función principal que solicita el dato al usuario y al final mostrará el resultado en pantalla.
def decimal_a_binario():
    recursos.limpiar_pantalla()
    print("""==== DECIMAL A BINARIO ==== 
    Ingrese el número natural que desea convertir a binario:""")   
    numero = int(input())
    if numero == 0:
        binario = "0"
    #elif numero < 0:
        #binario = negativo_a_binario(numero)
    else:
        binario = positivo_a_binario(numero)
       
    print(f"El número decimal ingresado es {binario} en binario.")
    
    recursos.pausar()
    
