import time

class Card(object):
    
    def getName(self):
        return ""
    
    def _hex(self, i):
        data = hex(i)[2:]
        
        if len(data) == 1:
            data = "0"+data
            
        return data.upper()
        
    def gcErease(self):
        return "erase40" 
        
    def gcDump(self):
        return []
        
    def isWriteable(self,addr):
        return False
