class Function:

    def __init__(self, parametros=None, comando=None):
        self.parametros = parametros
        self.comando = comando

    def __str__(self):
        aux = "<FUNCTION> \n"

        if self.parametros:
            aux += self.parametros.__repr__()
        
        if self.comando:
            aux += self.comando.__repr__()

        aux += "</FUNCTION> \n"
        return aux

    def __repr__(self):
        return self.__str__()