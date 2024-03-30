
with open('puz1_input.txt', 'r') as file:

    summarized = []
    current_sum = 0

    for line in file:
        if line != "\n":
            num1 = int(line)
            current_sum = current_sum + num1
        else:
            summarized.append(current_sum)
            current_sum = 0

    if current_sum != 0:
        summarized.append(current_sum)
        
sorted = sorted(summarized)
print(sorted)
print(sorted[-3:])
top_three_sum = sum(sorted[-3:])
print(top_three_sum)
