# A* for 8 Puzzle (Simple Version)

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Print function
def print_state(s):
    for row in s:
        print(row)
    print()

# Heuristic
def h(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val-1)//3
                y = (val-1)%3
                dist += abs(i-x) + abs(j-y)
    return dist

# Find zero
def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i,j

# A* Algorithm
def astar(start):
    print("Start State:")
    print_state(start)

    print("Goal State:")
    print_state(goal)

    open_list = [(h(start), 0, start)]
    visited = []

    while open_list:
        open_list.sort()
        f, g, curr = open_list.pop(0)

        if curr == goal:
            print("Goal reached!")
            return

        visited.append(curr)

        x, y = find_zero(curr)

        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [row[:] for row in curr]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                if new not in visited:
                    new_g = g + 1
                    new_f = new_g + h(new)
                    open_list.append((new_f, new_g, new))

    print("No solution")

# Start state
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

astar(start)