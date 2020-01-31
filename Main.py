from Biblioteca import Biblioteca
from model.Obra import Obra
from model.Revista import Revista
from model.Volum import Volum


def menu():
    print "1 - Mostrar la capacidad de la biblioteca"
    print "2 - Mostrar el nombre d'elements que hi ha en la biblioteca"
    print "3 - Afegir una publicacio a la biblioteca"
    print "4 - Mostrar una publicacio a partir de la seva referencia"
    print "5 - Visualitzar el contingut de la biblioteca"
    print "6 - Salir"

def metodo4():

    # pedimos al usuario que introduzca una referencia
    referencia = raw_input("Pon una referencia para buscar una publicacion\n")
    # creamos una variable para obtener con el metodo buscar una publicacion
    publicacion = biblioteca.buscar_publicacion(referencia)
    if(publicacion == "No"):
        return "No se ha podido encontrar"
    else:
        return publicacion

def metodo3():
    # solo podemos agregar volum, obra, revista
    pregunta_tipo = raw_input("Que desea introducir una revista, un volum o una obra\n")
    if(pregunta_tipo.lower() == "revista"):
        # hacer cosas de revistas
        referencia = raw_input("Introduzca una referencia\n")
        titulo = raw_input("Introduzca un titulo\n")
        any = int(input("Introduzca el dia del any\n"))
        nro = int(input("Introduzca el numero de revistas\n"))
        revista = Revista(referencia,titulo,any,nro)
        biblioteca.introducir_publicacion(revista)
        # introducir y controlar errores
    elif(pregunta_tipo.lower() == "obra"):
        # hacer cosas de obras
        referencia = raw_input("Introduzca una referencia\n")
        titulo = raw_input("Introduzca un titulo\n")
        autor = raw_input("Introduzca un autor\n")
        nrePags = int(input("Introduzca el numero de paginas\n"))
        obra = Obra(referencia,titulo,autor,nrePags)
        biblioteca.introducir_publicacion(obra)
        # introducir y controlar errores
    elif(pregunta_tipo.lower() == "volum"):
        # hacer cosas de volum
        referencia = raw_input("Introduzca una referencia\n")
        titulo = raw_input("Introduzca un titulo\n")
        autor = raw_input("Introduzca un autor\n")
        nrePags = int(input("Introduzca el numero de paginas\n"))
        nro = int(input("Introduzca el numero de volumenes"))
        volum = Volum(referencia,titulo,autor,nrePags,nro)
        biblioteca.introducir_publicacion(volum)
        # introducir y controlar errores
    else:
        # repetir
        print "Tenias que elegir"




run = False
biblioteca = Biblioteca(10)

while not (run):
    menu()
    pregunta = int(input("Di un numero \n"))
    if(pregunta == 1):
        print biblioteca.get_capacitat()
    if(pregunta == 2):
        print biblioteca.total_elementos()
    if(pregunta == 3):
        metodo3()
    if(pregunta == 4):
        resultado_metodo = metodo4()
        resultado_metodo.visualitzar()
    if(pregunta == 5):
        biblioteca.visualitzar()
    if(pregunta == 6):
        run = True
        print "Adios"
