class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        savedmails = set()
        for mail in emails:

            temp = ""
            for ch in mail:
                if ch == '@' or ch == '+': break
                if ch != '.':
                    temp += ch
            
            for i in range(len(mail)):
                if mail[i] == '@':
                    break
            
            domain = mail[i + 1 :]
            savedmails.add((temp, domain))

        return len(savedmails)