# Ejercicio 2: Contador de Líneas
# • Problema: Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El
# programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene.
# Debe manejar el error en caso de que el archivo no exista.
# • Paso a paso:
# 1. Solicitar al usuario el nombre del archivo (ej: poema.txt).
# 2. Usar un bloque try...except para manejar la excepción FileNotFoundError.
# 3. Dentro del try, abrir el archivo en modo lectura ('r').
# 4. Utilizar el método readlines() para leer todas las líneas en una lista.
# 5. Calcular la longitud de la lista (que es igual al número de líneas) y mostrarla.
# 6. En el bloque except, si el archivo no se encuentra, imprimir un mensaje de error
# amigable.

import os

os.system("cls || clear")
nombre_archivo = input("Escriba el nombre del archivo: ")

try:
    with open(nombre_archivo,"r") as archivo:
        archivo1 = archivo.readlines()
    print(f"El archivo contiene {len(archivo1)} lineas en total")
except FileNotFoundError:
    print("Por desgracia, el archivo que busca no existe")