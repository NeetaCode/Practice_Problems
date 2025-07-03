from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, fp, bp):
            if len(current) == 2 * n:
                result.append(current)
                return

            if fp < n:
                backtrack(current + "(", fp + 1, bp)

            if bp < fp:
                backtrack(current + ")", fp, bp + 1)

        backtrack("", 0, 0)
        return result
