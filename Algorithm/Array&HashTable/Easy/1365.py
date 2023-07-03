# [My answer] time 5:22 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums.copy())
        res = []

        for num in nums:
            res.append(sortedNums.index(num))
        return res