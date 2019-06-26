import serial



def writeStrings(s,lines):
    sep = chr(13)+chr(10)
    term = chr(62)
    for l in lines:
        s.write(str.encode( l +sep ))
    s.write(str.encode( term ))
    
def writeData(s,data):
    sep = chr(13)+chr(10)
    term = chr(62)
    s.write(data)
    s.write(str.encode( sep+term ))

def writeMemory(addr,data,blockSize=256):
    file = open("mem1.dat","b+")
    file.seek(addr*blockSize)
    file.write(data);
    file.close()

    
def readMemory(addr, blockSize=256):
    file = open("mem1.dat","rb")
    file.seek(addr*blockSize)
    data = file.read(blockSize);
    file.close()
    return data

def getAddr(cmd):
    parts = cmd.split(" ")
    addr = int(parts[1]+parts[2],16)
    
    #print(cmd)
    #print(parts)
    #print(addr)
    #print("-----------------------")
        
    return addr
    
def parseCommand(s,cmd):
    if cmd == "model":
        writeStrings(s,[cmd,"UltimateBox 1000"])
        
    elif cmd == "version":
        writeStrings(s,[cmd,"UltimateBox Rev 1000"])
        
    elif cmd == "cd":
        writeStrings(s,[cmd,"Found"])
    

    
    elif cmd == "id6":
        writeStrings(s,[cmd+"01D50001"])

    elif cmd == "id5":
        writeStrings(s,[cmd+"43706F79"])
        
    elif cmd == "id4":
        writeStrings(s,[cmd+"01D50001"])
        
    elif cmd == "id3":
        writeStrings(s,[cmd+""])
        
    elif cmd == "id2":
        writeStrings(s,[cmd+""])
        
    elif cmd == "id1":
        writeStrings(s,[cmd+""])
        
    elif cmd == "id0":
        writeStrings(s,[cmd+""])
        

    elif cmd == "erase40":
        writeStrings(s,[cmd,"OK"])
        
        
    elif cmd[:5] == "bws40":
        addr = getAddr(cmd)
        #writeData(s,str.encode(cmd+"@"))
        
    elif cmd[:5] == "bread":
        addr = getAddr(cmd)
        data = readMemory(addr)
        writeData(s,str.encode(cmd+"@")+data)


    else:
        print( "unknown command: "+cmd )
    
def main():

    portIn  = "com12"

    
    port = serial.Serial(
        portIn,
        9600,
        timeout=0,
        parity=serial.PARITY_EVEN,
        rtscts=1
    )
    port.set_buffer_size(rx_size = 12800, tx_size = 12800)

    cmd = ""

    while True:
        for c in port.read():
            if c != 13:
                cmd = cmd + chr(c)
                
            if c == 13:
                parseCommand(port, cmd)
                cmd = ""
                
    port.close()

main()


