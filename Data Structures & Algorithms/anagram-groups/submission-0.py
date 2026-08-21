class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: #we ar ematching occurences of each letter array as key to all strings which have same letters as value in hashmap
        res = defaultdict(list) #to prevent edge case if dict exists or not
        
        for s in strs:
            count = [0]*26 # max lowercase alphabets we have are 26 = count[0,0,0...26times]
            for c in s: #count occurence of each alphabet in each string 
                count[ord(c) - ord("a")] = count[ord(c) - ord("a")] +1 #ord() if gets ascii/unicode interger of each string , eg for "a" ord("a")-ord("a") = 0
            res[tuple(count)].append(s)  #dictionary does not take in list, it can take tuple since it cant be changed 
        return list(res.values())
      