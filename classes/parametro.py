class Parametro:

    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        aux = "<PARAMETRO> \n"

        if self.id:
            aux += self.id.__repr__()
        
        aux += "</PARAMETRO> \n"
        return aux

    def __repr__(self):
        return self.__str__()