#!/usr/bin/env python3
"""
UTF-8 Validation
"""

from typing import List

def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Only consider the least significant 8 bits

        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

if __name__ == "__main__":
    data = [197, 130, 1]
    print(validUTF8(data))  # Output: True

