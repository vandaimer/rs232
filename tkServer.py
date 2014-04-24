from tkinter import *
from server import *
from threading import Thread
class Server(Tk):
	def __init__(self):
		self.root = Tk()
		self.root.geometry("300x300+550+250")
		self.root.title("Servidor RS232")
		self.frame = Frame( self.root )

		self.botao = Button( self.frame,text="Enviar arquivo via RS232",command=self.escrever)
		self.label = Label( self.frame,text="Digite o caminho do arquivo" )

		self.textCaixa = StringVar(self.frame)
		self.textCaixa.set("linux.pdf")
		self.caixa = Entry( self.frame,textvar=self.textCaixa )
		self.label.pack()
		self.caixa.pack()
		self.botao.pack()

		self.frame.pack( expand=True )
	def escrever(self):
		self.botao['state'] = DISABLED
		t = Thread( target=self.internal )
		t.start()
	def internal(self):
		x = RS232Server( "/dev/ttyS10" )
		x.mudarConfig()
		x.escrever( self.textCaixa.get() );
app = Server()
mainloop()