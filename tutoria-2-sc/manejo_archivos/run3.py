from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona         # Importamos los modulos que utilizaremos 

m = MiArchivo()                                                    # Instanciamos el objeto MiArchivo 
lista = m.obtener_informacion()                                    # Declaramos una lista y llamamos al metodo obtener_informacion
lista = [l.split("|") for l in lista]                               # Dividimos cada cadena de la lista por el caracter "|"

# print(lista)

lista = lista[1:]                                               # Inicializamos la lista desde el elemeno 1
lista_personas = []                                             # Declaramos una lista vacia
for d in lista:                                                 # recorremos la lista
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4] , d[5])            # Creamos un objeto Persona y le enviamos parametros
    lista_personas.append(p)                                    # Agregamos el objeto a la lista

operaciones = OperacionesPersona(lista_personas)                # Instanciamos el metodo OperacionPerona
print("LISTADO DE ESTUDIANTES")                                 # Presentamos un encabezado
print(operaciones)                                              # Presentamos el metodo __str__ de la clase
print(operaciones.obtener_promedio_n1())                        # Llamamos a las funciones creadas
print(operaciones.obtener_promedio_n2())
print(operaciones.obtener_listado_n1())
print(operaciones.obtener_listado_n2())
print(operaciones.obtener_listado_personas("R", "J"))