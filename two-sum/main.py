from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            second_number = target - n
            if second_number in hashMap:
                return [hashMap[second_number], i]
            hashMap[n] = i
        return []


solution = Solution()
print("Typing array: ")
nums = [int(x) for x in input().split()]
target = int(input("Target: "))
print(f"Result: {solution.twoSum(nums, target)}")
