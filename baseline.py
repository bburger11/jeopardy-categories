#!/usr/bin/env python3

import re
from collections import Counter

def parse_line(string):
    cleanr = re.compile('<question>')
    cleantext = re.sub(cleanr, ' ', string)
    cleanr = re.compile('<answer>')
    cleantext = re.sub(cleanr, ' ', cleantext)
    return cleantext

def count_most(string):
    str_list = string.split(" ")
    words = [word for word in str_list if len(word) > 4]
    counter = Counter(words)
    if words:
        most_common = counter.most_common(1)[0][0]
    else:
        return ""
    return most_common

if __name__ == '__main__':
    f = open("data/test.qa", "r")
    out = open("outputs/baseline.output", "a")
    lines = f.readlines()
    for line in lines:
        cleanline = parse_line(line)
        most_common = count_most(cleanline)
        to_write = most_common + "\n"
        out.write(to_write)
        
