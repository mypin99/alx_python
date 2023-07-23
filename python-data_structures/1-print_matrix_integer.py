#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to print the integer without casting it to a string explicitly
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                # Print a space after each element except the last one in the row
                print(" ", end="")
        print()  # Move to the next line after printing each row