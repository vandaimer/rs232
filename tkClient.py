from tkinter import *
from cliente import *
import tkinter.messagebox as box
from threading import Thread
import sys
class Client(Tk):
	def __init__(self):
		self.root = Tk()
		self.root.geometry("300x300+550+250")
		self.root.title("Client RS232")

		self.frame = Frame( self.root )

		self.text = Text( self.frame )

		self.botao = Button( self.frame,text="Escutar portas RS232",command=self.ler)

		scrollbar = Scrollbar(self.frame)
		scrollbar.pack(side=RIGHT, fill=Y)
		
		self.text.config(yscrollcommand=scrollbar.set)

		self.botao.pack()
		self.text.pack(side="bottom")

		self.frame.pack( expand=True )
		//cria instancia de RS232Client
		self.x = RS232Client("/dev/ttyS11")
		//muda config como pedia enunciado
		self.x.mudarConfig()
	def ler(self):
		self.botao['state'] = DISABLED
		t = Thread( target=self.internal )
		t.start()
	def internal(self):
		//lê bits da porta RS232
		string = self.x.ler()
		tmp	   = ""
		while len(string) > 0:
			tmp = string
			//insere no componente gráfico
			self.text.insert(END,string)
			//lê dados da porta RS232
			string = self.x.ler()
		if len(string) > 0:
			box.showinfo("Client RS232", "Acabou transferencia do arquivo")
		else:
			box.showinfo("Client RS232", "Timeout")
		self.root.destroy();
app = Client()
mainloop()