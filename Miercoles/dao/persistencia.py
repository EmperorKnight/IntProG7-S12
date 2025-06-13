class persistenciaDao:
    def __init__(self,ruta_archivo):
        self.ruta_archivo = ruta_archivo
    
    def abrir_archivo(self):
        try:
            with open(self.ruta_archivo,"r") as archivo:
                self.registro = eval(archivo.read())
        except FileNotFoundError:
            self.registro = []
    
    def guardar_archivo(self,texto =None):
        with open(self.ruta_archivo,"w") as archivo:
            archivo.write(str(self.registro))