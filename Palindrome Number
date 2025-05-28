class Solution:
    def isPalindrome(self,x:int)->bool:
        digit = 0
        original = x
        reverse = 0

        while x>0:
            digit = x%10
            reverse = reverse*10 + digit
            x = x//10

        if reverse == original:
            return True
        else:
            return False
