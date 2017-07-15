from pathlib import Path
import numpy as np

langs = ["French", "German"]
directory = Path("C:/Users/eeast/documents/visual studio 2017/Projects/LanguageList")
#filepath = directory / "French.txt"

def binom(n, m):
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n + 1):
        b[i] = 1
        j = i - 1
        while j > 0:
            b[j] += b[j - 1]
            j -= 1
    return b[m]

def eratosthenes(n):
    n = (n + 1) >> 1
    i, j, p = 1, 3, np.ones(n, dtype=np.int8)
    
    while i < n:
        if p[i]:
            p[j * j >> 1::j] = 0
        i, j = i + 1, j + 2
    return p.sum()

for i in langs:
    filepath = directory / (i + ".txt")
    if filepath.exists():
        print("File found")

        fd = open(filepath, "r")
        fList = fd.readlines()
        print(fList[2])
    else: 
        print("File not found")

winpct = .6
for numwins in range(1, 20):
    sum = 0
    for i in range(numwins):
        sum += binom(numwins + i - 1, i) * pow(winpct, numwins) * pow(1 - winpct, i)
    print(numwins, sum * (1000 - 10 * numwins))
# Best 13 of 25; $736,222

print(eratosthenes(500000))