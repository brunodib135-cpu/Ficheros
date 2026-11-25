def ejercicio2():
    n = int(input("Ingrese un numero entre 1 y 10: "))

    try:
        arch = open("tabla-%s.txt" % n, "r")

        for linea in arch:
            print(linea, end="")

        arch.close()

    except:
        print("El archivo no existe")

ejercicio2()