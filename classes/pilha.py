class Pilha(object):

    def __init__(self):
        self.dados = []

    def __name__(self):
        return "Pilha"

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def getDados(self):   
        return self.dados

    def tamanho(self):
        return len(self.dados)

    def vazia(self):
        return len(self.dados) == 0