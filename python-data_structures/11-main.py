#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)  # [1, 2, 3, 5]
print(my_list)   # [1, 2, 3, 5]

# Extra checks:
print(delete_at([1, 2, 3], -1))   # [1, 2, 3]
print(delete_at([1, 2, 3], 10))   # [1, 2, 3]
print(delete_at([42], 0))         # []
