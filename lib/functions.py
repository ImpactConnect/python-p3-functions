#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    
greet_programmer()

def greet(name):
    print(f'Hello, {name}!')

greet('programmer')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')
greet_with_default()

def add(num1, num2):
    return num1 + num2

sum = add(45, 55)
print(sum)


def halve(number):
    if type(number) not in (int, float):
        return None

    return number / 2

halve = halve('99')
print(halve)