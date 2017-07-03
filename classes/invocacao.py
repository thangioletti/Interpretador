class Invocacao:

    def __init__(self, id=None, parametros=None):
        self.parametros = parametros
        self.id = id

    def __str__(self):
        aux = "<INVOCACAO> \n"

        if self.id:
            if (isinstance(self.id, str)):
                aux += self.id + "\n"
            else:
                aux += self.id.__repr__()

        aux += "( \n"

        if self.parametros:
            aux += self.parametros.__repr__()

        aux += ") \n"
        aux += "</INVOCACAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()