import re
from itertools import product

with open("input/day07-input.txt", "r") as file:
    equation_list = list()
    for line in file:
       elem = list(filter(lambda s: len(s) > 0, re.split('\s+|:', line.strip())))
       equation_list.append(elem)
"""
signs = list()

def gen_all_signs(size, sign_str = ''):
    if size > 0:
        gen_all_signs(size-1, sign_str + '+')
        gen_all_signs(size-1, sign_str + '*')
    else:
        signs.append(sign_str)
"""
def gen_all_signs(size):
    # generate combinations with itertools.product 
    return ["".join(sign) for sign in product("+*", repeat=size)]

def gen_expressions(equation):
    calibration_result = 0
    sign_count = len(equation) - 2 # first element int the equation is the expected result
    signs = gen_all_signs(sign_count)
    for sign in signs:
        expr = ""
        expr_value = int(equation[1])
        for i in range(1, len(equation)-1):
            expr += equation[i] + sign[i-1]
            if sign[i-1] == "+":
                expr_value += int(equation[i+1])
            else:
                expr_value *= int(equation[i+1])
        expr += equation[-1]
        if (expr_value == int(equation[0])):
            print(expr + " = " + str(expr_value))
            calibration_result = expr_value
    return calibration_result

print(equation_list)

all_calibration_results = [ gen_expressions(equation) for equation in equation_list ]
print(f"total calibration result: {sum(all_calibration_results)}")