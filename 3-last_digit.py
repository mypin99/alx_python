#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Check if the number is negative and adjust the last digit accordingly
if number < 0:
    last_digit *= -1

# Print the result
print("The string Last digit of", number, "is", last_digit, end=" ")

# Check the value of the last digit and print the appropriate message
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")