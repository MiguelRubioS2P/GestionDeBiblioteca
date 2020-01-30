from model.Publicacion import Publicacion

class Obra(Publicacion):

    def __init__(self,referencia,titol,autor,nrePags):
        """
        Constructor con herencia de Publicacion

        :param referencia:
        :param titol:
        :param autor:
        :param nrePags:
        """
        Publicacion.__init__(self,referencia,titol)
        self.autor = autor
        self.nrePags = nrePags

    def get_autor(self):
        """
        Getter del atributo autor

        :return: Atributo autor
        """
        return self.autor

    def set_autor(self,autor):
        """
        Setter del atributo autor

        :param autor: Nuevo valor para el atributo autor
        :return: Nada
        """
        self.autor = autor

    def get_nrePags(self):
        """
        Getter del atributo nrePags

        :return: Atributo nrePags
        """
        return self.nrePags

    def set_nrePags(self,nrePags):
        """
        Setter del atributo nrePags

        :param nrePags: Nuevo valor para el atributo nrePags
        :return: Nada
        """
        self.nrePags = nrePags

    def visualitzar(self):
        """
        Metodo sobreescrito para mostrar los datos del objeto

        :return: String con la informacion del objeto
        """
        print "{} {} {} {}".format(self.referencia,self.titol,self.autor,self.nrePags)
