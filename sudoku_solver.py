def write_suduko(l):
    global row
    numbers = [1, 2, 3]
    for j, row in enumerate(l):
        for column_num, k in enumerate(row):
            if k == 0:
                row_num = 0
                colum = []
                while row_num < 3:
                    colum.append(l[row_num][column_num])
                    row_num += 1

                validation(row, colum, j, column_num)
    print("after updating", l)


def validation(rowe, column, row_num, column_num):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in numbers:
        if num not in column and num not in rowe:
            if is_safe(row_num, column_num, num):
                l[row_num][column_num] = num
                row[column_num] = num


def is_safe(row_num, column_num, num):
    start_row, start_col = 3 * (row_num // 3), 3 * (column_num // 3)
    for i in range(3):
        for j in range(3):
            if l[i + start_row][j + start_col] == num:
                return False

    return True


global l
# l = [[0, 3, 0], [1, 2, 0], [0, 0, 2]]
# write_suduko(l)
l = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]
write_suduko(l)
# l = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# write_suduko(l)
