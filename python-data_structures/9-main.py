#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Extra checks:
print(max_integer([]))          # None
print(max_integer([42]))        # 42
print(max_integer([-5, -1]))    # -1
