class Publicacion():
    # Constructor
    def __init__(self,referencia,titol):
        self.referencia = referencia
        self.titol = titol

    # Bloque de trato de referencia
    def get_referencia(self):
        return self.referencia

    def set_referencia(self,referencia):
        self.referencia = referencia

    # Bloque de trato de titol
    def get_titol(self):
        return self.titol

    def set_titol(self,titol):
        self.titol = titol

    # Metodo para visualizar el objeto
    def visualitzar(self):
        print self.referencia
        print self.titol

    # Bloque de sobrescritura de metodos
    def __str__(self):
        return self.referencia

    def __eq__(self, other):
        return self.referencia == other
