func isPowerOfTwo(n int) bool {
    if n<=0{
        return false 
    }  
    if n==1{
        return true
    }
    if n%2==1{
        return false
    }
    n = n/2
    res := isPowerOfTwo(n)
    return res
}