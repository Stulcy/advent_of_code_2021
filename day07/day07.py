crabship_positions = [int(position) for position in open(
    'day07/day07.txt').readline().split(',')]


def get_best_position(normal_consumption):
    min_fuel_consumption = float('inf')
    curr_best_position_fuel_consumption = 0
    curr_best_position = 0
    for possible in range(max(crabship_positions) + 1):
        fuel_spent = 0
        for crabship_position in crabship_positions:
            fuel_spent += abs(possible - crabship_position) if normal_consumption else sum(
                range(abs(possible - crabship_position) + 1))
        if fuel_spent < min_fuel_consumption:
            min_fuel_consumption = fuel_spent
            curr_best_position_fuel_consumption = fuel_spent
            curr_best_position = possible
    print(curr_best_position)
    print(curr_best_position_fuel_consumption)


get_best_position(True)
get_best_position(False)
