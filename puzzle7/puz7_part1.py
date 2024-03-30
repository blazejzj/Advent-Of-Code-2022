from collections import defaultdict

dictionary = defaultdict(int)
paths = []

with open("puz7_input.txt") as file:
    for line in file:
        words = line.strip().split()
        if words[1] == "cd":
            if words[2] == "..":
                paths.pop()
            else:
                paths.append(words[2])
        elif words[0].isnumeric():
            for i in range(1, len(paths)+1):                                 # for current_path in paths:
                dictionary['/'.join(paths[:i])] += int(words[0])             # dictionary[current_path] += int(words[0]) 
sums = list(x for x in dictionary.values() if x <= 100000)
result = sum(sums)
print(result) #