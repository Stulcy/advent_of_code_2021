depths = [int(depth) for depth in open('day1/day1.txt').readlines()]

num = 0
for prev, curr in zip(depths, depths[1:]):
    if curr > prev:
        num += 1
print(num)

num = 0
for i in range(len(depths) - 3):
    if (depths[i + 1] + depths[i + 2] + depths[i + 3]) > (depths[i] + depths[i + 1] + depths[i + 2]):
        num += 1
print(num)
