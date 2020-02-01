from model.Obra import Obra
from model.Publicacion import Publicacion
from model.Revista import Revista
from model.Volum import Volum


def menu_opcion4(biblioteca):
    """
    Preguntamos por una referencia para despues buscarla en la lista de publicaciones de la biblioteca

    :return: En caso de recibir un no del metodo empleado, devolvemos un mensaje, si es lo contrario devolvemos el objeto
    encontrado en el metodo para que despues se pueda usar el metodo propio de visualitzar()
    """
    # pedimos al usuario que introduzca una referencia
    # referencia = raw_input("Pon una referencia para buscar una publicacion\n")
    referencia = raw_input("Pon una referencia para buscar una publicacion\n")
    # creamos una variable para obtener con el metodo buscar una publicacion
    publicacion = biblioteca.buscar_publicacion(referencia)
    if (publicacion == "No"):
        return None
    else:
        return publicacion

def menu():
    """
    Menu de la aplicacion

    :return: Nada
    """
    print ("1 - Mostrar la capacidad de la biblioteca")
    print ("2 - Mostrar el nombre d'elements que hi ha en la biblioteca")
    print ("3 - Afegir una publicacio a la biblioteca")
    print ("4 - Mostrar una publicacio a partir de la seva referencia")
    print ("5 - Visualitzar el contingut de la biblioteca")
    print ("6 - Salir")


def menu_opcion3(biblioteca):
    pregunta = raw_input("Que desea introducir, Revista, Volum o Obra\n")
    if(pregunta.lower()=="revista"):
        publicacion = datos_publicacion()
        try:
            revista = datos_revista(publicacion)
        except:
            print("No has introducido correctamente los datos")
            menu_opcion3(biblioteca)
        else:
            control = biblioteca.introducir_publicacion(revista)
            if (control):
                print("Se ha introducido correctamente")
            else:
                print("No se ha podido introducir porque ya existe o ya estamos llenos")

    elif(pregunta.lower()=="volum"):
        publicacion = datos_publicacion()
        try:
            obra = datos_obrea(publicacion)
            volum = datos_volum(obra)
        except:
            print("No has introducido correctamente los datos")
        else:
            control = biblioteca.introducir_publicacion(volum)
            if (control):
                print("Se ha introducido correctamente")
            else:
                print("No se ha podido introducir porque ya existe o ya estamos llenos")
    elif(pregunta.lower()=="obra"):
        publicacion = datos_publicacion()
        try:
            obra = datos_obrea(publicacion)
        except:
            print ("No has introducido correctamente los datos")
            menu_opcion3(biblioteca)
        else:
            control = biblioteca.introducir_publicacion(obra)
            if(control):
                print("Se ha introducido correctamente")
            else:
                print("No se ha podido introducir porque ya existe o ya estamos llenos")
    else:
        print("No ha elegido bien")
        menu_opcion3(biblioteca)


def datos_publicacion():
    """
    Pedimos los datos necesarios para poder crear una publicacion

    :return: Objeto tipo Publicacion
    """
    referencia=raw_input("Introduzca una referencia\n")
    titulo = raw_input("Introduzca un titulo\n")
    publicacion = Publicacion(referencia,titulo)
    return publicacion


def datos_revista(publicacion):
    """
    Pedimos los datos necesarios para crear una revista

    :param publicacion: El objeto publicacion para poder usar los getter y crear un nuevo objeto
    :return: Objeto tipo Revista
    """

    any = int(input("Introduzca un numero de any\n"))
    nro = int(input("Introduzca el numero de revistas\n"))
    revista = Revista(publicacion.get_referencia(), publicacion.get_titol(), any, nro)
    return revista


def datos_obrea(publicacion):
    """
    Pedimos los datos necesarios para crear una obra
    :param publicacion: El objeto necesario para usar los getter y crear una obra
    :return: Objeto tipo Obra
    """
    autor = raw_input("Introduzca un autor\n")
    nrePags = int(input("Introduzca el numero de paginas\n"))
    obra = Obra(publicacion.get_referencia(),publicacion.get_titol(),autor,nrePags)
    return obra


def datos_volum(obra):
    """
    Pedimos los datos necesarios para crear un volum

    :param obra: El objeto necesario para usar los getters y crear un volum
    :return: Objeto tipo Volum
    """
    nro = int(input("Introduce el numero de volumenes\n"))
    volum = Volum(obra.get_referencia(),obra.get_titol(),obra.get_autor(),obra.get_nrePags(),nro)
    return volum

