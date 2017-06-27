from util import Util
from compiler import Compiler

util = Util()

sData = util.getFileContent('runTesteLeandro.top')
compila = Compiler(sData)

#TOKENS
#print(util.getTokenFileContent())

#SINTATICO
print(util.getSintaticFileContent())