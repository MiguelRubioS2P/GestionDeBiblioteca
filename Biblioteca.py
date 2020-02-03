class Biblioteca():

    # metodos
    # conocer la capacidad de la biblioteca (listo)
    # conocer el numero de elementos que tiene la biblioteca (listo)
    # introducir una publicacion (listo)
    # buscar una publicacion por su referencia (listo)
    # mostrar una publicacion por su referencia (listo)
    # visualizar el contenido de la biblioteca (listo)

    publicaciones = []

    def __init__(self,capacitat):
        self.capacitat = capacitat

    def get_capacitat(self):
        return self.capacitat

    def total_elementos(self):
        """
        Devuelve el total de elementos que tiene la lista de publicaciones

        :return: Int
        """
        return len(self.publicaciones)

    def introducir_publicacion(self,publicacion):
        """
        Introducir una publicacion a la lista de publicaciones

        :param publicacion: La publicacion que queremos agregar a la lista
        :return: Boolean
        """

        if(self.get_capacitat() == self.total_elementos()):
            return False

        for p in self.publicaciones:
            if(p == publicacion.get_referencia()):
                return False

        self.publicaciones.append(publicacion)
        return True

    def buscar_publicacion(self,referencia):
        """
        Buscamos la publicacion que nos indican pasandonos la referencia

        :param referencia: La referencia que queremos comparar
        :return: El objeto
        """

        for p in self.publicaciones:
            if(p == referencia):
                return p
        return "No"

    def mostrar_publicacion(self,referencia):
        """
        Mostramos la informacion del objeto que recuperamos

        :param referencia: La referencia que queremos comparar
        :return:
        """
        for p in self.publicaciones:
            if(p == referencia):
                p.visualitzar()

    def visualitzar(self,biblioteca):
        """
        Visualizar las publicaciones, Controlamos que hay elementos y despues mostramos o los datos o un mensaje de que no hay nada.

        :param biblioteca: Objeto biblioteca
        :return: Nada
        """
        if(biblioteca.total_elementos()==0):
            print "No hay valores que mostrar"
        else:
            for p in self.publicaciones:
                print (p.visualitzar())