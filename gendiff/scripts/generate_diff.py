#!/usr/bin/env python

import argparse
import json
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()

    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))

    print(generate_diff(file1, file2))
