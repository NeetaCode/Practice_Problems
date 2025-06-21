class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words= s.split()
        size_of_array =len(words)
        last_word = words[size_of_array-1]
        res=len(last_word)
                
        return res
        
print(length_of_last_word("Hello World"))  
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         # Strip trailing spaces and split the string by spaces
#         words = s.strip().split()
#         # Return the length of the last word
#         return len(words[-1])
