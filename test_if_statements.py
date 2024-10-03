#!/usr/bin/env python3

# Test 1: Using if True
if True:
    print('This print is part of the if statement')

# Test 2: Using if False
if False:
    print('This first print statement will never run')
    print('This second print statement will also not run')
print('This print statement will run')

# Test 3: Using a conditional with input
password = input('Please enter a secret password: ')
if password == 'P@ssw0rd':
    print('You have successfully used the right password')

