# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n-1

        while l <= r:
            index = (l+r)//2
            if isBadVersion(index):
                r = index-1
            else:
                l = index+1
        return l