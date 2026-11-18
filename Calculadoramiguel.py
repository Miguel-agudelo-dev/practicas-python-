while True:
    print("\n--- MI CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    num1 = float(input("Escribe el primer número: "))
    num2 = float(input("Escribe el segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)
    elif opcion == "2":
        print("Resultado:", num1 - num2)
    elif opcion == "3":
        print("Resultado:", num1 * num2)
    elif opcion == "4":
        print("Resultado:", num1 / num2)
    else:
        print("Opción no válida")
