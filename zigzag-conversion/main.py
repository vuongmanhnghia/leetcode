class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        size = len(s)
        group = 2 * (numRows - 1)

        result = ""

        for i in range(numRows):
            for j in range(0,  size - i, group):
                result += s[i + j]

                notFirstRow = i != 0
                notLastRow = i != numRows - 1;
                nextMiddleChar = j + group - i < size

                if notFirstRow and notLastRow and nextMiddleChar:
                    result += s[j + group - i]

        return result

solution = Solution()
s = "PAYPALISHIRING"

result = solution.convert(s, 3)
print(f"result: {result}")

