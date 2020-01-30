from model.Publicacion import Publicacion


class Revista(Publicacion):
    def __init__(self,referencia,titol,any,nro):
        """
        Constructor con herencia de Publicacion

        :param referencia:
        :param titol:
        :param any:
        :param nro:
        """
        Publicacion.__init__(self,referencia,titol)
        self.any = any
        self.nro = nro

    def get_any(self):
        """
        Getter del atributo any

        :return: Valor del atributo any
        """
        return self.any

    def set_any(self,any):
        """
        Setter del atributo any

        :param any: Nuevo valor para el atributo any
        :return: Nada
        """
        self.any = any

    def get_nro(self):
        """
        Getter del atributo nro

        :return: Valor del atributo nro
        """
        return self.nro

    def set_nro(self,nro):
        """
        Setter del atributo nro

        :param nro: Nuevo valor para el atributo nro
        :return: Nada
        """
        self.nro = nro

    def visualitzar(self):
        """
        Metodo con sobreescritura para visualizar los datos del objeto

        :return: String con la informacion del objeto
        """
        print "{} {} {} {}".format(self.referencia,self.titol,self.any,self.nro)
