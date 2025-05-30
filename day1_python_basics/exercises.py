# Day 1: Python Basics

def even_or_odd(number: int):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def sum_of_numbers(number: int):
    total = 0
    for i in range(1, number + 1):
        total += i
    print(total)

def fizz_buzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

def max_of_three(a: int, b: int, c: int):
    print(max(a, b, c))

import random
def guess_random_number():
    random_number = random.randint(1, 10)
    while True:
        number = int(input('Guess the number from 1 to 10: '))
        if number == random_number:
            print('You guessed it right')
            return True
        elif number > random_number:
            print('Your guess number is high')
        else:
            print('Your guess number is low')
