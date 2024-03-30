"""
part2
difference between this and part1 is that instead of popping from the stack to another stack,
we need to have a stack "in between", which will reverse the order of the pushed elements, preserving their order that they had in the original stack
"""

buffer_crates = [] # a list containing all the lines until the first blank line
buffer_crates_data = True # flag to determine if we should still buffer data or not

buffer_instructions = [] # a list containing all the lines after the first blank line (the instructions)

with open("puz5_part1_input.txt") as file: # open file
    for line in file: #loop through file line by line
        line = line.strip("\n") # remove trailing '\n' characters only

        if(len(line) == 0): # blank line
            buffer_crates_data = False # stop buffering data

        if buffer_crates_data: # should we still buffer
            buffer_crates.append(line) # add to buffer
        else:
            buffered_instruction = []
            line_parts = line.split(' ') # split the line on spaces
            for line_part in line_parts:
                if line_part.isnumeric():
                    buffered_instruction.append(int(line_part))
            if(len(buffered_instruction) != 0):
                buffer_instructions.append(buffered_instruction)

buffer_crates.reverse() # reverse the buffer of crates
first_buffer_crates_line: str = buffer_crates[0]

stack_character_position_line = [] # a list of at what position to read a char into the correct stack

counter_characters = 0
number_of_stacks_needed = 0
for char in first_buffer_crates_line:
    counter_characters += 1 #increment by 1 for each char
    if char.isnumeric(): # if this is a number
        number_of_stacks_needed = int(char)
        stack_character_position_line.append(counter_characters)

stacks = []
for i in range(0, number_of_stacks_needed, 1):
    stacks.append([])

for line in buffer_crates[1:]: # loop through buffer of crates, skipping the first line
    if(len(line.strip()) == 0): #check if there is nothing to read at this line
        continue

    for i, position_to_read_at in enumerate(stack_character_position_line): # loop through each position we need to read at on the line, we enumerate to know which stack we are supposed to insert the character into
        if(len(line) >= position_to_read_at): #not all lines are the same, we need to check if we can read so far into the line
            if not line[position_to_read_at-1].isspace(): # check if this is a whitespace char, if it is then dont read
                stacks[i].append(line[position_to_read_at-1])

for buffered_instruction in buffer_instructions:
    stack_pop_buffer = [] # a buffer that we push the popped elements onto and then loop through and push onto the target stack
    for i in range(0, buffered_instruction[0], 1): # loop from 0 to how many times we should be popping
        if(len(stacks[buffered_instruction[1] - 1]) != 0): # if the actually has something
            stack_pop_buffer.append(stacks[buffered_instruction[1] - 1].pop())

    for i in range(0, len(stack_pop_buffer), 1):
        stacks[buffered_instruction[2] - 1].append(stack_pop_buffer.pop()) #we need to do -1 here cause stacks indexes start from 0

for stack in stacks: # loop through each stack and pop it
    if(len(stack) != 0): #check if the stack actually has something
        print(stack.pop(), end="")

print()