# WHILE e FOR
#
class Repeticao:

    def __init__(self, bloco=None, explog=None, id1=None, expreg1=None, id2=None, expreg2=None):
        self.expreg1 = expreg1
        self.bloco = bloco
        self.id1 = id1
        self.explog = explog
        self.expreg2 = expreg2
        self.id2 = id2

    def __str__(self):
        aux = "<REPETICAO> \n"

        if self.id1:
            aux += "FOR \n"
            aux += "( \n"
            aux += "VAR \n"
            aux += self.id1.__repr__()
            aux += ":= \n"
            if self.expreg1:
                aux += self.expreg1.__repr__()
            
            aux += "; \n"
            if self.explog:
                aux += self.explog.__repr__()
                aux += "; \n"
            
            if self.id2:
                aux += self.id2.__repr__()
                aux += ":= \n"
                if self.expreg2:
                    aux += self.expreg2.__repr__()
            
            aux += ") \n"
        else:
            aux += "WHILE \n"
            aux += "( \n"
            if self.explog:
                aux += self.explog.__repr__()
            aux += ") \n"

        if self.bloco:
            aux += self.bloco.__repr__()
        
        
        aux += "</REPETICAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()