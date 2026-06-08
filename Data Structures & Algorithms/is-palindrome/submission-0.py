class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #return s == s[::-1]
        # st , end = 0 , len(s) - 1

        # while st < end :
        
        res = ''
        for ch in s:
            if ch.isalnum():
                res += ch.lower()
        return res == res[::-1]
