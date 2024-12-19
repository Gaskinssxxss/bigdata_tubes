import sys
import csv

for line in sys.stdin:
    reader = csv.reader([line])
    try:
        col = next(reader)
        content = col[4]
        words = content.split()
        for word in words:
            print(f"{word.lower()}\t1")
    except Exception as e:
        continue
