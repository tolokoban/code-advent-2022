import sys
import readline


def add(cur, sums):
    for i in range(len(sums)):
        val = sums[i]
        if cur > val:
            sums[i] = cur
            cur = val


filename = sys.argv[1]
fd = open(filename, "r")
maxSums = [0, 0, 0]
curSum = 0
while True:
    line = fd.readline()
    if not line:
        break
    try:
        value = int(line)
        curSum += value
    except:
        add(curSum, maxSums)
        curSum = 0
fd.close()

add(curSum, maxSums)
print("Sums:", maxSums)
print("Total:", sum(maxSums))
