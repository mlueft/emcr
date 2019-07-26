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

    
def main():

    reader   = "vub"
    port     = "com1"
    action   = "load"
    dataFile = "data.bin"
    
    try:
        opts, args = getopt.getopt( sys.argv[1:], "hc:p:dlsf" )
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

    cr = getCardReader(reader)
    
    cr.connect(port)
    
    cr.identify()

    #cr.erase()
    #cr.uploadFile("card.dmp")
    
    cr.downloadFile("card1.dmp")
    cr.writeFile("data.bin")
    
    cr.disconnect()
 

main()