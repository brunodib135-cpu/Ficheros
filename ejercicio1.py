def ejercicio1():
    n = int(input("Ingrese un numero entre 1 y 10: "))

    arch = open("tabla-%s.txt" % n, "w")

    for i in range(1, 11):
        arch.write("%s x %s = %s\n" % (n, i, n*i))

    arch.close()

ejercicio1()