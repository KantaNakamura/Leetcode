class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right+1):
            if self.isPrime(self.countNumberOfOneFromBinary(i)):
                ans += 1
        
        return ans


    def countNumberOfOneFromBinary(self, s):
        binary = ''
        ans = 0
        while s > 0:
            remainder = s % 2
            binary = str(remainder) + binary
            s = s//2
            if remainder == 1:
                ans += 1
        return ans

    def isPrime(self, s):
        if s <= 1:
            return False

        for i in range(2, int(sqrt(s))+1):
            if s%i == 0:
                return False
        return True
