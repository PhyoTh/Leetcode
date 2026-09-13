from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort() # O(nlogn)
        cardCount = Counter(hand) # O(n)
        for card in hand:
            if cardCount[card] == 0:
                continue
            
            make = card
            groupCount = 0
            while make in cardCount and cardCount[make] > 0 and groupCount < groupSize:
                cardCount[make] -= 1
                make += 1
                groupCount += 1
                
            if groupCount != groupSize:
                return False
        
        return True