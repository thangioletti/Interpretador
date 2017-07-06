from util import Util
class Function:

    def __init__(self, parametros=None, bloco=None):
        self.parametros = parametros
        self.bloco = bloco

    def __str__(self):
        aux = "<FUNCTION> \n"

        if self.parametros:
            aux += self.parametros.__repr__()
        
        if self.bloco:
            aux += self.bloco.__repr__()

        aux += "</FUNCTION> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        util = Util()

        if self.bloco:
            if not self.bloco.semantico:
                return False

        return True