import sys

lines1 = [' '.join(line.split()) for line in open(sys.argv[1])]
lines2 = [' '.join(line.split()) for line in open(sys.argv[2])]

if len(lines1) != len(lines2):
    raise ValueError()

total = correct = partial = 0
for line1, line2 in zip(lines1, lines2):
    total += 1
    if line1 == line2:
        correct += 1
        print(f"{line1} and {line2}")
    
    if line2 in line1.split():
        partial += 1
        print(f"{line1} and {line2}")

print(f"Precisely Correct: {correct}")
print(f"Partially Correct: {partial}")
print(f"Total:             {total}")
print("---")
print(f"Precise Accuracy: {correct/total}")
print(f"Partial Accuracy: {partial/total}")