meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio","julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

while True:
    try:
        num_mes = int(input("Ingrese el número del mes (1-12): "))
        nombre_mes = meses[num_mes - 1]
        print("El mes correspondiente es:", nombre_mes)
        break
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except IndexError:
        print("Error: El número de mes debe estar entre 1 y 12.")