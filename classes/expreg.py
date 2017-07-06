from util import Util
# operacao = + ou -
#
class Expreg:

    def __init__(self, expreg=None, operacao=None, term=None):
        self.expreg = expreg
        self.operacao = operacao
        self.term = term

    def __str__(self):
        aux = "<EXPREG> \n"

        if self.expreg:
            aux += self.expreg.__repr__()

        if self.operacao:
            aux += self.operacao + "\n"

        if self.term:
             aux += self.term.__repr__()
        
        
        aux += "</EXPREG> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def getValue(self):
        if self.operacao:
            if self.operacao == '+':
                return self.expreg.getValue() + self.term.getValue()
            else:
                return self.expreg.getValue() - self.term.getValue()
        elif self.term:
            return self.term.getValue()

    def semantico(self):
        if self.expreg:
            if not self.expreg.semantico():
                return False

        if self.term:
            if not self.term.semantico():
                return False

        return True