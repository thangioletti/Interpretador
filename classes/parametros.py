from util import Util
class Parametros:

    def __init__(self, parametro=None, parametros=None):
        self.parametro = parametro
        self.parametros = parametros

    def __str__(self):
        aux = "<PARAMETROS> \n"

        if self.parametros:
            aux += self.parametros.__repr__()
            aux += ", \n"

        if self.parametro:
            aux += self.parametro.__repr__()
        
        aux += "</PARAMETROS> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):
        util = Util()

        #if self.parametros:
            

        return True