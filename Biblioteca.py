class Biblioteca():
    # No se debe poder agregar dos publicaciones con la misma referencia
    # No se puede tener mas publicaciones mas que la capacidad

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
        return len(self.publicaciones)

    def introducir_publicacion(self,publicacion):
        self.publicaciones.append(publicacion)

    def buscar_publicacion(self,referencia):
        for p in self.publicaciones:
            if(p == referencia):
                return p
        return "No"

    def mostrar_publicacion(self,referencia):
        for p in self.publicaciones:
            if(p == referencia):
                p.visualitzar()

    def visualitzar(self):
        for p in self.publicaciones:
            p.visualitzar()