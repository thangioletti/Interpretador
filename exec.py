from tkinter import *
from util import Util
from ex import Compiler

class Application:
	util = Util()
	def __init__(self, master=None):	

		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["height"] = 200
		self.primeiroContainer["padx"] = 50
		self.primeiroContainer.pack(side=LEFT)

		self.segundoContainer = Frame(master)
		self.segundoContainer["height"] = 250
		self.segundoContainer["padx"] = 50
		self.segundoContainer.pack(side=RIGHT)
		
		#TITULO
		self.titulo = Label(self.primeiroContainer, text="Compilador", anchor='w')
		self.titulo["font"] = ('Arial', '16', 'bold')	
		self.titulo.pack(fill='both')

		#CAIXA DE COMANDOS DA LINGUAGEM		
		self.codeLabel = Label(self.primeiroContainer,text="Código:", font=self.fontePadrao, anchor='w')
		self.codeLabel.pack(fill='both')		
		
		self.code = Text(self.primeiroContainer, height=33, width=70)
		self.code.insert(END, self.util.getDefaultCode())
		self.code["font"] = self.fontePadrao
		self.code.pack()

		self.codeLabel = Label(self.primeiroContainer,text="")
		self.codeLabel.pack()		

		#BOTÕES
		self.compilar = Button(self.primeiroContainer)
		self.compilar["text"] = "Compilar"
		self.compilar["font"] = ("Calibri", "12")
		self.compilar["width"] = 12
		self.compilar["pady"] = 5		
		self.compilar["command"] = self.compila
		self.compilar.pack(side=LEFT)

		self.space = Label(self.primeiroContainer,text="", font=self.fontePadrao, width=1)
		self.space.pack(side=LEFT)

		self.limpar = Button(self.primeiroContainer)
		self.limpar["text"] = "Limpar"
		self.limpar["font"] = ("Calibri", "12")
		self.limpar["width"] = 12
		self.limpar["pady"] = 5				
		self.limpar["command"] = self.limpar
		self.limpar.pack(side=LEFT)

		#CAIXAS ONDE SERÃO LISTADOS OS DADOS
		self.lexLabel = Label(self.segundoContainer,text="Lexico:", font=self.fontePadrao, anchor='w')
		self.lexLabel.pack(fill='both')
		
		self.lex = Text(self.segundoContainer, height=10, width=50)
		self.lex["font"] = self.fontePadrao
		self.lex.pack()

		self.sinLabel = Label(self.segundoContainer,text="Sintático:", font=self.fontePadrao, anchor='w')
		self.sinLabel.pack(fill='both')
		
		self.sin = Text(self.segundoContainer, height=10, width=50)
		self.sin["font"] = self.fontePadrao
		self.sin.pack()

		self.semLabel = Label(self.segundoContainer,text="Semantico:", font=self.fontePadrao, anchor='w')
		self.semLabel.pack(fill='both')
		
		self.sem = Text(self.segundoContainer, height=10, width=50)
		self.sem["font"] = self.fontePadrao
		self.sem.pack()	

		self.mensagem = Label(self.segundoContainer, text="", font=self.fontePadrao)
		self.mensagem.pack()

	def limpar(self):
		self.code.delete(1.0, END)		    
		self.lex.delete(1.0, END)
		self.sin.delete(1.0, END)		    
		self.sem.delete(1.0, END)

	def compila(self):
		sData = self.code.get('1.0', END);
		comp = Compiler(sData)
		self.lex.delete(1.0, END)
		self.lex.insert(END, self.util.getTokenFileContent())
		
	   
root = Tk()
Application(root)
root.mainloop()