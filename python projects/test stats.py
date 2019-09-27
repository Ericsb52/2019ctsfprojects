from collections import Counter
import statistics


counts = Counter(titles)
print(counts)
counts_sorted = sorted(counts.items(), key=lambda x: x[1])
print(counts_sorted)
median = statistics.median(counts)
print(median)
