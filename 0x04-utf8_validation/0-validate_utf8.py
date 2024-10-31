#!/usr/bin/python3
"""
This script contains a function to determine if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Check if the given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is valid UTF-8, else False
    """
    num_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0

# Example usage
if __name__ == "__main__":
    data1 = [197, 130, 1]  # Valid UTF-8
    print(validUTF8(data1))  # Output: True

    data2 = [235, 140, 4]  # Invalid UTF-8
    print(validUTF8(data2))  # Output: False
