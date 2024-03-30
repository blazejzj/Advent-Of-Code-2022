from collections import defaultdict

data = open("puz8_input.txt").read().strip()
lines = [x for x in data.split('\n')]
grid = []
for line in lines:
    grid.append(line)
directions = [(-1,0),(0,1),(1,0),(0,-1)]
num_rows = len(grid)
num_columns = len(grid[0])
num_visible_spots = 0
for row in range(num_rows):
    for col in range(num_columns):
        is_visible = False
        for (dr,dc) in directions:
            r = row
            c = col
            is_direction_valid = True
            while True:
                r += dr
                c += dc
                if not (0<=r<num_rows and 0<=c<num_columns):
                    break
                if grid[r][c] >= grid[row][col]:
                    is_direction_valid = False
            if is_direction_valid:
                is_visible = True
        if is_visible:
            num_visible_spots += 1
print(num_visible_spots)