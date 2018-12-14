"""
    creación de clases
"""

class Persona(object):                                      # Creacion de la Clase Persona
    """
    """
    
    def __init__(self, n, ape, ed, cod,not1,not2):          # Constructor de la clase Persona
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(not1)
        self.nota2 = int(not2)

    def agregar_nombre(self, n):                            # Metodos SET y GET de la clase
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_edad(self, n):
        self.edad = int(n)

    def obtener_edad(self):
        return self.edad
    
    def agregar_codigo(self, n):
        self.codigo = int(n)

    def obtener_codigo(self):
        return self.codigo

    def agregar_codigo(self, ape):
        self.apellido = ape
    
    def obtener_apellido(self):
        return self.apellido

    def agregar_nota1(self,not1):
        self.nota1=int(not1)

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota2(self,not1):
        self.nota2=int(not2)

    def obtener_nota2(self):
        return self.nota2

    
    def __str__(self):                                  # Metodo __str__ de la clase
        return "%s - %s - %d - %d - %d -%d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota1, self.nota2)


class OperacionesPersona(object):                       #Creacion de la clase OperacionesPersona
    """
    """
            
    def __init__(self, listado):                        # Constructor de la clase 
        self.listado_personas = listado

    def obtener_promedio_n1(self):                      # Metodo para calculular el promedio de los estudiantes en nota1 
        suma_n1=0
        print("PROMEDIO NOTAS 1")
        for n in self.listado_personas:
            suma_n1 += n.obtener_nota1()
        return suma_n1/len(self.listado_personas)

    def obtener_promedio_n2(self):                      # Metodo para calculular el promedio de los estudiantes en nota2
        suma_n2=0
        print("PROMEDIO NOTAS 2")
        for n in self.listado_personas:
            suma_n2 += n.obtener_nota2()
        return suma_n2/len(self.listado_personas)

    def obtener_listado_n1(self):                       # Metodo que presenta los estudiantes con nota1 menor a 15
        cadena=""
        print("ESTUDIANTES CON NOTAS MENORES A 15 EN NOTA#1")
        for n in self.listado_personas:
            if (n.obtener_nota1() < 15):
                cadena="%s%s %s\n"%(cadena,n.obtener_nombre(),n.obtener_apellido())
        return cadena

    def obtener_listado_n2(self):                       # Metodo que presenta los estudiantes con nota2 menor a 15
        cadena=""
        print("ESTUDIANTES CON NOTAS MENORES A 15 EN NOTA#2")
        for n in self.listado_personas:
            if (n.obtener_nota2() < 15):
                cadena="%s%s %s\n"%(cadena,n.obtener_nombre(),n.obtener_apellido())
        return cadena

    def obtener_listado_personas(self,a,b):             # Metodo para presentar los estudnates cuyo nombre empieza con R o J
        lista=[]
        print("ESTUDIANTES CON INICIAL R o J")
        for n in self.listado_personas:
            if (a==n.obtener_nombre()[0].upper() or b==n.obtener_nombre()[0].upper()):  # Se compara los parametros con la primera letra del nombre
                nombre="%s %s"%(n.obtener_nombre(),n.obtener_apellido())
                lista.append(nombre)
        return lista

    def __str__(self):                                  # Metodo __str__ de la clase
        cadena=""
        for n in self.listado_personas:
            cadena="%s %s %s\n"%(cadena,n.obtener_nombre(), n.obtener_apellido())
        return cadena
