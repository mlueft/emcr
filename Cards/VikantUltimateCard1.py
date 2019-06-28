import Cards.Card

class VikantUltimateCard1(Cards.Card.Card):

     def gcRease(self):
        return "erase40"  
        
    @staticmethod
    def isId(ids):
        myIds = [
            '43706F79',
            '01D50001'
        ]
        
        for i in myIds:
            if i not in ids:
                return False
        
        return True
        
    def __init__(self):
        pass
