#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics for
IP Address, date, HTTP request status code, and file size.
"""

import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_stats():
    """ Print the accumulated statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    line_count = 0
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue

        ip, dash, date, request, request_line, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[6], parts[8]

        try:
            total_size += int(file_size)
        except ValueError:
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()

