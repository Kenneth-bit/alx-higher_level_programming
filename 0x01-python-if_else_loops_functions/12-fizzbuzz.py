#!/usr/bin/python3
def fizzbuzz():
    count = 1
    while count < 101:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz", end=' ')
            count += 1
        elif count % 5 == 0:
            print("Buzz", end=' ')
            count += 1
        elif count % 3 == 0:
            print("Fizz", end=' ')
            count += 1
        else:
            print(count, end=' ')
            count += 1
