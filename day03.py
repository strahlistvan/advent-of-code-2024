import re

with open("input/day03-input.txt", "r") as file:
    input_lines = file.readlines()

result = 0
for input in input_lines:
    expressions = re.findall("mul\(\d+,\d+\)", input)
    for exp in expressions:
        operands = re.findall("\d+", exp)
        result += int(operands[0]) * int(operands[1])

print(f"The result of multiplications: {result}")