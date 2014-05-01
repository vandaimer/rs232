# -*- coding: UTF-8 -*-
from mySerial import *
class RS232Server:
    def __init__(self,port=0):
        self.serial = mySerial( port )
        self.obj = self.serial.getObj()
    def escrever(self,arquivo=0):
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
        self.serial.mudarConfig()