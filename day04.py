with open("input/day04-input.txt", "r") as file:
    letters = []
    for line in file:
        letters.append(list(line.strip()))

""" # Don't need the numpy library!
letters = np.array(letters)

def count_words(letters, pattern):
    count = 0
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            word = "".join(letters[i][j:j+4])
            count += len(re.findall(pattern, word))
    return count

def count_words_diag(letters, pattern):
    count = 0
    for i in range(-len(letters), len(letters)):
        diag = "".join(letters.diagonal(i))
        count += len(re.findall(pattern, diag))
    return count
"""

def check_horizontal(table, row, col):
    str = ""
    end = min(col + 4, len(table[row]))
    for k in range(col, end):
        str += table[row][k]
    return 1 if (str == "XMAS" or str == "SAMX") else 0

def check_vertical(table, row, col):
    str = ""
    end = min(row + 4, len(table))
    for k in range(row, end):
        str += table[k][col]
    return 1 if (str == "XMAS" or str == "SAMX") else 0

def check_main_diag(table, row, col):
    str = ""
    end_row = min(row + 4, len(table))
    end_col = min(col + 4, len(table[row]))
    for k in range(4):
        if row + k < end_row and col + k < end_col:
            str += table[row + k][col + k]
    return 1 if (str == "XMAS" or str == "SAMX") else 0

def check_other_diag(table, row, col):
    str = ""
    end_row = min(row + 4, len(table))
    end_col = max(col - 4, 0)
    for k in range(4):
        if row + k < end_row and col - k >= end_col:
            str += table[row + k][col - k]
    return 1 if (str == "XMAS" or str == "SAMX") else 0

count = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        count += check_horizontal(letters, i, j)
        count += check_vertical(letters, i, j)
        count += check_main_diag(letters, i, j)
        count += check_other_diag(letters, i, j)
print(f"The word XMAS count in puzzle: {count}")

# Part 2

def check_x_mas(table, row, col):
    if table[row][col] != 'A': # not A in the middle - cannot be X-MAS
        return 0
    if set([table[row-1][col-1], table[row-1][col+1], table[row+1][col-1], table[row+1][col+1]]) != set(['M', 'S']): # invalid characters
        return 0
    if table[row-1][col-1] == 'M' and table[row+1][col+1] != 'S': # bad diagonal (MM or SS)
        return 0
    if table[row-1][col-1] == 'S' and table[row+1][col+1] != 'M': # bad diagonal (MM or SS)
        return 0
    if table[row-1][col+1] == 'M' and table[row+1][col-1] != 'S': # bad diagonal (MM or SS)
        return 0
    if table[row-1][col+1] == 'S' and table[row+1][col-1] != 'M': # bad diagonal (MM or SS)
        return 0
    return 1 # Merry X-MAS!

# check everything except the boundaries
count = 0
for i in range(1, len(letters)-1):
    for j in range(1, len(letters[i])-1):
        count += check_x_mas(letters, i, j)
print(f"X-MAS count in puzzle: {count}")