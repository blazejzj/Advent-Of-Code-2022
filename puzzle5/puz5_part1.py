"""
part1
thoughts:
have to utalize a stack datastructure, a list of them (list of stacks)
NB! in python a list is a stack, where pushing onto the stack is the same as list.Append() and popping of the stack is list.pop()

implementation idea:
1.open file

2.read line by line until first blank line enountered, storing lines in a list (buffer of crates)

3.after blank line, read lines into another buffer (buffer of instructions)
here we need to only read the numbers and put them into a list
so for example in the example we have this
move 1 from 2 to 1
when we read into the buffer, we only temporarily add 1 2 and 1, and then add that list to the buffer of instructions

4.close file

5.reverse the crate buffer, as we want to know how many stacks we need and will simply reading, we can push onto stack directly
will look like so
 1   2   3
[Z] [M] [P]
[N] [C]
    [D]

6. loop through the first line in the crate buffer, to see at which character position on a given line we are supposed to assign the crate characters on
at the same time, convert each number to int and store it in the same variable, in the end we will this way know how many stacks we need
in the example we need 3, in puzzle input we need 9

7. create the list of stack

8. loop through the buffer of crates, not including the first line, and create/store the character at the corresponding position into the correct stack
check for line length while reading, as now all lines are of the same length
dont add whitespace characters into stacks

9. loop through buffer of instructions
the format of the instructions is the following
"move X", is how many times we need to pop from the stack
"from Y", is which stack we should be popping from
"to Z", is which stack we should be pushing onto (appending in python)

for us since we have the buffer of instructions
the first number is how many times we need to pop from the stack
second number is which stack we should be popping from
third number is which stack we should be pushing onto

"""

buffer_crates = [] # a list containing all the lines until the first blank line
buffer_crates_data = True # flag to determine if we should still buffer data or not

buffer_instructions = [] # a list containing all the lines after the first blank line (the instructions)

with open("puz5_input.txt") as file: # open file
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
    for i in range(0, buffered_instruction[0], 1): # loop from 0 to how many times we should be popping
        if(len(stacks[buffered_instruction[1] - 1]) != 0): # if the actually has something
            stacks[buffered_instruction[2] - 1].append(stacks[buffered_instruction[1] - 1].pop()) #we need to do -1 here cause stacks indexes start from 0

for stack in stacks: # loop through each stack and pop it
    if(len(stack) != 0): #check if the stack actually has something
        print(stack.pop(), end="")

print()