class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        #we do numrows sep substrs
        temp = [[] for _ in range(numRows)]
        slen = len(s)
        i = 0
        while i < slen:

            #top to down
            j = 0
            while j < numRows and i < slen:
                temp[j].append(s[i])
                i += 1
                j += 1
               
            while j > 2 and i < slen:
                j -= 1
                temp[j - 1].append(s[i])
                #temp[j].append(s[i])
                i += 1
        
        return ''.join(''.join(row) for row in temp)

