    
result = 0

#with open('puz3_example_input.txt') as file:

with open('puz3_input.txt') as file:
    for line in file:
        #print(line, end="")
        line = line.strip()
        line_length = len(line)
        line_length_middle = line_length // 2
        first_compartment = line[:line_length_middle]
        second_compartment = line[line_length_middle :line_length]

        common_characters = set(first_compartment) & set(second_compartment)
        num_common_characters = len(common_characters)
        print(common_characters)

        dictionary_small_case = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26,
        }
        dictionary_capital_case = {
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
        }

    
        common_characters = set(first_compartment) & set(second_compartment)
        num_common_characters = len(common_characters)
        if num_common_characters == 0:
            continue
        #print(common_characters)
        
        first_common_character = common_characters.pop()
        print(first_common_character)
        first_common_character_value = 0
        if first_common_character.isupper():
            first_common_character_value = dictionary_capital_case[first_common_character]
        else:
            first_common_character_value = dictionary_small_case[first_common_character]
        
        result = result + first_common_character_value
        print(result)





        #######################OPTIMIZED CODE#######################

    result = 0

# Open the input file and loop through each line of the file.
with open('puz3.part1.input.txt') as file:
    for line in file:
        # Strip any whitespace from the line and calculate the length
        # of the line.
        line = line.strip()
        line_length = len(line)

        # Calculate the middle of the line, which is where we will
        # split the line into two compartments.
        line_length_middle = line_length // 2

        # Split the line into two compartments.
        first_compartment = line[:line_length_middle]
        second_compartment = line[line_length_middle:line_length]

        # Use sets to find the common characters in the two compartments.
        common_characters = set(first_compartment) & set(second_compartment)

        # If there are no common characters, skip this line.
        if not common_characters:
            continue

        # Get the first common character and calculate its value using
        # the dictionaries for small and capital case letters.
        first_common_character = common_characters.pop()
        first_common_character_value = 0
        if first_common_character.islower():
            dictionary = {
                "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
            }
            first_common_character_value = dictionary[first_common_character]
        else:
            dictionary = {
                "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33,
                "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
                "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47,
                "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52,
            }
            first_common_character_value = dictionary[first_common_character]

        # Add the value of the first common character to the result.
        result += first_common_character_value

# Print the result.
print(f"result = {result}")



    

        