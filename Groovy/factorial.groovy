def fact(n) {
    if (n <= 1) {
        return 1
    } else {
        n = fact(n-1) * n
    }
}

def number = System.console().readLine 'What is your number: '
println fact(Integer.parseInt(number))