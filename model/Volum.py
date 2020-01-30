from model.Obra import Obra


class Volum(Obra):
    def __init__(self,referencia,titol,autor,nrePags,nro):
        Obra.__init__(self,referencia,titol,autor,nrePags)
        self.nro = nro

    def get_nro(self):
        return self.nro

    def set_nro(self,nro):
        self.nro = nro

    def visualitzar(self):
        print "{} {} {} {} {}".format(self.referencia,self.titol,self.autor,self.nrePags,self.nro)