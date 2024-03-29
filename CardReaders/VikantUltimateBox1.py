import CardReaders.CardReader
from Cards.VikantUltimateCard1 import *
from Cards.BrotherCard51 import *
import Cards
import serial, time
import os

class VikantUltimateBox1(CardReaders.CardReader.CardReader):

    def __init__(self):
        self.__sepperator = chr(13)+chr(10)
        self.__terminator = chr(62)
        self.__card = None
        
    def disconnect(self):
        self.__con.close()
        
    def connect(self, port):
        self.__con = serial.Serial(
            port,
            baudrate  = 57600,
            bytesize = serial.EIGHTBITS,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            timeout=0,
            xonxoff = False,
            rtscts = True,
            dsrdtr = True,
            write_timeout = 0,
            inter_byte_timeout = None
        )
        
    def identify(self):
        self.writeString("\r")
        
        self.writeString("version")
        answer0 = self.readString()
        
        self.writeString("model")
        answer1 = self.readString()
        
        print "answer0: "+ answer0
        if "UltimateBox" not in answer0:
            raise Exception("Card reader not recognized.("+answer0+")")
            
        print "answer1: "+ answer1
        if "UltimateBox" not in answer1:
            raise Exception("Card reader not recognized.("+answer1+")")
    
    def hasCard(self):
        self.writeString("cd")
        time.sleep(1)
        answer = self.readString()
        
        if "Not Found" in answer:
            return False
            
        return True
    
    def identifyCard(self):
        id = 6
        
        data = []
        while id >= 0:
        
            self.writeString("id"+str(id))
            #time.sleep(1)
            answer = self.readString()
            
            data.append(answer[3:-2])
            
            id = id -1

        print(data)
        return data
        
    def getCard(self):
        if not self.hasCard():
            return None
            
        if self.__card != None:
            return self.__card
        
        id = 6
        
        data = self.identifyCard()
        
        if VikantUltimateCard1.isId(data):
            self.__card = VikantUltimateCard1()
        elif BrotherCard51.isId(data):
            self.__card = BrotherCard51()
        
        print ("found card:"+ self.__card.getName() )
        
        return self.__card

    def writeString(self,line):
        print( "command sending: "+ line )
        self.__con.write( str.encode(line+chr(13),'ascii' ))
        
    def readString(self):
        data = ""
        while True:
            for c in self.__con.read():
                #print type(c)
                #data = data + chr(c)
                data = data + c
                if self.__con.in_waiting == 0 and data != "":
                    return data[:-1]
        
    def readData(self, blockSize = 256):
        data = []
        i = 0
        while True:
            for d in self.__con.read():
                #print(d)
                data.append(d)
                if i >= 14+blockSize:
                    return data[12:-3]
                #time.sleep(0.04)
                i = i +1

    def erase(self):
        print("erase")
        card = self.getCard()
        code = card.gcErease()
        self.writeString(code)
        result = self.readString()
        print(result)
        
    def downloadFile(self, fileName):
        print("downloadFile")
        
        if os.path.exists(fileName):
            os.remove(fileName)
  
        #file = open(fileName,"a")
        #file.close()
        #time.sleep(0.5)
        
        card = self.getCard()
        codes = card.gcDump()
        file = open(fileName,"w+b")
        
        for i in codes:
            self.writeString(i)
            data = self.readData()
            file.write(bytearray(data))
            time.sleep(0.04)
            
        file.close()
            
    def writeData(self,addr,data):
        print( "command sending: "+ str(addr) +" "+ str(data[0:15]) + " ..." )
        #self.__con.write( str.encode("bws40 "+addr) )
        self.__con.write( str.encode("bws40 "+addr)+data+str.encode(chr(13)) )
        
    def uploadFile(self,fileName,blockSize=256):
        print("uploadFile")
        card= self.getCard()
        
        file = open(fileName, "rb")
        data = " "
        addr = 0
        #while len(data) > 0:
        while addr < 4096:
            data = file.read(blockSize)
            addrStr = ("00"+str(hex((addr>>8)&255))[2:])[-2:] +" "+ ("00"+str(hex((addr)&255))[2:])[-2:]
            if card.isWriteable(addr) and len(data) > 0:
                self.writeData(addrStr,data)
            addr = addr + 1
            time.sleep(0.04)
            
            
            