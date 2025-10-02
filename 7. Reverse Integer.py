class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        int_max=2**31-1

        sign = 1
            
        if x<0:
            sign = -1
        
        x=abs(x)
        reverse=0

        while x!=0:
            digit= x%10 
            x=x//10

            if(reverse>(int_max - digit)//10):
                return 0

            reverse = reverse*10+digit

        return reverse*sign
