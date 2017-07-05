from util import Util

class Escrever:

    def __init__(self, texto=None, id=None):
        self.texto = texto
        self.id = id
        self.semantico()

    def __str__(self):
        aux = "<ESCREVER> \nPRINT \n( \n"
        
        if self.texto:
            aux += self.texto + "\n"
        elif self.id:
            aux += self.id.__repr__()
            
        aux += ")\n; \n</ESCREVER> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        util = Util()

        if self.id:
            if not util.symbolExists('VAR'+self.id.getName()):
                util.setSemanticFile('<ESCREVER>Variável ' + str(self.id.getName()) + ' não foi declarada</ESCREVER>')
            elif self.id.getType() == object:
                    util.setSemanticFile('<ESCREVER>Não é possível escrever o valor de um objeto</ESCREVER>')
                    