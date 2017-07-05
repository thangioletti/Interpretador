import os
import json

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

	def getTable(self):
		if (os.path.isfile('table.ttop')):
			sJson = self.getFileContent('table.ttop')
		else:
			sJson = '{}'

		return json.loads(sJson)			

	def getSymbol(self, sKey):
		try:
			return self.getTable()[sKey]
		except Exception as e:
			return False

	def symbolExists(self, sKey):
		try:
			self.getTable()[sKey]
			return True
		except Exception as e:
			return False

	def setTable(self, oObj):
		oJson = self.getTable()	
		oJson = self.objMerge(oJson, oObj)
		sJsonSave = json.dumps(oJson)		
		oArquivo = open('table.ttop', 'w')
		oArquivo.write(sJsonSave)
		oArquivo.close()

	def objMerge(self, obj, add_obj):		
		for property in add_obj:
			obj[property] = add_obj[property]
		return obj

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