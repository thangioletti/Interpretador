class Declaracao:

    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        aux = "<DECLARACAO> \n VAR \n"

        if self.id:
            aux += self.id.__repr__()

        aux += "; \n"
        aux += "</DECLARACAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()