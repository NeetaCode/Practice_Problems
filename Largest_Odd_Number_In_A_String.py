class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        whole_num = int(num)

        if whole_num % 2 != 0:
            return num  # whole string is already odd

        max_odd_index = -1
        for i, c in enumerate(num):
            if int(c) % 2 == 1:
                max_odd_index = i

        if max_odd_index == -1:
            return ""

        # Build the substring manually without slicing
        result = ""
        for j in range(max_odd_index + 1):
            result += num[j]

        return result
