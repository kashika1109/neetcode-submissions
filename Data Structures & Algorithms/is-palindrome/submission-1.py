class Solution:
    def isAlphaNumeric(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        # s1 = ''.join(char.lower() for char in s if char.isalnum()) #isalnum checks if its alphanumeric

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.isAlphaNumeric(s[i]):
                i+=1
            while i < j and not self.isAlphaNumeric(s[j]):
                j-=1
            
            if(s[i].lower() != s[j].lower()): return False
            
            i+=1
            j-=1
        return True


        
        