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
        """
        Visualizar la informacion del objeto

        :return: String con la informacion del objeto
        """
        print "{} {}".format(self.referencia,self.titol)

    # Bloque de sobrescritura de metodos
    def __str__(self):
        """
        Para hacer un print controlado de nuestro objeto

        :return: Un string con solo la referencia del objeto
        """
        return "{}".format(self.referencia)

    def __eq__(self, other):
        """
        Comparamos la referencia del objeto directamente con una referencia

        :param other: una referencia
        :return: True o False
        """
        return self.referencia == other
