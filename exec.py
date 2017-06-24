from tkinter import *
from util import Util
from ex import Compiler

class Application:
	util = Util()
	def __init__(self, master=None):	

		#CONTAINERS
		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		#self.primeiroContainer["height"] = 200
		#self.primeiroContainer["width"] = 30
		self.primeiroContainer["padx"] = 50
		self.primeiroContainer.pack(side=LEFT)

		self.segundoContainer = Frame(master)
		#self.segundoContainer["height"] = 250
		#self.segundoContainer["width"] = 50
		self.primeiroContainer["padx"] = 50	
		self.segundoContainer.pack(side=RIGHT)

		self.titleCotainer = Frame(self.primeiroContainer)
		self.titleCotainer.pack()

		self.codeCotainer = Frame(self.primeiroContainer)
		self.codeCotainer.pack()
		

		self.newCodeCotainer = Frame(self.primeiroContainer)
		self.newCodeCotainer.pack()

		self.lexicoContainer = Frame(self.segundoContainer)
		#self.lexicoContainer["height"] = 250
		self.lexicoContainer["width"] = 100
		self.lexicoContainer.pack()

		self.sintaticoContainer = Frame(self.segundoContainer)
		#self.sintaticoContainer["height"] = 250
		self.sintaticoContainer["width"] = 100		
		self.sintaticoContainer.pack()		

		self.semanticoContainer = Frame(self.segundoContainer)
		#self.semanticoContainer["height"] = 250
		self.semanticoContainer["width"] = 100		
		self.semanticoContainer.pack()		

		#TITULO
		self.titulo = Label(self.titleCotainer, text="Compilador", anchor='w')
		self.titulo["font"] = ('Arial', '16', 'bold')	
		self.titulo.pack(fill='both')

		#CAIXA DE COMANDOS DA LINGUAGEM		
		self.codeLabel = Label(self.codeCotainer,text="Código:", font=self.fontePadrao, anchor='w')
		self.codeLabel.pack(fill='both')		
		
		self.code = Text(self.codeCotainer, height=20, width=100)
		self.code.insert(END, self.util.getDefaultCode())
		self.code["font"] = self.fontePadrao
		self.code.pack()

		#BOTÕES
		self.compilar = Button(self.codeCotainer)
		self.compilar["text"] = "Compilar"
		self.compilar["font"] = ("Calibri", "12")
		self.compilar["width"] = 12
		self.compilar["pady"] = 5		
		self.compilar["command"] = self.compila
		self.compilar.pack(side=LEFT)

		self.space = Label(self.codeCotainer,text="", font=self.fontePadrao, width=1)
		self.space.pack(side=LEFT)

		self.limpar = Button(self.codeCotainer)
		self.limpar["text"] = "Limpar"
		self.limpar["font"] = ("Calibri", "12")
		self.limpar["width"] = 12
		self.limpar["pady"] = 5				
		self.limpar["command"] = self.limpar
		self.limpar.pack(side=LEFT)

		#CODIGO GERADO
		self.newCodeLabel = Label(self.newCodeCotainer,text="Código gerado:", font=self.fontePadrao, anchor='w')
		self.newCodeLabel.pack(fill='both')		
		
		self.newCode = Text(self.newCodeCotainer, height=20, width=100)
		self.newCode["font"] = self.fontePadrao
		self.newCode.pack()
		#CAIXAS ONDE SERÃO LISTADOS OS DADOS
		
		#LEXICO
		self.lexLabel = Label(self.lexicoContainer,text="Lexico:", font=self.fontePadrao, anchor='w')
		self.lexLabel.pack(fill='both')

		self.ylexscroll = Scrollbar(self.lexicoContainer, orient=VERTICAL)		
		self.ylexscroll.pack(side=RIGHT, fill=Y, expand=False)

		self.lex = Text(self.lexicoContainer, height=10, width=70)
		self.lex["font"] = self.fontePadrao
		self.lex["yscrollcommand"] = self.ylexscroll.set				
		self.lex.pack(side=LEFT, fill='both', expand=True)

		self.ylexscroll.config(command=self.lex.yview);

		#SINTATICO
		self.sinLabel = Label(self.sintaticoContainer,text="Sintático:", font=self.fontePadrao, anchor='w')
		self.sinLabel.pack(fill='both')
		
		self.ysinscroll = Scrollbar(self.sintaticoContainer, orient=VERTICAL)		
		self.ysinscroll.pack(side=RIGHT, fill=Y, expand=False)

		self.sin = Text(self.sintaticoContainer, height=10, width=70)
		self.sin["font"] = self.fontePadrao
		self.sin["yscrollcommand"] = self.ysinscroll.set				
		self.sin.pack(side=LEFT, fill='both', expand=True)

		self.ysinscroll.config(command=self.lex.yview);
	
		#SEMANTICO

		self.semLabel = Label(self.semanticoContainer,text="Semantico:", font=self.fontePadrao, anchor='w')
		self.semLabel.pack(fill='both')

		self.ysemscroll = Scrollbar(self.semanticoContainer, orient=VERTICAL)		
		self.ysemscroll.pack(side=RIGHT, fill=Y, expand=False)

		self.sem = Text(self.semanticoContainer, height=10, width=70)
		self.sem["font"] = self.fontePadrao
		self.sem["yscrollcommand"] = self.ysemscroll.set				
		self.sem.pack(side=LEFT, fill='both', expand=True)

		self.ysemscroll.config(command=self.lex.yview);
		

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
		self.sin.delete(1.0, END)
		self.sin.insert(END, self.util.getSintaticFileContent())
		
	   
root = Tk()
Application(root)
root.state('zoomed')
root.resizable(width=False, height=False)
root.mainloop()