fish_dictionary = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

for days in open('day06/day06.txt').readline().split(','):
    fish_dictionary[int(days)] += 1


def next_day():
    birth_givers = fish_dictionary[0]
    for age in fish_dictionary:
        if age != 8:
            fish_dictionary[age] = fish_dictionary[age + 1]
        else:
            fish_dictionary[age] = 0
    fish_dictionary[6] += birth_givers
    fish_dictionary[8] += birth_givers


# for part one change from 256 to 80
for i in range(256):
    next_day()

num_of_fish = 0
for age in fish_dictionary:
    num_of_fish += fish_dictionary[age]

print(num_of_fish)
