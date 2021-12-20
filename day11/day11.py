data = [[int(i) for i in x] for x in [line.strip('\n')
        for line in open('day11/day11.txt')]]


def flash_it(i, j):
    need_to_flash = []
    for i, j in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
                 (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
        if 0 <= i < len(data) and 0 <= j < len(data[0]):
            data[i][j] += 1
            if data[i][j] == 10:
                need_to_flash.append((i, j))
    return need_to_flash


step = 0
result = 0
while 1:
    flashing_this_round = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
            if data[i][j] == 10:
                flashing_this_round.append((i, j))
    for (i, j) in flashing_this_round:
        flashing_this_round += flash_it(i, j)
    for i, j in flashing_this_round:
        data[i][j] = 0

    result += len(flashing_this_round)
    step += 1
    if step == 100:
        print(result)
    if len(flashing_this_round) == 100:
        print(step)
        break
