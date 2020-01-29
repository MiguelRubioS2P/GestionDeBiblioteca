from model.Obra import Obra


class Volum(Obra):
    def __init__(self,nro):
        Obra.__init__(self)
        self.nro = nro

    def get_nro(self):
        return self.nro

    def set_nro(self,nro):
        self.nro = nro

    def visualitzar(self):
        Obra.visualitzar(self)
        print self.nro