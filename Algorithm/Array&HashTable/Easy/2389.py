class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []

        for query in queries:
            counter = 0
            numsSum = 0
            while numsSum <= query and counter < len(nums):
                numsSum += nums[counter]
                counter += 1
            if numsSum <= query:
                res.append(counter)
            else:
                res.append(counter-1)
        return res


# better answer
class Solution: 
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = list(accumulate(sorted(nums)))
        return [bisect_right(prefix, q) for q in queries]