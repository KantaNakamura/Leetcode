func countPrimeSetBits(left int, right int) int {
    var ans int
    for left <= right {
        if isPrime(countOneFromBinary(left)) {
            ans += 1
        }
        left += 1
    }
    return ans
}

func countOneFromBinary(decimal int) int {
    var binary string
    var numberOfOne int
    for decimal > 0 {
		remainder := decimal % 2
		binary = strconv.Itoa(remainder) + binary
        if strconv.Itoa(remainder) == "1" {
            numberOfOne += 1
        }
		decimal = decimal / 2
    }
    return numberOfOne
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}

	sqrt := int(math.Sqrt(float64(n)))
	for i := 2; i <= sqrt; i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}