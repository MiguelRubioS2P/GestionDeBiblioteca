class Publicacion():
    # Constructor
    def __init__(self,referencia,titol):
        """
        Constructor de Publicacion

        :param referencia:
        :param titol:
        """
        self.referencia = referencia
        self.titol = titol

    # Bloque de trato de referencia
    def get_referencia(self):
        """
        Getter del atributo referencia

        :return: Devuelve el valor del atributo referencia
        """
        return self.referencia

    def set_referencia(self,referencia):
        """
        Setter del atributo de referencia

        :param referencia: Nuevo valor para el atributo referencia
        :return:
        """
        self.referencia = referencia

    # Bloque de trato de titol
    def get_titol(self):
        """
        Getter del atributo de titulo

        :return: Devuelve el valor del atributo titol
        """
        return self.titol

    def set_titol(self,titol):
        """
        Setter del atributo de titulo
        :param titol: Nuevo valor para el atributo de titulo
        :return:
        """
        self.titol = titol

    # Metodo para visualizar el objeto
    def visualitzar(self):
        """
        Visualizar la informacion del objeto

        :return: String
        """
        return "{} {}".format(self.referencia,self.titol)

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
