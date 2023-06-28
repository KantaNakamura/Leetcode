class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_len += 1
            else:
                max_len = max(cur_len, max_len)
                cur_len = 1
        return max(cur_len, max_len)

