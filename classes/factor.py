from util import Util
# expression = (expression)
#
class Factor:

    def __init__(self, id=None, number=None, expression=None):
        self.id=id
        self.number=number
        self.expression=expression

    def __str__(self):
        aux = "<FACTOR> \n"

        if (self.expression):
             aux += "( \n"
             aux += self.expression.__repr__()
             aux += ") \n"
        
        elif self.id:
            aux += self.id.__repr__()
        elif self.number:
            aux += str(self.number) + "\n"
        
        aux += "</FACTOR> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def getValue(self):
        if self.expression:
            return self.expression.getValue()
        elif self.id:
            return self.id.getValue()
        else:
            return self.number

    def semantico(self):        
        util = Util()

        if self.id:
            if not util.symbolExists("VAR"+self.id.getName()):
                util.setSemanticFile('<FACTOR> Variável ' + str(self.id.getName()) + ' não foi declarada </FACTOR>')
                return False
            else:
                if self.id.getType() == str:
                    util.setSemanticFile('<FACTOR> Não é possível definir variável do tipo STRING como FACTOR </FACTOR>')
                    return False
                elif self.id.getType() == bool:
                    util.setSemanticFile('<FACTOR> Não é possível definir variável do tipo BOOLEAN como FACTOR </FACTOR>')
                    return False
                elif self.id.getType() == object:
                    util.setSemanticFile('<FACTOR> Não é possível definir variável do tipo OBJECT como FACTOR </FACTOR>')
                    return False

        if self.expression:
            if not self.expression.semantico():
                return False

        return True