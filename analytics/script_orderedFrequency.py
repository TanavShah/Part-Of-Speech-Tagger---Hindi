import csv
from collections import Counter

d1 = dict()
d2 = dict()

with open('token-tag_pairs_cleaned.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        if row[1] in d2:
            d2[row[1]] = d2[row[1]] + 1
        elif row[1] not in d2:
            d2[row[1]] = 1
        if row[0] in d1:
            d1[row[0]] = d1[row[0]] + 1
        elif row[0] not in d1:
            d1[row[0]] = 1

k1 = Counter(d1)
h1 = k1.most_common(10)

with open('topWords', 'w') as f2:
    for i in h1:
        f2.write('%s:%s\n' % (i[0], i[1]))
k2 = Counter(d2)
h2 = k2.most_common(10)

with open('topTags', 'w') as f3:
    for j in h2:
        f3.write('%s:%s\n' % (j[0], j[1]))
