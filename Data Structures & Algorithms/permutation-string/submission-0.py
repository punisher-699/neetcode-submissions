class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1dic = {}
        for ch in s1:
            s1dic[ch] = s1dic.get(ch, 0) + 1
        ws = len(s1)
        for i,ch in enumerate(s2):
            st = i
            end = i + ws
            if end > len(s2): break
            temp = {}
            for il in range( st , end ):
                temp[s2[il]] = temp.get(s2[il], 0) + 1
            if temp == s1dic :
                return True
        return False