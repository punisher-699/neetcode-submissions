class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
       
        fives_count = tens_count = 0
        for b in bills:
            if b == 5:
                fives_count += 1
            elif b == 10:
                if fives_count == 0:
                    return False
                fives_count -= 1
                tens_count += 1
            else:
                if tens_count > 0 and fives_count > 0:
                    tens_count -= 1
                    fives_count -= 1
                elif fives_count >= 3:
                    fives_count -= 3
                else: return False
        
        return True

                