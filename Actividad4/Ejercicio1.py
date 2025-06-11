# Ejercicio 1: Diario Personal
# • Problema: Escribe un programa que funcione como un diario simple. Cada vez que se
#   ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora
#   actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del
#   archivo sin borrar las anteriores.
# • Paso a paso:
# 1. Importar el módulo datetime para obtener la fecha y hora.
# 2. Solicitar al usuario que ingrese el texto para su entrada del diario.
# 3. Abrir el archivo diario.txt en modo de adición ('a').
# 4. Escribir la fecha y hora actual, seguida de la entrada del usuario. Asegurarse de
#    añadir un salto de línea para separar las entradas.
# 5. Cerrar el archivo.
# 6. Mostrar un mensaje de confirmación al usuario

def dia_hora():
    from datetime import datetime as d
    hoy = d.now()
    return f"Dia: {hoy.day:02}/{hoy.month:02}/{hoy.year} \nHora: {hoy.hour:02}:{hoy.minute:02}:{hoy.second:02}"

def crear_archivo(nombre_archivo,contenido):
    fecha = dia_hora()
    with open(nombre_archivo,"a") as archivo:
        archivo.write(fecha + "\n")
        archivo.write(contenido + "\n")
        archivo.write("----------------------------------------------------\n")

def main():
    import os
    os.system("cls || clear")
    texto = input("Introduzca el texto que desea escribir: ")
    fecha = dia_hora()
    print(fecha)
    print(f"El texto introducido fue: '{texto}'")
    crear_archivo("diario.txt",texto)
    print("Actualizacion guardada con exito en diario.txt")

main()
