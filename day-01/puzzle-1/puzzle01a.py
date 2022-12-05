import sys
import readline

filename = sys.argv[1]
fd = open(filename, "r")
maxSum = 0
curSum = 0
while True:
    line = fd.readline()
    if not line:
        break
    try:
        value = int(line)
        curSum += value
    except:
        maxSum = max(maxSum, curSum)
        curSum = 0
fd.close()

print("Max:", max(maxSum, curSum))
