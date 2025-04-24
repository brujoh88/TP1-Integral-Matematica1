import os

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    limpiar_pantalla()
    print("============================================")
    print("=== SISTEMA DE OPERACIONES Y CONVERSIONES ===")
    print("============================================")
    print("\n1. Compuertas lógicas")
    print("2. Conversión de decimal a binario")
    print("3. Conversión de decimal a hexadecimal")
    print("4. Conversión de decimal a octal")
    print("5. Suma de numeros binarios")
    print("0. Salir")
    
    opcion = input("\nSeleccione una opción: ")
    return opcion

