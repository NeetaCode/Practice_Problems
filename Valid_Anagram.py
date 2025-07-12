class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for char in s:
            #dictionary[key] = value
            count_s[char] = count_s.get(char,0)+1
            # .get(char,0)+1
            # .get(char --> means get current count
            # ,0 --> return 0 if there is no current count return 0
            # )+1 --> increment the current count by 1, if the char is found.
        
        print(count_s)

        for char in t:
             #dictionary[key] = value
            count_t[char] = count_t.get(char,0)+1

        print(count_t)

        return count_s==count_t
