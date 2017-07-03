class ParametrosInvocacao:

    def __init__(self, id1=None, id2=None):
        self.id1 = id1
        self.id2 = id2

    def __str__(self):
        aux = "<PARAMETROS_INVOCACAO> \n"

        if self.id1:
            aux += self.id1.__repr__()
        
        aux += ", \n"

        if self.id2:
            aux += self.id2.__repr__()
        
        aux += "</PARAMETROS_INVOCACAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()