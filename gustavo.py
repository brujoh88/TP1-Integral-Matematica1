import recursos

def compuertas_logicas():
    """Función para manejar operaciones con compuertas lógicas"""
    recursos.limpiar_pantalla()
    print("==== COMPUERTAS LÓGICAS ====")
    print("\n1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. NAND")
    print("6. NOR")
    print("0. Volver al menú principal")
    
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == "0":
        return
    
    if opcion in ["1", "2", "4", "5", "6"]:
        try:
            a = int(input("Ingrese el primer valor (0 o 1): "))
            b = int(input("Ingrese el segundo valor (0 o 1): "))
            
            if a not in [0, 1] or b not in [0, 1]:
                print("Error: Los valores deben ser 0 o 1")
                recursos.pausar()
                return compuertas_logicas()
                
            if opcion == "1":  # AND
                resultado = a and b
                print(f"\n{a} AND {b} = {resultado}")
            elif opcion == "2":  # OR
                resultado = a or b
                print(f"\n{a} OR {b} = {resultado}")
            elif opcion == "4":  # XOR
                resultado = a ^ b
                print(f"\n{a} XOR {b} = {resultado}")
            elif opcion == "5":  # NAND
                resultado = not (a and b)
                print(f"\n{a} NAND {b} = {int(resultado)}")
            elif opcion == "6":  # NOR
                resultado = not (a or b)
                print(f"\n{a} NOR {b} = {int(resultado)}")
        except ValueError:
            print("Error: Debe ingresar valores numéricos")
    
    elif opcion == "3":  # NOT
        try:
            a = int(input("Ingrese el valor (0 o 1): "))
            
            if a not in [0, 1]:
                print("Error: El valor debe ser 0 o 1")
                recursos.pausar()
                return compuertas_logicas()
                
            resultado = not a
            print(f"\nNOT {a} = {int(resultado)}")
        except ValueError:
            print("Error: Debe ingresar un valor numérico")
    
    else:
        print("Opción no válida")
    
    recursos.pausar()
    compuertas_logicas()