import Cards.Card

class BrotherCard51(Cards.Card.Card):

    @staticmethod
    def isId(ids):
        myIds = [
            '43706F79'
        ]
        
        for i in myIds:
            if i not in ids:
                return False
        
        return True
        
    def getName(self):
        return "BrotherCard51"
        
    def gcDump(self):
        
        data = []
        for i in range(0,16):
            for j in range(0,256):
                data.append( "bread "+ self._hex(i) +" "+ self._hex(j)    )
                
        return data