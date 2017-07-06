from util import Util

class Atribuicao:

    def __init__(self, id=None, expreg=None, string=None, explog=None):    
        self.expreg = expreg
        self.id = id
        self.string = string
        self.explog = explog

    def __str__(self):
        aux = "<ATRIBUICAO> \n"

        if self.id:
            aux += self.id.__repr__()

        aux += ":= \n"

        if self.expreg:
            aux += self.expreg.__repr__()
        elif self.string:
            aux += self.string + "\n"
        else:
            aux += self.explog.__repr__()


        aux += "; \n"
        aux += "</ATRIBUICAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):        
        util = Util()

        if not util.symbolExists('VAR'+str(self.id.getName())):
            util.setSemanticFile('<ATRIBUICAO>A variavel ' + str(self.id.getName()) + ' não foi previamente declarada </ATRIBUICAO>')
        else:
            if self.expreg: 
                if self.expreg.semantico():
                    if (not isinstance(self.expreg.getValue() , self.id.getType())):
                        util.setSemanticFile('<ATRIBUICAO>A variavel ' + str(self.id.getName()) + ' espera um valor '+util.getLabelTypes(str(self.id.getType()))+' mas o recebido foi '+util.getLabelTypes(str(type(self.expreg.getValue())))+' </ATRIBUICAO>')
            elif self.explog: 
                if self.explog.semantico():
                    if (not type(self.explog.getValue()) == self.id.getType()):
                        util.setSemanticFile('<ATRIBUICAO>A variavel ' + str(self.id.getName()) + ' espera um valor '+util.getLabelTypes(str(self.id.getType()))+' mas o recebido foi '+util.getLabelTypes(str(type(self.expreg.getValue())))+' </ATRIBUICAO>')
            else:
                if (not isinstance(self.string, self.id.getType())):                                
                    util.setSemanticFile('<ATRIBUICAO>A variavel '+ str(self.id.getName()) + ' espera um valor '+ util.getLabelTypes(str(self.id.getType()))+' mas o recebido foi ' +util.getLabelTypes(str(type(self.string)))+' </ATRIBUICAO>')

        #AQUI LEANDRO
        sValor = '0' #aqui vai o valor da variavel
        #MONTA UM JSON CASO PASSOU NAS VERIFICAÇÕES DO SEMANTICO
        oJson = {'VALOR': sValor}
        #GRAVA NA TABELA
        util.setTableVar('VAR'+str(self.id.getName()), oJson)

        #PRA PEGAR O VALOR 
        oJson = util.getSymbol('VAR'+str(self.id.getName()))
        sValor = oJson['VALOR']
        #print(sValor)