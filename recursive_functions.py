# file name: recursive_functions.py 
# by: Ben Silbernagel
# date: 6/8/2016
# class: Intro to Computer Science, by Udacity
# purpose: functions to be used to create a hash table

def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        elif n > 1:
            return fibonacci(n-1) + fibonacci(n-2)