# -*- coding: UTF-8 -*-
import serial
import os
class RS232Client():
    def __init__(self, port):
        self.port = port
        self.obj = serial.Serial(port,18000)
        self.obj.timeout = 30
        self.obj.parity=serial.PARITY_NONE
        self.obj.stopbits=serial.STOPBITS_ONE
        self.obj.bytesize=serial.FIVEBITS
        if os.path.isfile("copia"):
            os.remove("copia")
        self.destino = open("copia","wb")
    def ler(self):
        if  self.obj.name:
        #     string = self.obj.read()
        #     if string:
        #         destino.write(string)
        #         print(string)
            string  = self.obj.read()
            self.destino.write(string)
            return string
    def mudarConfig(self):
            self.obj.parity=serial.PARITY_EVEN
            self.obj.stopbits=serial.STOPBITS_ONE_POINT_FIVE
            self.obj.bytesize=serial.SIXBITS