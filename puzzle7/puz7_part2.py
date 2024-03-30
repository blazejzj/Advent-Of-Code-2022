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

unused_space = 70000000 - dictionary["/"]
needed_space = 30000000 - unused_space
candidates_for_deletion = list(x for x in dictionary.values() if x >= needed_space)
result = min(candidates_for_deletion)
print(result)