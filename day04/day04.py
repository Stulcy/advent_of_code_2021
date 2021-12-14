f = open('day04/day04.txt', 'r')
numbers_drawn = [num.strip('\n') for num in f.readline().split(
    ',') if num != '\n']
lines = [line.strip('\n').split() for line in f.readlines() if line != '\n']
tables = [lines[i:i + 5] for i in range(0, len(lines), 5)]
dummy_tables = [[['' for i in range(5)] for j in range(5)]
                for k in range(len(tables))]


def checkRows(table):
    for row_index in range(5):
        if table[row_index][0] in numbers_drawn and table[row_index][1] in numbers_drawn and table[row_index][2] in numbers_drawn and table[row_index][3] in numbers_drawn and table[row_index][4] in numbers_drawn:
            return True
    return False


def checkColumns(table):
    for column_index in range(5):
        if table[0][column_index] in numbers_drawn and table[1][column_index] in numbers_drawn and table[2][column_index] in numbers_drawn and table[3][column_index] in numbers_drawn and table[4][column_index] in numbers_drawn:
            return True
    return False


def checkWinCondition(dummy_tables):
    for table in dummy_tables:
        if checkRows(table) or checkColumns(table):
            return True
    return False


def playGame(numbers_drawn, tables, dummy_tables):
    for drawn_number in numbers_drawn:
        for table_index in range(len(tables)):
            for row_index in range(5):
                for column_index in range(5):
                    if drawn_number == tables[table_index][row_index][column_index]:
                        dummy_tables[table_index][row_index][column_index] = drawn_number
                        if checkWinCondition(dummy_tables):
                            return [drawn_number, table_index]


def sumOfUnmarked(table, dummy_table):
    sum = 0
    for row_index in range(5):
        for column_index in range(5):
            if table[row_index][column_index] != dummy_table[row_index][column_index]:
                sum += int(table[row_index][column_index])
    return sum


results = playGame(numbers_drawn, tables, dummy_tables)
print(sumOfUnmarked(tables[results[1]],
                    dummy_tables[results[1]]) * int(results[0]))


# SECOND PART
dummy_tables = [[['' for i in range(5)] for j in range(5)]
                for k in range(len(tables))]

tables_won = []


def playGameSecond(numbers_drawn, tables, dummy_tables):
    for drawn_number in numbers_drawn:
        for table_index in range(len(tables)):
            for row_index in range(5):
                for column_index in range(5):
                    if drawn_number == tables[table_index][row_index][column_index]:
                        dummy_tables[table_index][row_index][column_index] = drawn_number
                        if (checkColumns(dummy_tables[table_index]) or checkRows(dummy_tables[table_index])) and (table_index not in tables_won):
                            tables_won.append(table_index)
                            if len(tables_won) == len(tables):
                                return int(drawn_number) * sumOfUnmarked(tables[tables_won[-1]], dummy_tables[tables_won[-1]])


print(playGameSecond(numbers_drawn, tables, dummy_tables))
