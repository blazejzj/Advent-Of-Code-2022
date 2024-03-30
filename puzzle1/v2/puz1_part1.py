

with open('puz1_input.txt', 'r') as file:

    summarized = []
    current_sum = 0

    for line in file:
        if not line.isspace():
            num1 = int(line)
            current_sum = current_sum + num1
        else:
            summarized.append(current_sum)
            current_sum = 0
        
    print(max(summarized))