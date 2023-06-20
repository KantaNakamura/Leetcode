class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        exist = set()
        l, r = 0, 1
        while r < len(nums):
            subarray = nums[l] + nums[r] 
            if subarray in exist:
                return True
            else:
                exist.add(subarray)
            l += 1
            r += 1
        return False