from tkinter import *

class Application:
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
		self.titulo = Label(self.primeiroContainer, text="Compilador", justify=LEFT)
		self.titulo["font"] = ("Arial", "16", "bold")	
		self.titulo.pack()

		#CAIXA DE COMANDOS DA LINGUAGEM		
		self.codeLabel = Label(self.primeiroContainer,text="Código", font=self.fontePadrao)
		self.codeLabel.pack()		
		
		self.code = Text(self.primeiroContainer, height=33, width=50)
		self.code["font"] = self.fontePadrao
		self.code.pack()

		self.codeLabel = Label(self.primeiroContainer,text="")
		self.codeLabel.pack()		

		#BOTÕES
		self.autenticar = Button(self.primeiroContainer)
		self.autenticar["text"] = "Compilar"
		self.autenticar["font"] = ("Calibri", "12")
		self.autenticar["width"] = 12
		self.autenticar["pady"] = 5				
		self.autenticar["command"] = self.verificaSenha
		self.autenticar.pack(side=LEFT)

		self.space = Label(self.primeiroContainer,text="", font=self.fontePadrao, width=1)
		self.space.pack(side=LEFT)

		self.limpar = Button(self.primeiroContainer)
		self.limpar["text"] = "Limpar"
		self.limpar["font"] = ("Calibri", "12")
		self.limpar["width"] = 12
		self.limpar["pady"] = 5				
		self.limpar["command"] = self.verificaSenha
		self.limpar.pack(side=LEFT)

		#CAIXAS ONDE SERÃO LISTADOS OS DADOS
		self.lexLabel = Label(self.segundoContainer,text="Lexico", font=self.fontePadrao)
		self.lexLabel.pack()
		
		self.lex = Text(self.segundoContainer, height=10, width=50)
		self.lex["font"] = self.fontePadrao
		self.lex.pack()

		self.sinLabel = Label(self.segundoContainer,text="Sintático", font=self.fontePadrao)
		self.sinLabel.pack()
		
		self.sin = Text(self.segundoContainer, height=10, width=50)
		self.sin["font"] = self.fontePadrao
		self.sin.pack()

		self.semLabel = Label(self.segundoContainer,text="Semantico", font=self.fontePadrao)
		self.semLabel.pack()
		
		self.sem = Text(self.segundoContainer, height=10, width=50)
		self.sem["font"] = self.fontePadrao
		self.sem.pack()	

		self.mensagem = Label(self.segundoContainer, text="", font=self.fontePadrao)
		self.mensagem.pack()

		#Método verificar senha
	def verificaSenha(self):
		usuario = self.nome.get()
		senha = self.senha.get()
		if usuario == "usuariodevmedia" and senha == "dev":
			self.mensagem["text"] = "Autenticado"
		else:
			self.mensagem["text"] = "Erro na autenticação"
	   
root = Tk()
Application(root)
root.mainloop()