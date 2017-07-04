import os

class Util:
	
	def unlinkSemantic(self):		
		if (os.path.isfile('semantico.stop')):
			os.remove('semantico.stop')

	def getDefaultCode(self):		
		return self.getFileContent('run.top')

	def getTokenFileContent(self):		
		return self.getFileContent('tokens.ttop')

	def getSintaticFileContent(self):		
		return self.getFileContent('sintatico.stop')		

	def getSemanticFileContent(self):

		if (os.path.isfile('semantico.stop')):
			return self.getFileContent('semantico.stop')
		else:
			return 'Ok'			

	def setSemanticFile(self, sText):
		oArquivoSemantico = open('semantico.stop', 'w')		
		oArquivoSemantico.write(str(sText))
		oArquivoSemantico.close()

	def getFileContent(self, sFileDir):

		oArquivo = open(sFileDir)
		sData = ''
		with oArquivo as oInfo:
			for sLine in oInfo.readlines():
				sData = sData+sLine

		oArquivo.close()

		return sData

	def getLabelTypes(self, sType):		
		 return {
            "<class 'bool'>"   : 'Boolean',
            "<class 'str'>"    : 'String',
            "<class 'int'>"    : 'Integer',
            "<class 'float'>"  : 'Float',
            "<class 'object'>" : 'Object',
        }[sType]