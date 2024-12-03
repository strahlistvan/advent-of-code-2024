import re

with open("input/day03-input.txt", "r") as file:
    input_lines = file.readlines()

result1 = 0
result2 = 0
enabled = 1
for input in input_lines:
    expressions = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", input)
    for exp in expressions:
        if exp == "do()":
            enabled = 1
        elif exp == "don't()":
            enabled = 0
        elif "mul" in exp:
            operands = re.findall("\d+", exp)
            result1 += int(operands[0]) * int(operands[1])
            result2 += ( int(operands[0]) * int(operands[1]) ) * enabled

print(f"The result of multiplications: {result1}")
print(f"The result of multiplications with do-s and don't-s: {result2}")