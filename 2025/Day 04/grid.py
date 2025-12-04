total = 0

with open("input.txt") as file:
    grid = [list(line.strip()) for line in file]

    while True:
        is_removed = False
        pos = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@":
                    count = 0
                    temp_pos = []
                    if i-1 >= 0 and grid[i-1][j] == "@":
                        count += 1
                    if i+1 < len(grid) and grid[i+1][j] == "@":
                        count += 1
                    if j-1 >= 0 and grid[i][j-1] == "@":
                        count += 1
                    if (j+1) < len(grid[i]) and  grid[i][j+1] == "@":
                        count += 1
                    if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == "@":
                        count += 1
                    if i-1 >= 0 and j+1 < len(grid[i-1]) and grid[i-1][j+1] == "@":
                        count += 1
                    if i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == "@":
                        count += 1
                    if i+1 < len(grid) and j+1 < len(grid[i+1]) and grid[i+1][j+1] == "@":
                        count += 1
                    if count < 4:
                        total += 1
                        pos.append((i, j))
                        
                
        for p in pos:
            grid[p[0]][p[1]] = "."

        if pos == []:
            for row in grid:
                print("".join(row))
            break

print(f"Total positions with fewer than 4 adjacent '@': {total}")
