from util import Util

util = Util()

oVar1 = {'VAR': {'NAME': 'iID', 'VALUE': '10'}}
util.setTable(oVar1)
oVar2 = {'VAR': {'NAME': 'iId', 'VALUE': '15'}}
util.setTable(oVar2)
print(util.getSimble('VAR'))
	
