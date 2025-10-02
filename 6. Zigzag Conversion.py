class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = ['']*numRows

        current_row = 0

        going_down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                going_down = True   # start going down

            elif current_row == numRows - 1:
                going_down = False  # start going up

            if going_down==True:
                current_row += 1   # move down one row
            else:
                current_row -= 1   # move up one row

       # print(rows)

        return ''.join(rows)
