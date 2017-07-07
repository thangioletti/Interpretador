import os
import json

class Util:
	
	def unlinkSemantic(self):		
		if (os.path.isfile('semantico.stop')):
			os.remove('semantico.stop')

	def unlinkConsole(self):		
		if (os.path.isfile('console.stop')):
			os.remove('console.stop')

	def getDefaultCode(self):		
		return self.getFileContent('run.top')

	def getTokenFileContent(self):		
		return self.getFileContent('tokens.ttop')

	def getSintaticFileContent(self):		
		return self.getFileContent('sintatico.stop')		

	def getConsoleFileContent(self):		
		return self.getFileContent('console.stop')		

	def getSemanticFileContent(self):
		if (os.path.isfile('semantico.stop')):
			return self.getFileContent('semantico.stop')
		else:
			return 'Ok'			

	def unlinkTable(self):	
		oJson = {}
		sJsonSave = json.dumps(oJson)		
		self.saveTableFile(sJsonSave)

	def getTable(self):
		if (os.path.isfile('table.ttop')):
			sJson = self.getFileContent('table.ttop')
		else:
			sJson = '{}'

		return json.loads(sJson)			

	def getSymbol(self, sKey):
		i = int(self.getCommand())
		oTable = self.getTable()		
		while (i >= 1):						
			try:								
				return oTable[str(i)][sKey]					
			except Exception as e:
				i = i-1
				continue						
			i = i-1
		return {}

	def symbolExists(self, sKey):		
		i = int(self.getCommand())
		oTable = self.getTable()		
		while (i >= 1):						
			try:								
				if (oTable[str(i)][sKey]):										
		
					return True
			except Exception as e:
				i = i-1
				continue						
			i = i-1
		return False

	def getCurrentBlock(self):
		i = int(self.getCommand())
		oTable = self.getTable()		
		while (i >= 1):						
			try:												
				if (not oTable[str(i)]['FOR']):										
					return 'FOR'+str(i)
			except Exception as e:
				i = i-1
				continue						
			i = i-1			
		return 'main'

	def setTableBlock(self, sType):
		oObj = {sType: {}}
		#print(oObj)
		self.setTable(oObj)

	def setTableVar(self, sVarName, oObjVar):
		oBlock = {'BLOCK': self.getCurrentBlock()}
		oJson = self.objMerge(oObjVar, oBlock)		
		oJsonVar = {sVarName: oJson}		
		self.setTable(oJsonVar)
		return True

	def getCommand(self):
		try:
			return self.getTable()['COMMAND']
		except Exception as e:
			self.incrementCommand(1)
			return self.getCommand()

	def incrementCommand(self, iCommand = None):		
		
		if (not iCommand):
			iCommand = int(self.getCommand()) + 1

		oJsonAllTable = self.getTable()
		oJsonSave = self.objMerge(oJsonAllTable, {'COMMAND': iCommand})
		sJsonSave = json.dumps(oJsonSave)		
		self.saveTableFile(sJsonSave)

	def setTable(self, oObj):
		self.incrementCommand()			
		oJson = self.getSymbol(self.getCommand())
		oJson = self.objMerge(oJson, oObj)
		oJsonLine = {str(self.getCommand()): oJson}
		oJsonAllTable = self.getTable()
		oJsonSave = self.objMerge(oJsonAllTable, oJsonLine)
		sJsonSave = json.dumps(oJsonSave)
		self.saveTableFile(sJsonSave)

	def saveTableFile(self, sJson):
		oArquivo = open('table.ttop', 'w')
		oArquivo.write(sJson)
		oArquivo.close()

	def objMerge(self, obj, add_obj):		
		for property in add_obj:
			obj[property] = add_obj[property]
		return obj

	def setSemanticFile(self, sText):
		if (not os.path.isfile('semantico.stop')):
			oArquivoSemantico = open('semantico.stop', 'w')		
			oArquivoSemantico.write(str(sText))
			oArquivoSemantico.close()

	def setConsoleFile(self, sText):		
		if (os.path.isfile('semantico.stop')):
			sData = self.getFileContent('console.stop')
		else:
			sData = ''

		sText = sData+'\n'+sText		
		oArquivo = open('console.stop', 'w')		
		oArquivo.write(str(sText))
		oArquivo.close()

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