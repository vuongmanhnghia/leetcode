import math

class Solution:
    def reverse(self, x: int) -> int:
        reverseNumber = 0

        MIN = -2147483648
        MAX = 2147483647

        while (x != 0):
            remainder = int(math.fmod(x, 10))
            x = int(x / 10)
            
            if (reverseNumber < MIN // 10 or (reverseNumber == MIN // 10 and remainder <= MIN % 10)):
                return 0

            if (reverseNumber > MAX // 10 or (reverseNumber == MAX // 10 and remainder >= MAX % 10)):
                return 0

            reverseNumber = reverseNumber * 10 + remainder
           
        return reverseNumber

solution = Solution()
x = int(input("Nhap so: "))
result = solution.reverse(x)
print(f"result: {result}")
