#!/usr/bin/env python3

import argparse, sys, re
from collections import Counter
import random

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable):
        return iterable

def determine_category(line, model):
    best = {}
    for category in model:
        count = 0
        category_words = model[category].keys()
        for word in line:
            if word in category_words:
                count += model[category][word]
        if count:
            if category not in best:
                best[category] = count
            else:
                best[category] += count
    vals = best.values()
    if not vals:
        return ""
    max_val = max(vals)
    if max_val > 1:
        max_key = max(best, key=best.get)
    else:
        max_key = random.choice(list(best.keys()))

    return max_key

def parse_line(string):
    cleanr = re.compile('<question>')
    cleantext = re.sub(cleanr, ' ', string)
    cleanr = re.compile('<answer>')
    cleantext = re.sub(cleanr, ' ', cleantext)
    return cleantext

def read_parallel(filename):
    """Read data from the file named by 'filename.'
    The file should be in the format:

    我 不 喜 欢 沙 子 \t i do n't like sand
    where \t is a tab character.
    """
    data = []
    for line in open(filename):
        fline, eline = line.split('\t')
        eline = parse_line(eline)
        fwords = fline.split()
        ewords = eline.split()
        data.append((ewords, fwords))
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', type=str, help='training data')
    parser.add_argument('--test', type=str, help='testing data')
    parser.add_argument('-o', '--outfile', type=str, help='write translations to file')
    args = parser.parse_args()

    if args.train and args.test and args.outfile:
        # Read in training data
        traindata = read_parallel(args.train)
        model = {}
        for line in traindata:
            category = " ".join(line[1])
            words = [word for word in line[0]]
            if category not in model:
                model[category] = Counter(words)
            else:
                model[category].update(words)

        # Find the best match for the test data
        f = open(args.test, "r")
        out = open(args.outfile, "a")
        for line in tqdm(f.readlines()):
            cleanr = re.compile('<question>')
            cleantext = re.sub(cleanr, ' ', line)
            cleanr = re.compile('<answer>')
            cleantext = re.sub(cleanr, ' ', cleantext).split()
            category = determine_category(cleantext, model)

            to_write = category + "\n"
            out.write(to_write)
        
        print("Done.")
    else:
        print("Train and test and outfile are required!")
        sys.exit(1)