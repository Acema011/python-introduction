def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

def compute():
    for i in range(1, 15):
        print(fizzbuzz(i))