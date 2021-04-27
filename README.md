# jeopardy-categories

## Baseline

The baseline category prediction is the most naive, simply predicting the category to be the most common word among the questions and answers. The script, `baseline.py` performs this prediction. I ran `python3 baseline.py` which converts the test file at `./data/test.qa` to categories and produces its output file at `./outputs/baseline.output`. In order to check the accuracy of the predicitions, I have a script, `accuracy.py` that will check for precisely and partially correct category names. The output from `python3 accuracy.py data/test.cat outputs/baseline.output` can be seen below:

```
Precisely Correct: 81
Partially Correct: 385
Total Correct:     466
---
Precise Accuracy:  0.017179215270413575
Partial Accuracy:  0.0816542948038176
Combined Accuracy: 0.09883351007423118
```

This method could only get about 1.7% of the categories precisely correct. I expected this since this approach is very simple and does not even allow the possibility of two word categories. It did acheive some partial accuracy. An example of this may be guessing "Dickens" when the category was "Charles Dickens". Overall, the combined accuracy of the baseline model was 9.88%.

## Rules Based

An improvement on the naive approach may be to keep track of which words are associated with which categories using a set of training data. Then, when we look at the testing data, we choose the category with which it aligns the most. This is the objective of `rules_based.py`, which I trained using `./data/train.qa-cat` and tested on `./data/test.qa`, producing `./outputs/rules.output`. I checked the accuracy, `python3 accuracy.py data/test.cat outputs/rules.output`:

```
Precisely Correct: 250
Partially Correct: 361
Total Correct:     611
---
Precise Accuracy:  0.053022269353128315
Partial Accuracy:  0.07656415694591728
Combined Accuracy: 0.1295864262990456
```

This method was able to get more categories precisely correct than the baseline and achieved a combined accuracy of 12.96%. This method suffers, however, because it is unable to predict a category that it has not seen in the training data.