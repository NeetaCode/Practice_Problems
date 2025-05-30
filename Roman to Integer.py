class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map ={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000  
        }
        res=0
        prev=0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev:
                res -= value
            else:
                res += value
            prev = value

        return res

        
        return res
        
