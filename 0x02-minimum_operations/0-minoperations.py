#!/usr/bin/python3
"""
This module provides a function to calculate the minimum operations
needed to result in exactly n H characters in a file using Copy All
and Paste operations.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly
    n H characters in the file.

    :param n: Number of H characters desired
    :return: Minimum number of operations to achieve n H characters, or 0 if impossible
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations

# Example usage
if __name__ == "__main__":
    n = 9
    print("Min operations to get {} H characters: {}".format(n, minOperations(n)))

