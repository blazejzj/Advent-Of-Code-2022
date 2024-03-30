
# Open the file in reading mode

import heapq

with open('puz1_input.txt', 'r') as file:

    summarized = []
    current_sum = 0

    for line in file:
        #print(line, end="") #end removes newline

        if not line.isspace():
            num1 = int(line)
            current_sum = current_sum + num1
        else:
            summarized.append(current_sum)
            current_sum = 0

    summarized.append(current_sum)
    #print(summarized)

    result = max(summarized)
    #print(result)

    h_values = heapq.nlargest(3, summarized)
    sum_num = sum(h_values)
    print(sum_num)

    l_values = heapq.nsmallest(3, summarized)
    sum1_num1 = sum(l_values)
    #print(sum1_num1)


    #SORT, TAKE OUT 3 LARGEST, SUM, PRINT
    sortme = sorted(summarized, reverse=True)
    first = sortme[0]
    second = sortme[1]
    third = sortme[2]

    result5 = first + second + third
    print(result5)








    























