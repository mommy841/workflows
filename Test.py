# test_lint.py

import os, sys

def say_hello(name):
    print( "Hello, " +name+"!" )  # extra spaces and missing proper spacing

def add_numbers(a,b):
    return a+b   # missing spaces around operator

def unused_function():
    pass  # This function is never used

say_hello("World")
print(add_numbers(3,4))