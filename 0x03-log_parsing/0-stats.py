#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics """

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        elements = line.split()
        try:
            if elements[5] not in status_codes:
                continue
            status_codes[int(elements[5])] += 1
            total_size += int(elements[6])
        except (IndexError, ValueError):
            continue
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for key in sorted(status_codes.keys()):
                if status_codes[key] > 0:
                    print(f"{key}: {status_codes[key]}")
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f"{key}: {status_codes[key]}")
