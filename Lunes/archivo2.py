import os

os.system("cls || clear")
archivo = open("my_file.txt","r")
texto_ini = archivo.read()
archivo = open("my_file.txt","w")
archivo.close()
texto = input("Escribe el texto que quieres guadar en el archivo \n-> ")
archivo = open("my_file.txt","w")
archivo.write(texto_ini)
archivo.write("\n")
archivo.write(texto)
archivo.close()