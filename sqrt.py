class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 1
        low = 1
        high = x

        while(low <= high):
            mid = low + (high-low)/2
            
            if(mid*mid <= x):
            
                res = mid
                low = mid+1
            
            else:
            
                high = mid -1
            
        
        return res
        
