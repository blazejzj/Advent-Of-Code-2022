# read from file line by line
# for each line, split the line in the middle,
# get the 2 parts of the line and see what character is common between them
# the character that is common in those 2 parts, needs to be converted to a value (we need to retrieve its priority)
# add the value of that character to the sum variable, and at the end print the sum

def get_character_value(character: str) -> int:
    character_int_value = ord(character)
    if character_int_value >= ord("a") and character_int_value <= ord("z"):
        return (character_int_value - ord("a")) + 1
    else:
        return (character_int_value - ord("A")) + 26 + 1

sum = 0

with open("../puzzle_input.txt") as file:
    #loop through file line by line
    for line in file:
        #print(line, end="")

        line = line.strip()
        line_length = len(line)
        line_length_middle = line_length // 2
        first_compartment_items = line[:line_length_middle]
        second_compartment_items = line[line_length_middle:line_length]

        #print(f"first_compartment_items = {first_compartment_items}, last_compartment_items = {second_compartment_items}")

        found = False
        for character_first_compartment_items in first_compartment_items:
            for character_second_compartment_items in second_compartment_items:
                if character_first_compartment_items == character_second_compartment_items:
                    character_value = get_character_value(character_first_compartment_items)
                    print(f"char = {character_first_compartment_items}, character_value = {character_value}")
                    sum += character_value
                    found = True
                    break
            if found:
                break

print()
print(f"sum = {sum}")