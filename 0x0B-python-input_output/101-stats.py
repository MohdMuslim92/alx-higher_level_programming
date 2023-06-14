#!/usr/bin/python3

"""This module reads stdin line by line and computes metrics"""


import sys


def print_stats(total_size, status_counts):
    """Function that prints statistics after each 10 lines and
    after a keyboard interruption (CTRL + C) since the beginning

    args :
        total_size : total file size
        status_counts : the count of status code
        """
    print(f"Total file size: {total_size}")
    print("Number of lines by status code:")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def process_input():
    """This function reads from the stdin and parse the lines,
    tokenize the lines to extract the file size and the status
    code and then sends them to the function print_stats after
    readin each 10 lines and after interrupting with keyboard
    (CTRL + C)"""
    total_size = 0
    status_counts = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            token = line.split()
            status_code = int(token[-2])
            file_size = int(token[-1])

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


process_input()
