import sys

scores = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}

filename = sys.argv[1]
fd = open(filename, "r")
total = 0
while True:
    line = fd.readline()
    if not line:
        break
    line = line.strip()
    score = scores[line]
    total += score

print()
print("Total:", total)
