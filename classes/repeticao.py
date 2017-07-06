from util import Util
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

    def semantico(self):
        util = Util()

        if self.id1:
            if util.symbolExists(self.id1.getName()):
                util.setSemanticFile('<REPETICAO>Já existe uma variável com o nome: ' + self.id1.getName() + '</REPETICAO>')
                return False
            else:
                if self.id2:
                    if self.id2.getName() != self.id1.getName():
                        util.setSemanticFile('<REPETICAO>Variável que recece atribuição(' + self.id2.getName() + ' é diferente de variável declarada inicialmente (' + self.id1.getName() + ')</REPETICAO>')
                        return False
                    else:
                        oJsonVar = {}
                        sVarName = 'VAR'+(self.id1.getName())
                        util.setTableVar(sVarName, oJsonVar)     
                
        if self.explog:
            if not self.explog.semantico():
                return False

        if self.expreg1:
            if not self.expreg1.semantico():
                return False

        if self.expreg2:
            if not self.expreg2.semantico():
                return False
        
        if self.bloco:
            if not self.bloco.semantico():
                return False
        
        return True

    def getValue(self):
        #Enquanto a explog for Verdadeira, executa o bloco de comandos
        while (self.explog.getValue()):
            self.bloco.getValue()
            if self.id1:
                oJson = {'VALOR': self.expreg2)}
                util.setTableVar('VAR'+str(self.id1.getName()), oJson)#GRAVA NA TABELA
