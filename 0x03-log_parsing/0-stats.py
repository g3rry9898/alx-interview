#!/usr/bin/python3
"""
Log Parsing Script

This script reads stdin line by line and computes metrics based on log entries.
"""

import sys

total_size = 0
status_counts = {
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
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status, count))

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        ip, dash, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[-2], parts[-1]

        try:
            total_size += int(file_size)
        except ValueError:
            continue

        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()

