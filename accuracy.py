import sys
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

lines1 = [' '.join(line.split()) for line in open(sys.argv[1])]
lines2 = [' '.join(line.split()) for line in open(sys.argv[2])]

if len(lines1) != len(lines2):
    raise ValueError()

def common_data(list1, list2):
    stop_words = set(stopwords.words('english')) 
    for x in list1:
        for y in list2:
            if x.lower() == y.lower() and x not in stop_words and y not in stop_words:
                return True 
    return False

total = correct = partial = combined = 0
for line1, line2 in zip(lines1, lines2):
    total += 1
    if line1.lower() == line2.lower():
        correct += 1
        combined += 1

    
    elif common_data(line1.split(), line2.split()):
        partial += 1
        combined += 1

print(f"Precisely Correct: {correct}")
print(f"Partially Correct: {partial}")
print(f"Total Correct:     {combined}")
print("---")
print(f"Precise Accuracy:  {correct/total}")
print(f"Partial Accuracy:  {partial/total}")
print(f"Combined Accuracy: {combined/total}")