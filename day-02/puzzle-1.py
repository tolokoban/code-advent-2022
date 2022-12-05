import sys

scores = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
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
    print(line, ">", score)

print()
print("Total:", total)
