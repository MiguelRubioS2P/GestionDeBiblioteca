from Biblioteca import Biblioteca
from utilidades.auxiliar import menu_opcion4, menu, menu_opcion3

# controlar excepcion de introducir string cuando estamos pidiendo un numero para la opcion del menu
run = False
biblioteca = Biblioteca(10)

while not (run):
    menu()
    try:
        pregunta = int(input("Di un numero \n"))
        if (pregunta == 1):
            print ("La capacidad es de {}".format(biblioteca.get_capacitat()))
        if (pregunta == 2):
            print ("El numero de elementos es: {}".format(biblioteca.total_elementos()))
        if (pregunta == 3):
            try:
                menu_opcion3(biblioteca)
            except:
                print("Ha ocurrido un error a la hora de introducir una publicacion")
        if (pregunta == 4):
            publicacion = menu_opcion4(biblioteca)
            if (publicacion == None):
                print("No se ha podido encontrar la publicacion que desea buscar")
            else:
                print(publicacion.visualitzar())
        if (pregunta == 5):
            biblioteca.visualitzar(biblioteca)
        if (pregunta == 6):
            run = True
            print ("Adios, vuelva cuando quiera.")
        if(pregunta > 6):
            print("Ese valor no tiene una opcion en el menu, prueba con otro")
    except:
        print("No has introducido un numero")
