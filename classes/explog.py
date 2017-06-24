# comparacao -> > < >= <= == !=
#
class Explog:

    def __init__(self, expreg1=None, comparacao=None, expreg2=None, explog=None):
        self.expreg1 = expreg1
        self.comparacao = comparacao
        self.expreg2 = expreg2
        self.explog = explog

    def __str__(self):
        aux = "<EXPLOG> \n"

        if self.expreg1:
            aux += self.expreg1.__repr__()
        elif self.explog:
            aux += self.explog + "\n"
        if self.comparacao:
            aux += self.comparacao + "\n"

        if self.expreg2:
             aux += self.expreg2.__repr__()
        
        
        aux += "</EXPLOG> \n"
        return aux

    def __repr__(self):
        return self.__str__()