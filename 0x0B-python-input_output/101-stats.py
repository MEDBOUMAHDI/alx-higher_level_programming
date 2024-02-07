#!/usr/bin/python3
"""
Log Parsing

This script parses a log of HTTP GET request results from stdin and tabulates
the total counts of status codes appearing in each response, as well as the
total file size across all requests.

Example of expected log line input:
128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" 301 292

Fields:
<IP Address> - [<Date>] "<GET request>" <Response status code> <File size>
"""


def print_log_totals(total_file_size, code_counts):
    print(f"File size: {total_file_size}")
    for code, count in code_counts.items():
        if count > 0:
            print(f"{code}: {count}")


if __name__ == '__main__':
    from sys import argv, stdin, stderr
    from collections import OrderedDict
    from datetime import datetime

    line_no = 0
    total_file_size = 0
    code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in stdin:
            line_no += 1

            components = line.split('-', 1)
            if len(components) != 2:
                continue

            timestamp = components[1].split(']')[0].strip(' []')
            try:
                datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                stderr.write(f"{argv[0]}: {line_no}: invalid timestamp\n")
                continue

            url_components = components[1].split('"')[1:]
            if url_components[0] != 'GET /projects/260 HTTP/1.1':
                stderr.write(f"{argv[0]}: {line_no}: unexpected HTTP request\n")
                continue

            status_code, file_size = url_components[1].strip().split(' ')
            
            if status_code.isdigit():
                code = int(status_code)
                code_counts[code] += 1

            if file_size.isdigit():
                total_file_size += int(file_size)

            if line_no % 10 == 0:
                print_log_totals(total_file_size, code_counts)
        
        print_log_totals(total_file_size, code_counts)

    except KeyboardInterrupt:
        print_log_totals(total_file_size, code_counts)
        raise
