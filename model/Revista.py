from model.Publicacion import Publicacion


class Revista(Publicacion):
    def __init__(self,any,nro):
        Publicacion.__init__(self)
        self.any = any
        self.nro = nro

    def get_any(self):
        return self.any

    def set_any(self,any):
        self.any = any

    def get_nro(self):
        return self.nro

    def set_nro(self,nro):
        self.nro = nro

    def visualitzar(self):
        Publicacion.visualitzar(self)
        print self.any
        print self.nro