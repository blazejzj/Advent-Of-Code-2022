
dictionary_small_case = {
                "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
        }
dictionary_capital_case = {
                "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33,
                "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
                "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47,
                "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52,
        }


result = 0
line_count = 0
lines = []
with open('puz3_input.txt') as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        line_count += 1
        if line_count % 3 == 0:

            print(len(lines))
            sets = [set(s) for s in lines]
            common_characters = sets[0] & sets[1] & sets[2]
            num_common_characters = len(common_characters)

            if num_common_characters != 0:
                common_character = common_characters.pop()
                common_character_value = 0 

                if common_character.isupper():
                    common_character_value = dictionary_capital_case[common_character]
                else:
                    common_character_value = dictionary_small_case[common_character]
                
                result = result + common_character_value

            lines.clear()

print(result)