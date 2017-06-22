# operacao = + ou -
#
class Expression:

    def __init__(self, expression=None, operacao=None, term=None):
        self.expression = expression
        self.operacao = operacao
        self.term = term

    def __str__(self):
        aux = "<EXPRESSION> \n"

        if self.expression:
            aux += self.expression.__repr__()

        if self.operacao:
            aux += "<OPERACAO>\n" + self.operacao + "\n</OPERACAO>\n"

        if self.term:
             aux += self.term.__repr__()
        
        
        aux += "</EXPRESSION> \n"
        return aux

    def __repr__(self):
        return self.__str__()