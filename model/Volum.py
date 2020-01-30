from model.Obra import Obra


class Volum(Obra):
    def __init__(self,referencia,titol,autor,nrePags,nro):
        """
        Constructor con herencia de obra

        :param referencia:
        :param titol:
        :param autor:
        :param nrePags:
        :param nro:
        """
        Obra.__init__(self,referencia,titol,autor,nrePags)
        self.nro = nro

    def get_nro(self):
        """
        Getter del atributo de nro

        :return: Devuelve el atributo de nro
        """
        return self.nro

    def set_nro(self,nro):
        """
        Setter del atributo de nro

        :param nro: Nuevo valor para el atributo nro
        :return:
        """
        self.nro = nro

    def visualitzar(self):
        """
        Metodo para visualizar toda la informacion del objeto Volum
        
        :return: String de la informacion del objeto Volum
        """
        print "{} {} {} {} {}".format(self.referencia,self.titol,self.autor,self.nrePags,self.nro)