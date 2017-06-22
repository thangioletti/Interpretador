class Util:
	
	def getDefaultCode(self):		
		return self.getFileContent('run.top')

	def getTokenFileContent(self):		
		return self.getFileContent('tokens.ttop')

	def getFileContent(self, sFileDir):

		oArquivo = open(sFileDir)
		sData = ''
		with oArquivo as oInfo:
			for sLine in oInfo.readlines():
				sData = sData+sLine

		oArquivo.close()

		return sData