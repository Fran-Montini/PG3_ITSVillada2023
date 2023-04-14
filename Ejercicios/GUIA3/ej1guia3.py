while True:
    try:
        num1 = int(input("Ingrese el primer numero entero: "))
        num2 = int(input("Ingrese el segundo numero entero: "))
        suma = num1 + num2
        print("La suma es:", suma)
        opcion = input("¿Desea seguir sumando valores? (s/n): ")
        if opcion != 's':
            break
    except ValueError:
        print("Error: Debe ingresar un numero  entero.")