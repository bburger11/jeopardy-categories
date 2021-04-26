#!/usr/bin/env python3

import random
import time

if __name__ == '__main__':
    f = open("data/all_data.qa-cat", "r")
    lines = f.readlines()

    random.seed()
    random.shuffle(lines)

    # First 80% will be train
    split_1 = int(0.8 * len(lines))
    # Dev (validation) and test (performance) will be 10% each
    split_2 = int(0.9 * len(lines))
    # Split appropriately
    train = lines[:split_1]
    dev = lines[split_1:split_2]
    test = lines[split_2:]

    #print(len(lines))
    with open("data/train.qa-cat", "a") as t:
        for line in train:
            t.write(line)
    
    with open("data/dev.qa-cat", "a") as d:
        for line in dev:
            d.write(line)

    with open("data/test.cat", "a") as tcat:
        with open("data/test.qa", "a") as tqa:
            for line in test:
                category = line.split('\t')[0] + "\n"
                q_and_a = line.split('\t')[1]
                tcat.write(category)
                tqa.write(q_and_a)
