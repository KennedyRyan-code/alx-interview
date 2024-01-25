#!/usr/bin/python3
import sys
from collections import defaultdict
import signal


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}


def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    print_stats(total_size, status_counts)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
total_size = 0
status_counts = defaultdict(int)

try:
    for line in sys.stdin:
        line = line.strip()

        # Parsing the line
        try:
            _, _, _, _, _, status_code, file_size = line.split(" ")
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError or IndexError:
            # Skip the line if the format is not as expected
            continue

        # Update metrics
        line_count += 1
        total_size += file_size
        status_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass  # Handle KeyboardInterrupt outside the loop

print_stats(total_size, status_counts)
