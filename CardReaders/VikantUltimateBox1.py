import CardReaders.CardReader
import serial, time

class VikantUltimateBox1(CardReaders.CardReader.CardReader):

    def __init__(self):
        self.__sepperator = chr(13)+chr(10)
        self.__terminator = chr(62)
        
    def disconnect(self):
        self.__con.close()
        
    def connect(self, port):
        self.__con = serial.Serial(
            port,
            9600,
            timeout=0,
            parity=serial.PARITY_EVEN,
            rtscts=1
        )
    
    def identify(self):
        self.writeString("version")
        time.sleep(1)
        answer0 = self.readString()
        
        self.writeString("model")
        time.sleep(1)
        answer1 = self.readString()
        
        if "UltimateBox" not in answer0:
            raise Exception("Card reader not recognized.("+answer0+")")
            
        if "UltimateBox" not in answer1:
            raise Exception("Card reader not recognized.("+answer1+")")
    
    def hasCard(self):
        self.writeString("cd")
        time.sleep(1)
        answer = self.readString()
        
        if "Not Found" in answer:
            return False
            
        return True
    
    def getCard(self):
        
        if not self.hasCard():
            return None
            
        card = None
        
        id = 6
        
        data = []
        while id >= 0:
        
            self.writeString("id"+str(id))
            time.sleep(1)
            answer = self.readString()
            
            data.append(answer)
            
            id = id -1
        
        
        
        if card == None:
            raise Exception("Card not recognized.")

    def writeString(self,line):
        self.__con.write(str.encode( line+chr(13) ))
        
    def readString(self):
        data = ""
        
        while True:
            for c in self.__con.read():
                data = data + chr(c)
                    
                if data[-1:] == self.__terminator:
                    return data[:-1]
        