 
class Atribuicao:

    def __init__(self, id=None, expreg=None):
        self.expreg = expreg
        self.id = id        

    def __str__(self):
        aux = "<ATRIBUICAO> \n"

        if self.id:
            aux += self.id.__repr__()

        aux += ":= \n"

        if self.expreg:
            aux += self.expreg.__repr__()
        
        aux += "; \n"
        aux += "</ATRIBUICAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):          
        if (not isinstance(self.expreg.getValue() , self.id.getType())):
            print('a variavel espera um valor %s mas o recebido foi %s' % (str(self.id.getType()), str(type(self.expreg.getValue()))));