class Biblioteca():

    # metodos
    # conocer la capacidad de la biblioteca (listo)
    # conocer el numero de elementos que tiene la biblioteca (listo)
    # introducir una publicacion (listo)
    # mostrar una publicacion por su referencia (listo)
    # visualizar el contenido de la biblioteca (listo)

    publicaciones = []

    def __init__(self,capacitat):
        self.capacitat = capacitat

    def get_capacitat(self):
        return self.capacitat

    def total_elementos(self):
        return len(self.publicaciones)

    def introducir_publicacion(self,publicacion):
        self.publicaciones.append(publicacion)

    def mostrar_publicacion(self,referencia):
        for p in self.publicaciones:
            if(p==referencia):
                return p
        return "No hemos tenido coincidencias"

    def visualitzar(self):
        for p in self.publicaciones:
            print p.visualitzar()
