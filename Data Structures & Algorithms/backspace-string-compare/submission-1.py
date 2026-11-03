class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass
        temps = ""
        tempt = ""

        for ch in s:
            if ch == '#':
                temps = temps[:-1]
            else:
                temps += ch
        for ch in t:
            if ch == '#':
                temps = temps[:-1]
            else:
                temps += ch
        
        
        return tempt == temps
