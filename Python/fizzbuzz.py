'''''###Print numbers from 1 to 50:

Multiples of 3 → "Fizz"
Multiples of 5 → "Buzz"
Both → "FizzBuzz"'''''

n = 1
while n <= 50:
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

    n += 1