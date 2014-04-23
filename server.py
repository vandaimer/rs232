# -*- coding: UTF-8 -*-
import serial
class RS232Server:
    def __init__(self,port=0):
        self.port = port
        self.obj = serial.Serial(port,9600)
        self.obj.parity=serial.PARITY_NONE
        self.obj.stopbits=serial.STOPBITS_ONE
        self.obj.bytesize=serial.FIVEBITS
    def escrever(self,arquivo=0):
        self.botao['state'] = DISABLED
        if arquivo == 0:
            if self.obj.name:
                string = input("ESCREVA\n")
                while string != "FIM":
                    self.obj.write(string)
                    string = input("")
        else:
            arquivo = open(arquivo,"rb")
            string = arquivo.read()
            self.obj.write(string)
    def mudarConfig(self):
        self.obj.parity=serial.PARITY_EVEN
        self.obj.stopbits=serial.STOPBITS_ONE_POINT_FIVE
        self.obj.bytesize=serial.SIXBITS