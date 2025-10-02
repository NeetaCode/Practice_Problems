class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Define integer range limits
        int_min = -2**31      # -2147483648
        int_max = 2**31 - 1   # 2147483647

        # Step 2: Initialize variables
        i = 0                 # index pointer
        n = len(s)            # length of the string
        sign = 1              # default sign is positive
        res = 0               # result starts at 0

        # Step 3: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 4: Handle sign if present
        if i < n:
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                sign = 1
                i += 1

        # Step 5: Convert digits into integer
        while i < n and s[i].isdigit():
            digit = int(s[i])             # convert character to integer
            res = res * 10 + digit        # shift left and add new digit
            i += 1

        # Step 6: Apply sign
        res = res * sign

        # Step 7: Clamp the result within 32-bit signed integer range
        if res < int_min:
            return int_min
        if res > int_max:
            return int_max

        return res
