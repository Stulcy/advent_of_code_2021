floor_map = [line for line in [read_line.strip('\n')
             for read_line in open('day09/day09.txt').readlines()]]
width = len(floor_map[0])
height = len(floor_map)

sum_of_risk_levels = 0
lowest_points = []


for i in range(height):
    for j in range(width):
        # top left
        if i == 0 and j == 0:
            if floor_map[i+1][j] > floor_map[i][j] and floor_map[i][j+1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # top right
        elif i == 0 and j == width - 1:
            if floor_map[i+1][j] > floor_map[i][j] and floor_map[i][j - 1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # bottom left
        elif i == height - 1 and j == 0:
            if floor_map[i-1][j] > floor_map[i][j] and floor_map[i][j+1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # bottom right
        elif i == height - 1 and j == width - 1:
            if floor_map[i-1][j] > floor_map[i][j] and floor_map[i][j-1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # top line
        elif i == 0 and 0 < j < width - 1:
            if floor_map[i][j-1] > floor_map[i][j] and floor_map[i][j+1] > floor_map[i][j] and floor_map[i+1][j] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # bottom line
        elif i == height - 1 and 0 < j < width - 1:
            if floor_map[i][j-1] > floor_map[i][j] and floor_map[i][j+1] > floor_map[i][j] and floor_map[i-1][j] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # left line
        elif 0 < i < height - 1 and j == 0:
            if floor_map[i-1][j] > floor_map[i][j] and floor_map[i+1][j] > floor_map[i][j] and floor_map[i][j+1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # right line
        elif 0 < i < height - 1 and j == width - 1:
            if floor_map[i-1][j] > floor_map[i][j] and floor_map[i+1][j] > floor_map[i][j] and floor_map[i][j-1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))
        # middle part
        else:
            if floor_map[i-1][j] > floor_map[i][j] and floor_map[i+1][j] > floor_map[i][j] and floor_map[i][j-1] > floor_map[i][j] and floor_map[i][j+1] > floor_map[i][j]:
                sum_of_risk_levels += int(floor_map[i][j]) + 1
                lowest_points.append((i, j))

print(sum_of_risk_levels)

needs_to_check = []


def get_basin(i, j):
    already_visited = []
    needs_to_check.append((i, j))
    while len(needs_to_check) > 0:
        point = needs_to_check.pop()
        i = point[0]
        j = point[1]
        if (i, j) not in already_visited:
            # top left
            if i == 0 and j == 0:
                if floor_map[i+1][j] != '9' and (i+1, j) not in already_visited:
                    needs_to_check.append((i+1, j))
                if floor_map[i][j+1] != '9' and (i, j+1) not in already_visited:
                    needs_to_check.append((i, j+1))
            # top right
            elif i == 0 and j == width - 1:
                if floor_map[i+1][j] != '9' and (i+1, j) not in already_visited:
                    needs_to_check.append((i+1, j))
                if floor_map[i][j - 1] != '9' and (i, j-1) not in already_visited:
                    needs_to_check.append((i, j-1))
            # bottom left
            elif i == height - 1 and j == 0:
                if floor_map[i-1][j] != '9' and (i-1, j) not in already_visited:
                    needs_to_check.append((i-1, j))
                if floor_map[i][j+1] != '9' and (i, j+1) not in already_visited:
                    needs_to_check.append((i, j+1))
            # bottom right
            elif i == height - 1 and j == width - 1:
                if floor_map[i-1][j] != '9' and (i-1, j) not in already_visited:
                    needs_to_check.append((i-1, j))
                if floor_map[i][j-1] != '9' and (i, j-1) not in already_visited:
                    needs_to_check.append((i, j-1))
            # top line
            elif i == 0 and 0 < j < width - 1:
                if floor_map[i][j-1] != '9' and (i, j-1) not in already_visited:
                    needs_to_check.append((i, j-1))
                if floor_map[i][j+1] != '9' and (i, j+1) not in already_visited:
                    needs_to_check.append((i, j+1))
                if floor_map[i+1][j] != '9' and (i+1, j) not in already_visited:
                    needs_to_check.append((i+1, j))
            # bottom line
            elif i == height - 1 and 0 < j < width - 1:
                if floor_map[i][j-1] != '9' and (i, j-1) not in already_visited:
                    needs_to_check.append((i, j-1))
                if floor_map[i][j+1] != '9' and (i, j+1) not in already_visited:
                    needs_to_check.append((i, j+1))
                if floor_map[i-1][j] != '9' and (i-1, j) not in already_visited:
                    needs_to_check.append((i-1, j))
            # left line
            elif 0 < i < height - 1 and j == 0:
                if floor_map[i-1][j] != '9' and (i-1, j) not in already_visited:
                    needs_to_check.append((i-1, j))
                if floor_map[i+1][j] != '9' and (i+1, j) not in already_visited:
                    needs_to_check.append((i+1, j))
                if floor_map[i][j+1] != '9' and (i, j+1) not in already_visited:
                    needs_to_check.append((i, j+1))
            # right line
            elif 0 < i < height - 1 and j == width - 1:
                if floor_map[i-1][j] != '9' and (i-1, j) not in already_visited:
                    needs_to_check.append((i-1, j))
                if floor_map[i+1][j] != '9' and (i+1, j) not in already_visited:
                    needs_to_check.append((i+1, j))
                if floor_map[i][j-1] != '9' and (i, j-1) not in already_visited:
                    needs_to_check.append((i, j-1))
            # middle part
            else:
                if floor_map[i-1][j] != '9' and (i-1, j) not in already_visited:
                    needs_to_check.append((i-1, j))
                if floor_map[i+1][j] != '9' and (i+1, j) not in already_visited:
                    needs_to_check.append((i+1, j))
                if floor_map[i][j-1] != '9' and (i, j-1) not in already_visited:
                    needs_to_check.append((i, j-1))
                if floor_map[i][j+1] != '9' and (i, j+1) not in already_visited:
                    needs_to_check.append((i, j+1))
        if point not in already_visited:
            already_visited.append(point)
    return already_visited


basins = []

for point in lowest_points:
    basins.append(get_basin(point[0], point[1]))

final_result = 1

for i in range(3):
    max_basin = basins[0]
    for basin in basins:
        if len(basin) > len(max_basin):
            max_basin = basin
    basins.remove(max_basin)
    final_result *= len(max_basin)

print(final_result)
