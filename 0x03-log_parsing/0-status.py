#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the current statistics."""
    print(f"Total file size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip, _, _, date, _, request, status, size = parts
        if request != '"GET /projects/260 HTTP/1.1"':
            continue
        status = int(status)
        size = int(size)
        total_size += size
        if status in status_counts:
            status_counts[status] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue

# Print final statistics after processing all lines
print_stats()

