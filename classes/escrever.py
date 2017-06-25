class Escrever:

    def __init__(self, texto=None, id=None):
        self.texto = texto

    def __str__(self):
        aux = "<ESCREVER> \n PRINT \n ( \n"
        
        if self.texto:
            aux += self.texto + "\n"
        elif self.id:
            aux += self.id.__repr__()
            
        aux += ")\n ; \n </ESCREVER> \n"
        return aux

    def __repr__(self):
        return self.__str__()