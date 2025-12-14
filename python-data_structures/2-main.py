#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)  # [1, 2, 3, 9, 5]
print(my_list)   # [1, 2, 3, 9, 5]

# Extra checks:
print(replace_in_list([1, 2, 3], -1, 99))  # [1, 2, 3]
print(replace_in_list([1, 2, 3], 3, 99))   # [1, 2, 3]
print(replace_in_list([1], 0, 42))         # [42]
