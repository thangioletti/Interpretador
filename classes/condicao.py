class Condicao:

    def __init__(self, explog=None, bloco=None):
        self.explog = explog
        self.bloco = bloco

    def __str__(self):
        aux = "<CONDICAO> \n IF \n ( \n"

        if self.explog:
            aux += self.explog.__repr__()

        aux += ") \n"

        if self.bloco:
            aux += self.bloco.__repr__()

        aux += "</CONDICAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()