import serial
class mySerial:
	def __init__(self, port):
		//seta porta
		self.port = port
		//cria obj serial
		self.obj = serial.Serial(port,18000)
		//seta timeout
		self.obj.timeout = 10
		//seta bit paridade
		self.obj.parity=serial.PARITY_NONE
		//seta bits de stop
		self.obj.stopbits=serial.STOPBITS_ONE
		//seta tamanho de bytes lidos
		self.obj.bytesize=serial.FIVEBITS
	def getObj(self):
		return self.obj;
	def mudarConfig(self):
		self.obj.parity=serial.PARITY_EVEN
		self.obj.stopbits=serial.STOPBITS_ONE_POINT_FIVE
		self.obj.bytesize=serial.SIXBITS