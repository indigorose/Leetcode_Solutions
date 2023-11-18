# For a 1d array return an array of it's running total.

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         answer = []
#         r = 0
#         for i in range(len(nums)):
#             r += nums[i]
#             answer.append(r)
#         return answer