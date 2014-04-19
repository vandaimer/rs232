# -*- coding: UTF-8 -*-
import serial
class RS232Client:
    def __init__(self, port=0,timeout=1000):
        self.port = port
        self.obj = serial.Serial(port,9600,serial.EIGHTBITS)
        self.obj.timeout = timeout
    def ler(self):
        if self.obj.name:
            print("IF")
            string = self.obj.read().decode()
            while  string != "FIM":
                if not string.empty()
                    string = self.obj.read().decode()
                    print("while")
                    print(string)
            print("SAIU while")
        print("SAIU IF")
obj = RS232Client("/dev/ttyS11",1000)
obj.ler()