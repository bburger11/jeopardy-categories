#!/usr/bin/env bash

cat data/all_data.qa-cat | head -n 1600 > small_data/train
cat data/all_data.qa-cat | head -n 1800 | tail -n 201 > small_data/dev
cat data/test.qa | head -n 200 > small_data/test.qa
cat data/test.cat | head -n 200 > small_data/test.cat

cat data/all_data.qa-cat | head -n 3200 > medium_data/train
cat data/all_data.qa-cat | head -n 3600 | tail -n 401 > medium_data/dev
cat data/test.qa | head -n 400 > medium_data/test.qa
cat data/test.cat | head -n 400 > medium_data/test.cat