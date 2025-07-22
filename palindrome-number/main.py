class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0): return False

        div = 1

        while x > div * 10:
            div *= 10

        while x:
            if x % 10 != x // div: return False
            
            x = (x % div ) // 10
            div = div // 100
            
        return True

solution = Solution()

x = int(input("Nhap x: "))
result = solution.isPalindrome(x)
print(result)
