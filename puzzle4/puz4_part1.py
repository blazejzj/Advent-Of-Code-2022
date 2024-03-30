


#PART 1

# Define a lambda function that returns a range of integers between its two arguments
irange = lambda a, b: range(a, b + 1)
# Initialize a counter variable to zero
counter = 0
# Open the file 'puz4_part1_input.txt' in read-only mode, and read its contents line by line
with open('puz4_part1_input.txt', 'r') as file:
    for line in file:
        # Split the line on a comma, and assign the two resulting substrings to variables 'a' and 'b'
        a, b = line.strip().split(",")
        # Convert 'a' and 'b' into sets of integers, by splitting each substring on a dash,
        # mapping the resulting substrings to integer values, and passing the resulting tuples to the 'irange' function
        a = set(irange(*map(int, a.split("-"))))
        b = set(irange(*map(int, b.split("-"))))
        # Use the difference operator ('-') to find the elements in 'a' that are not in 'b',
        # and check if the length of the resulting set is zero
        # Also, use the difference operator to find the elements in 'b' that are not in 'a',
        # and check if the length of the resulting set is zero
        if len(a - b) == 0 or len(b - a) == 0:
            # If either of the differences is empty, increment the counter by one
            counter += 1
# After all lines have been processed, print the final value of the counter to the console
print(counter)




#PART 2


# Define a lambda function that returns a range of integers between its two arguments
irange = lambda a, b: range(a, b + 1)
# Initialize a counter variable to zero
counter = 0
# Open the file 'puz4_part1_input.txt' in read-only mode, and read its contents line by line
with open('puz4_input.txt', 'r') as file:
    for line in file:
        # Split the line on a comma, and assign the two resulting substrings to variables 'a' and 'b'
        a, b = line.strip().split(",")
        # Convert 'a' and 'b' into sets of integers, by splitting each substring on a dash,
        # mapping the resulting substrings to integer values, and passing the resulting tuples to the 'irange' function
        a = set(irange(*map(int, a.split("-"))))
        b = set(irange(*map(int, b.split("-"))))
        # Use the intersection operator ('&') to find the common elements between 'a' and 'b',
        # and check if the length of the resulting set is greater than zero
        if len(a & b) > 0:
            # If the length of the intersection is greater than zero, increment the counter by one
            counter += 1
# After all lines have been processed, print the final value of the counter to the console
print(counter)
