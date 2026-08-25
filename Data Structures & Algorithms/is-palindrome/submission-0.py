class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(char.lower() for char in s if char.isalnum()) #isalnum checks if its alphanumeric

        i, j = 0, len(s1) - 1
        for i in range(len(s1)):
            if (s1[i]==s1[j]):
                i+=1
                j-=1
            else: return False
        return True
        