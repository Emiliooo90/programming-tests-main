# Aquí programa una función que resuelva el problema 1 FizzBuz

def fizzbuzz_function():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(n, "FizzBuzz")
        elif n % 3 == 0:
            print(n, "Fizz")
        elif n % 5 == 0:
            print(n, "Buzz")

fizzbuzz_function()
    


