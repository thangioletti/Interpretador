from util import Util

class Declaracao:

    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        aux = "<DECLARACAO> \n VAR \n"

        if self.id:
            aux += self.id.__repr__()

        aux += "; \n"
        aux += "</DECLARACAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        util = Util()

        if util.symbolExists(self.id.getName()):
            util.setSemanticFile('<DECLARACAO>Já existe uma variável com o nome: ' + self.id.getName() + '</DECLARACAO>')
        else:
            oJsonVar = {}
            sVarName = 'VAR'+(self.id.getName())
            util.setTableVar(sVarName, oJsonVar)
    
    def getValue(self):
        return