from urllib.request import urlopen

def ejercicio4():
    url = input("Ingrese la URL: ")

    arch = urlopen(url)

    texto = arch.read().decode("utf-8")

    palabras = texto.split()

    print("Cantidad de palabras:", len(palabras))

    arch.close()

ejercicio4()