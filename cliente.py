# -*- coding: UTF-8 -*-
import os
from mySerial import *
class RS232Client():
    def __init__(self, port):
        self.serial = mySerial( port )
        self.obj = self.serial.getObj()
        if os.path.isfile("copia"):
            os.remove("copia")
        self.destino = open("copia","wb")
    def ler(self):
        if  self.obj.name:
            string  = self.obj.read()
            self.destino.write(string)
            return string
        if self.x.inWaiting():
            box.showinfo("Client RS232", "Timeout")
            sys.exit(0)
    def mudarConfig(self):
        self.serial.mudarConfig()