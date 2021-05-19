# jeopardy-categories

## Preprocessing

In order to create the data to be used in this project, I created the script `preprocess.py`. This reformats the data from J! Archive into a more reasonable format for my system. This transforms `rawdata/jeopardy.json` into `rawdata/processed.json`.

## Baseline

The baseline category prediction is the most naive, simply predicting the category to be the most common word among the questions and answers. The script, `baseline.py` performs this prediction. I ran `python3 baseline.py` which converts the test file at `./data/test.qa` to categories and produces its output file at `./outputs/baseline.output`. In order to check the accuracy of the predicitions, I have a script, `accuracy.py` that will check for precisely and partially correct category names. 

Full command: `python3 baseline.py`.

I then checked the accuracy, `python3 accuracy.py data/test.cat outputs/baseline.output`:

WITHOUT STOPWORDS
```
Precisely Correct: 87
Partially Correct: 420
Total Correct:     507
---
Precise Accuracy:  0.018451749734888653
Partial Accuracy:  0.08907741251325557
Combined Accuracy: 0.10752916224814422
```

WITH STOPWORDS:
```
Precisely Correct: 87
Partially Correct: 420
Total Correct:     507
---
Precise Accuracy:  0.018451749734888653
Partial Accuracy:  0.08907741251325557
Combined Accuracy: 0.10752916224814422
```

This method could only get about 1.8% of the categories precisely correct. I expected this since this approach is very simple and does not even allow the possibility of two word categories. It did acheive some partial accuracy. An example of this may be guessing "Dickens" when the category was "Charles Dickens". Overall, the combined accuracy of the baseline model was 10.75%.

## Rules Based

An improvement on the naive approach may be to keep track of which words are associated with which categories using a set of training data. Then, when we look at the testing data, we choose the category with which it aligns the most. This is the objective of `rules_based.py`, which I trained using `./data/train.qa-cat` and tested on `./data/test.qa`, producing `./outputs/rules.output`. 

Full command: `python3 rules_based.py --train data/train.qa-cat --test data/test.qa -o outputs/rules.output`.

I then checked the accuracy, `python3 accuracy.py data/test.cat outputs/rules.output`:

WITHOUT STOPWORDS:
```
Precisely Correct: 249
Partially Correct: 366
Total Correct:     615
---
Precise Accuracy:  0.0528101802757158
Partial Accuracy:  0.07762460233297985
Combined Accuracy: 0.13043478260869565
```

WITH STOPWORDS:
```
Precisely Correct: 249
Partially Correct: 393
Total Correct:     642
---
Precise Accuracy:  0.0528101802757158
Partial Accuracy:  0.08335100742311771
Combined Accuracy: 0.1361611876988335
```

This method was able to get more categories precisely correct than the baseline and achieved a combined accuracy of 12.96%. This method suffers, however, because it is unable to predict a category that it has not seen in the training data.

## RNN Model

For the RNN, I used a machine translation model with copy functionality. In order to speed up training time, I used a subset of the data. In order to create the subsets, run the script, `make_small.sh`, which will create two directories with 200 and 400 test entries in `small_data/` and `medium_data` respectively. The generated train set is 8x the size of the test entries (1600 and 3200 respectively). And the number of dev entries is the same as the number of test entries for each.

I trained my model on the `small_data` for testing purposes and determined the results for the model using the `medium_data`.

Full command: `python3 neural.py --train medium_data/train --dev medium_data/dev --save model`.

Generating translations for medium data: `python3 neural.py --load model --outfile outputs/rnn.output medium_data/test.qa`.

Finally, checking the accuracy, `python3 accuracy.py medium_data/test.cat outputs/rnn.output`:

WITHOUT STOPWORDS:
```
Precisely Correct: 3
Partially Correct: 19
Total Correct:     22
---
Precise Accuracy:  0.0075
Partial Accuracy:  0.0475
Combined Accuracy: 0.055
```

WITH STOPWORDS:
```
Precisely Correct: 3
Partially Correct: 52
Total Correct:     55
---
Precise Accuracy:  0.0075
Partial Accuracy:  0.13
Combined Accuracy: 0.1375
```