#!/usr/bin/python3
a = 1
print(is_same_class(a, int))      # Output: True

a = True
print(is_same_class(a, int))      # Output: False

a = 3.14
print(is_same_class(a, int))      # Output: False

a = True
print(is_same_class(a, object))   # Output: True

a = None
print(is_same_class(a, object))   # Output: True

a = None
print(is_same_class(a, list))     # Output: False

a = [1, 2, 3]
print(is_same_class(a, list))     # Output: True

a = [1, 2, 3]
print(is_same_class(a, object))   # Output: False
