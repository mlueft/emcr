import serial


def writeString(line):
    global __con
    #__con.rts = True
    #__con.rts = False
    __con.write( str.encode( line+chr(13),'ascii' ))
    
def readString():
    global __con
    #__con.rts = False
    #__con.rts = True
    print("readString")
    data = ""
    
    while True:
        for c in __con.read():
            print( str( __con.in_waiting) +" => "+ data )
            data = data + chr(c)
                
            #if data[-1:] == chr(62):
            #    print("return")
            #    return data[:-1]
    
                
port = "com1"


__con = serial.Serial(
    port = port,
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
#__con.set_buffer_size(rx_size = 12800, tx_size = 12800)
#print("__con.BAUDRATES:")
#print(__con.BAUDRATES)
#print("__con.BYTESIZES:")
#print(__con.BYTESIZES)
#print("__con.PARITIES:")
#print(__con.PARITIES)
#print("__con.STOPBITS:")
#print(__con.STOPBITS)
#settings = __con.get_settings()
#print(settings)
#settings["baudrate"]           = 57600     # IOCTL_SERIAL_SET_BAUD_RATE 
#settings["bytesize"]           = 7         # IOCTL_SERIAL_SET_LINE_CONTROL 5 6 7 8
#settings["paritystopbits"]     = "E"       # N E O M S
#settings["stopbits"]           = 1         # 1 1.5 2
#settings["xonxoff"]            = False
#settings["dsrdtr"]             = False
#settings["rtscts"]             = False
#settings["timeout"]            = 0
#settings["write_timeout"]      = 0
#settings["inter_byte_timeout"] = 0
#__con.apply_settings( settings )

#__con.open()

writeString("\r")
writeString("version")
readString()

__con.close()