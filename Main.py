from Biblioteca import Biblioteca
from model.Publicacion import Publicacion
from model.Revista import Revista
from model.Volum import Volum


def menu():
    print "1 - Mostrar la capacidad de la biblioteca"
    print "2 - Mostrar el nombre d'elements que hi ha en la biblioteca"
    print "3 - Afegir una publicacio a la biblioteca"
    print "4 - Mostrar una publicacio a partir de la seva referencia"
    print "5 - Visualitzar el contingut de la biblioteca"
    print "6 - Salir"


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
        volum = Volum(1,"Prueba","Miguel",200,30)
        biblioteca.introducir_publicacion(volum)
    if(pregunta == 4):
        publicacion = biblioteca.buscar_publicacion(1)
        if(publicacion == "No"):
            print "No se ha podido encontrar"
        else:
            print publicacion.visualitzar()
    if(pregunta == 5):
        biblioteca.visualitzar()
    if(pregunta == 6):
        run = True
        print "Adios"
