#!/usr/bin/env python3
import sys

# Get the total number of arguments
num_args = len(sys.argv) - 1

if num_args == 0:
    # No arguments passed
    print("0 arguments.")
elif num_args == 1:
    # One argument passed
    print("1 argument:")
    print(f"1: {sys.argv[1]}")
else:
    # More than one argument passed
    print(f"{num_args} arguments:")
    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")
