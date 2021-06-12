import os,getopt,sys
import CardReaders as CR


def showHelp():
    print("")
    print("-c       Defined the card reader.")
    print("         vub - Vikant Ultimate box")
    print("-p       Connection port of the card reader.")
    print("-d       Delete content from card.")
    print("-l       Load content from card and saves it to data folder.")
    print("-s       Stores content from data folder to card.")
    print("-f       Data folder.")
    print("")

def getCardReader(type):

    if type == "vub":
        return CR.VikantUltimateBox1.VikantUltimateBox1()
    
    raise Exception("Card reader of type('"+type+"') not supported.")

cr = None
    
def main():
    global cr
    
    reader   = "vub"
    port     = "com1"
    action   = "load"
    dataFile = "data.bin"
    
    try:
        opts, args = getopt.getopt( sys.argv[1:], "hc:p:dlsf:" )
    except getopt.GetoptError:
        showHelp()
        sys.exit(2)

    for opt, arg in opts:
        if  opt in ("-h"):
            showHelp()
            sys.exit()
        elif opt in ("-c" ):
            reader = arg
        elif opt in ("-p"):
            port = arg
            
        elif opt in ("-d"):
            action = "delete"
        elif opt in ("-l"):
            action = "load"
        elif opt in ("-s"):
            action = "store"
            
        elif opt in ("-f"):
            dataFile = arg

    #print "Reader: "+reader
    #print "port: "+port
    #print "action: "+ action
    #print "dataFile: "+ dataFile
    
    
    cr = getCardReader(reader)
    
    cr.connect(port)
    
    print "identify card reader:"
    cr.identify()

    print ""
    print "has card:"
    print str(cr.hasCard())
    
    print ""
    print "identify card:"
    cr.identifyCard()
    
    
    #if action == "delete":
    #    cr.erase()
    #elif action == "load":
    #    cr.downloadFile(dataFile)
    #elif action == "store":
    #    cr.uploadFile(dataFile)
    #else:
    #    print "action nicht erkannt."
     
     
    #cr.erase()
    cr.downloadFile(dataFile)
    

    
 
try:
    main()
finally:
    cr.disconnect()
    print "disconnected"
    