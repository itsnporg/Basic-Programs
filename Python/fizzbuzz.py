def fizzbuzz(n: int) -> list[int | str]:
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        
        elif i % 5 == 0:
            result.append("Buzz")
        
        else:
            result.append(str(i))

    return result

print(fizzbuzz(100))
