report = [str(line.strip('\n')) for line in open('day3/day3.txt').readlines()]

gamma_binary = ''
epsilon_binary = ''

for i in range(len(report[0])):
    temp = ''
    for line in report:
        temp += '1' if line[i] == '1' else '0'
    gamma_binary += '1' if (temp.count('1') > temp.count('0')) else '0'
    epsilon_binary += '0' if (temp.count('1') > temp.count('0')) else '1'

print(int(gamma_binary, 2) * int(epsilon_binary, 2))


def day3_fun(report, oxygen):
    major = ''
    i = -1
    while len(report) > 1:
        i += 1
        temp = ''
        for line in report:
            temp += '1' if line[i] == '1' else '0'
        if oxygen:
            major = '1' if (temp.count('1') >= temp.count('0')) else '0'
        else:
            major = '0' if (temp.count('0') <= temp.count('1')) else '1'
        temp_report = report.copy()
        for line in report:
            if line[i] != major:
                temp_report.remove(line)
        report = temp_report
    return int(report[0], 2)


print(day3_fun(report, True) * day3_fun(report, False))
