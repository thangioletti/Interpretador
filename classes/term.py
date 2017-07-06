from util import Util
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

    def semantico(self):        
        util = Util()
        
        if self.term:
            if not self.term.semantico():
                return False

        if self.factor:
            if not self.factor.semantico():
                return False 

        if self.operacao and self.operacao == '/':
            #Valida se não está tentando fazer uma divisão por zero, porém não tem como validar se for divisão por uma variável
            if self.factor.getValue() == 0:
                util.setSemanticFile('<TERM>Não é possível fazer divisão por zero</TERM>')
                return False

        return True

               