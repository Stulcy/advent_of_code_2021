data = [line.strip('\n') for line in open('day10/day10.txt').readlines()]

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

error_count = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}

error_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def remove_corrupted(line):
    looking_for = []
    for bracket in line:
        if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
            looking_for.append(pairs[bracket])
        else:
            if bracket == looking_for[-1]:
                looking_for.pop()
            else:
                error_count[bracket] += 1
                return False
    return True


clean_data = []
for line in data:
    if remove_corrupted(line):
        clean_data.append(line)

print(error_count[')'] * 3 + error_count[']'] * 57 +
      error_count['}'] * 1197 + error_count['>'] * 25137)


def solve_incomplete(line):
    looking_for = []
    result = 0
    for bracket in line:
        if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
            looking_for.append(pairs[bracket])
        else:
            if bracket == looking_for[-1]:
                looking_for.pop()
    for bracket in looking_for[::-1]:
        result = result * 5 + error_points[bracket]
    return result


autocomplete_error_scores = []
for line in clean_data:
    autocomplete_error_scores.append(solve_incomplete(line))

print(sorted(autocomplete_error_scores)[int(
      (len(autocomplete_error_scores) + 1) / 2) - 1])
