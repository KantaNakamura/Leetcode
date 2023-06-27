class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        while l <= r:
            mid = (l+r) // 2
            coins = (mid/2) * (mid+1)
            if n < coins:
                r = mid -1
            else:
                l = mid + 1
                res = max(mid, res)
        return res