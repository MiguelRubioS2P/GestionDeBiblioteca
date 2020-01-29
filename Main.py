def menu():
    print "1 - Mostrar la capacidad de la biblioteca"
    print "2 - Mostrar el nombre d'elements que hi ha en la biblioteca"
    print "3 - Afegir una publicacio a la biblioteca"
    print "4 - Mostrar una publicacio a partir de la seva referencia"
    print "5 - Visualitzar el contingut de la biblioteca"
    print "6 - Salir"


run = False

while not (run):
    menu()
    pregunta = int(input("Di un numero \n"))

    if(pregunta == 6):
        run = True
        print "Adios"
