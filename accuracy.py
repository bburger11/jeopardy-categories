import sys

lines1 = [' '.join(line.split()) for line in open(sys.argv[1])]
lines2 = [' '.join(line.split()) for line in open(sys.argv[2])]

if len(lines1) != len(lines2):
    raise ValueError()

def common_data(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True 
    return False

total = correct = partial = combined = 0
for line1, line2 in zip(lines1, lines2):
    total += 1
    if line1 == line2:
        correct += 1
        combined += 1
        #print(f"{line1} and {line2}")

    
    elif common_data(line1.split(), line2.split()):
        partial += 1
        combined += 1
        #print(f"{line1} and {line2}")


print(f"Precisely Correct: {correct}")
print(f"Partially Correct: {partial}")
print(f"Total Correct:     {combined}")
print("---")
print(f"Precise Accuracy:  {correct/total}")
print(f"Partial Accuracy:  {partial/total}")
print(f"Combined Accuracy: {combined/total}")