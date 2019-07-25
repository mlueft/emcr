import Cards.Card

class VikantUltimateCard1(Cards.Card.Card):

    @staticmethod
    def isId(ids):
        myIds = [
            '01D50001'
        ]
        
        for i in myIds:
            if i not in ids:
                return False
        
        return True
        
    def _hex(self, i):
        data = hex(i)[2:]
        
        if len(data) == 1:
            data = "0"+data
            
        return data.upper()
    
    def __init__(self):
        pass

    def gcErease(self):
        return "erase40" 
        
    def gcDump(self):
        
        data = []
        #for i in range(0,16):
        for i in range(0,1):
            for j in range(0,256):
                data.append( "bread "+ self._hex(i) +" "+ self._hex(j)    )
                
        return data
        
    def isWriteable(self,addr):
        return True
        if addr <= 1:
            return True
            
        if addr == 16:
            return True
            
        if addr >= 65:
            return True
        
        return False