#operacao = * ou /
#
class Term():

    def __init__(self, term=None, operacao=None, factor=None):
        self.term = term
        self.operacao = operacao
        self.factor = factor
    
    def __str__(self):
        aux = "<TERM> \n"

        if self.term:
            aux += self.term.__repr__()

        if self.operacao:
            aux += "<OPERACAO>\n" + self.operacao + "\n</OPERACAO>\n"

        if self.factor:
             aux += self.factor.__repr__()
        
        
        aux += "</TERM> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    #def getFactor(self):
        #return self.factor
    def getValue(self):
        if self.operacao:
            if self.operacao == '*':
                return self.term.getValue() * self.factor.getValue()
            else:
                return self.term.getValue() / self.factor.getValue()
        else:
            return self.factor.getValue()