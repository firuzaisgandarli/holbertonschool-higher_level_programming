#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal’s triangle of n.
    Args:
        n (int): number of rows
    Returns:
        list: Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        # Yeni sətir həmişə 1 ilə başlayır və 1 ilə bitir
        row = [1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
