class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "": return []

        ht = { 2 : "abc", 3 : "def", 4: "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
        if len(digits) == 1:
            return list(ht[int(digits[0])])
        def bt(d, strs):
            temp = []
            for chara in strs:
                for charb in ht[d]:

                    temp.append(chara + charb)
            return temp

        #init
        strs = ht[int(digits[0])]

        for d in digits[1:]:

            #bt(int(d), ht[int(d)])
            strs = bt(int(d), strs)
        
        return strs


