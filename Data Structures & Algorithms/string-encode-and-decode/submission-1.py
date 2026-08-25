class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     s = ""
    #     for i in strs:
    #         s += i + "*#@"
    #     return s

    # def decode(self, s: str) -> List[str]:
    #     final = s.split("*#@")
    #     if(final[-1] == ""):
    #         final.pop()
    #     return final

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j]) #what is two or three digit number
            final.append(s[j+1:j+1+length])
            i = j+1+length
        return final
                



    #there are other approaches as well like appending length with demiliter for each string in ecoding

