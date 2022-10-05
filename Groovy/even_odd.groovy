def fact(n) {
    if (n % 2 == 0) {
        return "It's even number"
    } else {
       return "It's odd number"
    }
}

def number = System.console().readLine 'What is your number: '
println fact(Integer.parseInt(number))