horizontal = 0
depth = 0

for instruction, direction in (((item.split(' ')) for item in [str(instruction.strip('\n'))
                                                               for instruction in open('day02/day02.txt').readlines()])):
    if instruction == 'up':
        horizontal -= int(direction)
    elif instruction == 'down':
        horizontal += int(direction)
    else:
        depth += int(direction)

print(horizontal * depth)

horizontal = 0
depth = 0
aim = 0

for instruction, direction in (((item.split(' ')) for item in [str(instruction.strip('\n'))
                                                               for instruction in open('day02/day02.txt').readlines()])):
    if instruction == 'up':
        aim -= int(direction)
    elif instruction == 'down':
        aim += int(direction)
    else:
        horizontal += int(direction)
        depth += (int(direction) * aim)

print(horizontal * depth)
