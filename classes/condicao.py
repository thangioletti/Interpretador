from util import Util
class Condicao:

    def __init__(self, explog=None, bloco=None, blocoElse=None):
        self.explog = explog
        self.bloco = bloco
        self.blocoElse = blocoElse

    def __str__(self):
        aux = "<CONDICAO> \nIF \n( \n"

        if self.explog:
            aux += self.explog.__repr__()

        aux += ") \n"

        if self.bloco:
            aux += self.bloco.__repr__()

        if self.blocoElse:
            aux += "ELSE \n"
            aux += self.blocoElse.__repr__()

        aux += "END \n"
        aux += "</CONDICAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        if self.explog:
            if not self.explog.semantico():
                return False

        if self.bloco:
            if not self.bloco.semantico():
                return False
        
        if self.blocoElse:
            if not self.blocoElse.semantico():
                return False

        return True