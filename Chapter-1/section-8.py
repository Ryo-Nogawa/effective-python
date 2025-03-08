names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]
print(counts)


print("###############")


longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)


print("###############")


for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)


print("###############")


for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

names.append("Rosalind")
for name, count in zip(names, counts):
    print(name)


print("###############")

import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f"{name}: {count}")
