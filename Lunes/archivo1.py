import os
try:
    os.system("cls || clear")
    mi_archivo = open("C:\\Users\\USUARIO\\Documents\\my_file.txt","r")
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada")