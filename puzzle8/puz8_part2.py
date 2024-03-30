from collections import defaultdict

data = open("puz8_input.txt").read().strip()
lines = [x for x in data.split('\n')]
grid = []

for line in lines:
    grid.append(line)
directions = [(-1,0),(0,1),(1,0),(0,-1)] # Defining directions 
num_rows = len(grid) #counting how many rows there is in the grid
num_columns = len(grid[0]) # counting how many colums there is in the grid 
max_score = 0
for row in range(num_rows):
    for col in range(num_columns):
        score = 1
        for (dr,dc) in directions:  # looping through every direction
            distance = 1
            rr = row+dr
            cc= col+dc
            while True:  # caluclating the distance tto the next higher spot in this direction
                if not (0<=rr<num_rows and 0<=cc<num_columns):
                    distance -= 1
                    break
                if grid[rr][cc] >= grid[row][col]:
                    break
                distance += 1
                rr += dr
                cc += dc
            score *= distance # updating the score for this spot 
            max_score = max(max_score, score)   # updating the max score
print(max_score) # printing the score