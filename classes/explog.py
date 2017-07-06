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

    def getValue(self):
        if str(self.comparacao) == ">":
            return self.expreg1.getValue() > self.expreg2.getValue()
        elif str(self.comparacao) == "<":
            return self.expreg1.getValue() < self.expreg2.getValue()
        elif str(self.comparacao) == "==":
            return self.expreg1.getValue() == self.expreg2.getValue()
        elif str(self.comparacao) == "!=":
            return self.expreg1.getValue() != self.expreg2.getValue() 
        elif str(self.comparacao) == "AND":
            return self.expreg1.getValue() and self.expreg2.getValue()    
        elif str(self.comparacao) == "OR":
            return self.expreg1.getValue() or self.expreg2.getValue()
        else:
            if self.explog == "TRUE":
                return True
            else:
                return False
              
    def semantico(self):
        if self.expreg1:
            if not self.expreg1.semantico():
                return False
        
        if self.expreg2:
            if not self.expreg2.semantico():
                return False

        return True