def ejercicio3():
    n = int(input("Ingrese un numero entre 1 y 10: "))
    m = int(input("Ingrese la linea que desea ver: "))

    try:
        arch = open("tabla-%s.txt" % n, "r")

        lineas = arch.readlines()

        print(lineas[m-1])

        arch.close()

    except:
        print("El archivo no existe o la linea no existe")

ejercicio3()