class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        result = s[0]

        F = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            F[i][i] = 1

        for window in range(2, size + 1):
            for i in range(0, size - window + 1):
                j = i + window - 1

                if window == 2 and s[i] == s[j]:
                    F[i][j] = 1

                elif s[i] == s[j] and F[i + 1][j - 1] == 1:
                    F[i][j] = 1

                if F[i][j] == 1 and window > len(result):
                    result = s[i : j + 1]

        return result


s = input("Nhap xau ky tu s... : ")

solution = Solution()
result = solution.longestPalindrome(s)
print(f"Result: {result}")
