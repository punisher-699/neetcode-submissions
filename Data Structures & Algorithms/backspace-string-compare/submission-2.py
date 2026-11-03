class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        temps = ""
        tempt = ""

        for ch in s:
            if ch == '#':
                temps = temps[:-1]
            else:
                temps += ch
        for ch in t:
            if ch == '#':
                tempt = tempt[:-1]
            else:
                tempt += ch
        
        
        return tempt == temps
