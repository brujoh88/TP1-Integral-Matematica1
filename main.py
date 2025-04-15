import recursos
import gustavo
import david
import dai
import santi
import flor

def main():
    corriendo_programa = True
    """Función principal del programa"""
    while corriendo_programa:
        opcion = recursos.mostrar_menu()
        
        if opcion == "1":
            gustavo.compuertas_logicas()
        elif opcion == "2":
            david.decimal_a_binario()
        elif opcion == "3":
            dai.decimal_a_hexadecimal()
        elif opcion == "4":
            santi.decimal_a_octal()
        elif opcion == "5":
            flor.binario_a_complemento_dos()
        elif opcion == "0":
            recursos.limpiar_pantalla()
            print("Gracias por utilizar el sistema. ¡Hasta pronto!")            
            corriendo_programa = False
        else:
            print("Opción no válida. Intente nuevamente.")
            recursos.pausar()

main()