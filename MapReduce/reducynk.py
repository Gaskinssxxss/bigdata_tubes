import sys

words = None
total = 0

for line in sys.stdin:
    word, count = line.strip().split("\t")
    count = int(count)

    if word == words:
        total += count
    else:
        if words:
            print(f"{words}\t{total}")
        words = word
        total = count

if words == word:
    print(f"{words}\t{total}")
