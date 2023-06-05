func minimumRecolors(blocks string, k int) int {
    l := 0
    r := k
    ans := 100
    for r <= len(blocks) {
        ans = min(ans, strings.Count(blocks[l:r], "W"))
        l += 1
        r += 1
    }
    return ans
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}