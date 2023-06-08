func countKDifference(nums []int, k int) int {
    var l int
    var r int
    var res int
    for l < len(nums)-1 {
        r = l+1
        for r < len(nums) {
            if math.Abs(float64(nums[l]-nums[r])) == float64(k) {
                res += 1
            }
            r += 1
        }
        l += 1
    }
    return res
}