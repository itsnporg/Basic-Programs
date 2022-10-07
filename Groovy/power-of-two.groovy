def isPowerOfTwo(n){

    if (n == 0) {
        return false
    }

    res = n & (n-1)
    if (res == 0) {
        return true
    }

    return false
}

def number = System.console().readLine 'Power of two checker. What is your number: '
println isPowerOfTwo(Integer.parseInt(number))