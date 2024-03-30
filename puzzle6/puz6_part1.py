"""
1. Read file line by line
2. Strip the line (removes newline)
3. Make a FOR loop and enumerate the collection(give index) in variable (line) starting at index and save as ( i )
"""

with open("puz6_input.txt") as file:
    for line in file:
        line = line.strip("\n")

        for i, character in enumerate(line): 
            unique_set = set(line[i:i+14]) 
            if len(unique_set) == 14:
                print(f"result = {i+14}")
                break