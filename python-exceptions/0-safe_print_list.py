#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list on one line; return count printed."""
    printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed += 1
        except IndexError:
            break
    print()
    return printed
