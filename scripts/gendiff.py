#!/usr/bin/env python

import argparse
import json


def generate_diff(file1, file2):
    result = ''
    keys_file1 = file1.keys()
    keys_file2 = file2.keys()
    keys_file3 = list(set(keys_file1) | set(keys_file2))
    keys_file3.sort()
    for key in keys_file3:
        if key in keys_file1 and key in keys_file2:
            if file1[key] != file2[key]:
                result += f'  - {key}: {file1[key]}\n'
                result += f'  + {key}: {file2[key]}\n'
            else:
                result += f'    {key}: {file1[key]}\n'
        elif key not in keys_file2:
            result += f'  - {key}: {file1[key]}\n'
        else:
            result += f'  + {key}: {file2[key]}\n'
    template = f"{{\n{result}}}"
    return template


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()

    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))

    print(generate_diff(file1, file2))
