import numpy as np
import re

with open("input/day04-input.txt", "r") as file:
    letters = []
    for line in file:
        letters.append(list(line.strip()))

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

xmas_count = count_words(letters, "XMAS|SAMX")
print(xmas_count)
xmas_count += count_words(letters.T, "XMAS|SAMX")
print(xmas_count)
xmas_count += count_words_diag(letters, "XMAS|SAMX")
print(xmas_count)
xmas_count += count_words_diag(letters.T, "XMAS|SAMX")
print(xmas_count)