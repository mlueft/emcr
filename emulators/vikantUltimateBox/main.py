import serial

def toAscii(text):
    data = []
    for char in text:
        data.append(ord(char)) 
    return data
    
def toString(data):
    res = ""
    for c in data:
        res = res + chr(c)
    return res
    
def hex2bin():
    file1 = open("mem_hex.dat","rb")
    file = open("mem.dat","wb+")
    
    i = 0
    while i < 1048576:
        hex = file1.read(2)
        dec = int(hex,16)
        print(hex)
        print(dec)
        file.write(bytes([ord(chr(dec))]))
        i = i +1
        
    file1.close()
    file.close()

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

    file = open("mem.dat","rb+")
    file.seek(addr*blockSize)
    #for i in data:
    file.write( bytes(data) )
    file.close()
    
def readMemory(addr, blockSize=256):
    file = open("mem.dat","rb")
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
    
    tcmd = toString(cmd)

    if tcmd == "model":
        writeStrings(s,[tcmd,"UltimateBox 1000"])
        
    elif tcmd == "version":
        writeStrings(s,[tcmd,"UltimateBox Rev 1000"])
        
    elif tcmd == "cd":
        writeStrings(s,[tcmd,"Found"])
    

    
    elif tcmd == "id6":
        writeStrings(s,[tcmd+"01D50001"])

    elif tcmd == "id5":
        writeStrings(s,[tcmd+"43706F79"])
        
    elif tcmd == "id4":
        writeStrings(s,[tcmd+"01D50001"])
        
    elif tcmd == "id3":
        writeStrings(s,[tcmd+""])
        
    elif tcmd == "id2":
        writeStrings(s,[tcmd+""])
        
    elif tcmd == "id1":
        writeStrings(s,[tcmd+""])
        
    elif tcmd == "id0":
        writeStrings(s,[tcmd+""])
        

    elif tcmd == "erase40":
        writeStrings(s,[tcmd,"OK"])
        
        
    elif tcmd[:5] == "bws40":
        addr = getAddr(tcmd[:11])
        writeMemory(
            addr,
            cmd[11:]
        )
        
    elif tcmd[:5] == "bread":
        addr = getAddr(tcmd)
        data = readMemory(addr)
        writeData(s,str.encode(tcmd+"@")+data)

    else:
        print( "unknown command: "+tcmd )
    
def main():

    portIn  = "com129"

    
    port = serial.Serial(
        portIn,
        115200,
        timeout=0,
        parity=serial.PARITY_EVEN,
        rtscts=1
    )
    port.set_buffer_size(rx_size = 12800, tx_size = 12800)

    cmd = []

    while True:
        for c in port.read():
        
            if (c == 13 and cmd[:3] != toAscii("bws")):
                parseCommand(port, cmd)
                cmd = []
                
            elif (cmd[:3] == toAscii("bws") and len(cmd) == 268):
                parseCommand(port, cmd)
                cmd = [c]
                
            else:
                cmd.append(c)
                
    port.close()


#for i in range(0,1024):
#    data = readMemory(i)
#    writeMemory(i,data)

#writeMemory(3,"c",1)
#writeMemory(1,"A",1)
#writeMemory(2,"b",1)


#hex2bin()
main()


