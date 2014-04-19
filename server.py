# -*- coding: UTF-8 -*-
import serial
class RS232Client:
    def __init__(self,port=0,timeout=1000):
        self.port = port
        self.obj = serial.Serial(port,9600,serial.EIGHTBITS)
        self.obj.timeout = timeout
    def escrever(self):
        if self.obj.name:
            string = ""
            while string != "FIM":
                string = input("ESCREVA\n")
                self.obj.write(string.encode())
                print(string)
            print("SAIU while")
obj = RS232Client("/dev/ttyS10")
obj.escrever()