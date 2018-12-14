import codecs
import sys

class MiArchivo:                            # Clase MiArchivo
    """
    """
    
    def __init__(self):                     # Constructor de la clase
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r")  # Abrimos el archivo csv

    def obtener_informacion(self):          # Metodos para leer las lineas del archivo
        return self.archivo.readlines()

    def cerrar_archivo(self):               # Metodo para cerrar el Archivo
        self.archivo.close()


class MiArchivoEscribir:                    
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()
