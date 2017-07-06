from tkinter import *
from util import Util
from compiler import Compiler

sCorFundo = '#202328'
sCorTexto = '#FFFFFF'
sCorTexto2 = '#A6B2C0'
sCorFundoCaixas = '#272B33'
sCorFundoBotao = '#2882F9'

class Application:
	util = Util()
	def __init__(self, master=None):	

		

		#CONTAINERS
		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["padx"] = 50
		self.primeiroContainer["bg"] = sCorFundo
		self.primeiroContainer.pack(side=LEFT)

		self.segundoContainer = Frame(master)
		self.primeiroContainer["padx"] = 30	
		self.segundoContainer["bg"] = sCorFundo		
		self.segundoContainer.pack(side=RIGHT, expand=YES)

		self.titleCotainer = Frame(self.primeiroContainer)
		self.titleCotainer["bg"] = sCorFundo		

		self.titleCotainer.pack()

		self.codeCotainer = Frame(self.primeiroContainer)
		self.codeCotainer["bg"] = sCorFundo				
		self.codeCotainer.pack()
		

		self.newCodeCotainer = Frame(self.primeiroContainer)
		self.newCodeCotainer["bg"] = sCorFundo
		self.newCodeCotainer.pack()

		self.lexicoContainer = Frame(self.segundoContainer)
		self.lexicoContainer["width"] = 90
		self.lexicoContainer["bg"] = sCorFundo
		self.lexicoContainer.pack()

		self.sintaticoContainer = Frame(self.segundoContainer)
		self.sintaticoContainer["width"] = 90
		self.sintaticoContainer["bg"] = sCorFundo
		self.sintaticoContainer.pack()		

		self.semanticoContainer = Frame(self.segundoContainer)
		self.semanticoContainer["width"] = 90
		self.semanticoContainer["bg"] = sCorFundo
		self.semanticoContainer.pack()			

		#CAIXA DE COMANDOS DA LINGUAGEM		
		self.codeLabel = Label(self.codeCotainer,text="Código:", font=self.fontePadrao, anchor='w')
		self.codeLabel.pack(fill='both')		
		self.codeLabel["fg"] = sCorTexto
		self.codeLabel["bg"] = sCorFundo
		
		self.code = Text(self.codeCotainer, height=20, width=100)
		self.code.insert(END, self.util.getDefaultCode())
		self.code["font"] = self.fontePadrao
		self.code["fg"] = sCorTexto2
		self.code["bg"] = sCorFundoCaixas
		self.code["bd"] = 0
		self.code.pack()

		self.space = Label(self.codeCotainer,text="", font=self.fontePadrao, width=1)
		self.space["bg"] = sCorFundo		
		self.space.pack()	
			
		#BOTÕES
		self.compilar = Button(self.codeCotainer)
		self.compilar["text"] = "Compilar"
		self.compilar["font"] = ("Calibri", "12")
		self.compilar["width"] = 12
		self.compilar["pady"] = 5		
		self.compilar["command"] = self.compila		
		self.compilar["bg"] = sCorFundoBotao		
		self.compilar["fg"] = sCorTexto		
		self.compilar["bd"] = 0							
		self.compilar.pack(side=LEFT)
		
		self.space2 = Label(self.newCodeCotainer,text="", font=self.fontePadrao, width=1)
		self.space2["bg"] = sCorFundo
		self.space2.pack()

		#CODIGO GERADO
		self.newCodeLabel = Label(self.newCodeCotainer,text="Console:", font=self.fontePadrao, anchor='w')
		self.newCodeLabel["fg"] = sCorTexto
		self.newCodeLabel["bg"] = sCorFundo
		self.newCodeLabel.pack(fill='both')		
		
		self.newCode = Text(self.newCodeCotainer, height=12, width=100)
		self.newCode["font"] = self.fontePadrao
		self.newCode["fg"] = sCorTexto2
		self.newCode["bg"] = sCorFundoCaixas
		self.newCode["bd"] = 0
		self.newCode.pack()
		
		#CAIXAS ONDE SERÃO LISTADOS OS DADOS
		
		#LEXICO
		self.space5 = Label(self.lexicoContainer,text="", font=self.fontePadrao, width=1)
		self.space5["bg"] = sCorFundo
		self.space5.pack()

		self.lexLabel = Label(self.lexicoContainer,text="Lexico:", font=self.fontePadrao, anchor='w')
		self.lexLabel["fg"] = sCorTexto
		self.lexLabel["bg"] = sCorFundo
		self.lexLabel.pack(fill='both')

		self.ylexscroll = Scrollbar(self.lexicoContainer, orient=VERTICAL)						
		self.ylexscroll.pack(side=RIGHT, fill=Y, expand=False)

		self.lex = Text(self.lexicoContainer, height=13, width=70)	
		self.lex["font"] = self.fontePadrao
		self.lex["yscrollcommand"] = self.ylexscroll.set		
		self.lex["fg"] = sCorTexto2
		self.lex["bg"] = sCorFundoCaixas
		self.lex["bd"] = 0		
		self.lex.pack(side=LEFT, fill='both', expand=True)

		self.ylexscroll.config(command=self.lex.yview);
		
		#SINTATICO

		self.space3 = Label(self.sintaticoContainer,text="", font=self.fontePadrao, width=1)
		self.space3["bg"] = sCorFundo
		self.space3.pack()

		self.sinLabel = Label(self.sintaticoContainer,text="Sintático:", font=self.fontePadrao, anchor='w')
		self.sinLabel["fg"] = sCorTexto
		self.sinLabel["bg"] = sCorFundo
		self.sinLabel.pack(fill='both')
		
		self.ysinscroll = Scrollbar(self.sintaticoContainer, orient=VERTICAL)		
		self.ysinscroll["bg"] = sCorFundoCaixas
		self.ysinscroll.pack(side=RIGHT, fill=Y, expand=False)

		self.sin = Text(self.sintaticoContainer, height=13, width=70)
		self.sin["font"] = self.fontePadrao
		self.sin["yscrollcommand"] = self.ysinscroll.set
		self.sin["fg"] = sCorTexto2
		self.sin["bg"] = sCorFundoCaixas
		self.sin["bd"] = 0					
		self.sin.pack(side=LEFT, fill='both', expand=True)

		self.ysinscroll.config(command=self.lex.yview);
	
		#SEMANTICO

		self.space4 = Label(self.semanticoContainer,text="", font=self.fontePadrao, width=1)
		self.space4["bg"] = sCorFundo
		self.space4.pack()

		self.semLabel = Label(self.semanticoContainer,text="Semantico:", font=self.fontePadrao, anchor='w')
		self.semLabel["bg"] = sCorFundo		
		self.semLabel["fg"] = sCorTexto
		self.semLabel.pack(fill='both')

		self.ysemscroll = Scrollbar(self.semanticoContainer, orient=VERTICAL)		
		self.ysemscroll["bg"] = sCorFundoCaixas		
		self.ysemscroll.pack(side=RIGHT, fill=Y, expand=False)

		self.sem = Text(self.semanticoContainer, height=8, width=70)
		self.sem["font"] = self.fontePadrao
		self.sem["yscrollcommand"] = self.ysemscroll.set
		self.sem["fg"] = sCorTexto2
		self.sem["bg"] = sCorFundoCaixas
		self.sem["bd"] = 0						
		self.sem.pack(side=LEFT, fill='both', expand=True)

		self.ysemscroll.config(command=self.lex.yview);		

	def compila(self):
		sData = self.code.get('1.0', END);
		comp = Compiler(sData)
		self.lex.delete(1.0, END)
		self.lex.insert(END, self.util.getTokenFileContent())
		self.sin.delete(1.0, END)
		self.sin.insert(END, self.util.getSintaticFileContent())
		self.sem.delete(1.0, END)
		self.sem.insert(END, self.util.getSemanticFileContent())		
	   
root = Tk()
Application(root)
root.state('zoomed')
root.title('Compilador Top Linguagem')
root.configure(bg=sCorFundo)
root.resizable(width=False, height=False)
root.mainloop()