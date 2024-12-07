import re
from itertools import product

def gen_all_signs(size, sign_str="+*"):
    # generate combinations with itertools.product 
    return ["".join(sign) for sign in product(sign_str, repeat=size)]

def gen_expressions(equation, sign_str):
    calibration_result = 0
    sign_count = len(equation) - 2 # first element int the equation is the expected result
    signs = gen_all_signs(sign_count, sign_str)
    for sign in signs:
        expr = "" # expression string to print - only for debugging
        expr_value = int(equation[1])
        for i in range(1, len(equation)-1):
            expr += equation[i] + sign[i-1]
            if sign[i-1] == "+":
                expr_value += int(equation[i+1])
            elif sign[i-1] == "*":
                expr_value *= int(equation[i+1])
            else: # concatenation - only used in part 2
                expr_value = int(str(expr_value) + str(equation[i+1]))
        expr += equation[-1] # last number
        if (expr_value == int(equation[0])):
            print(f"{expr} = {expr_value}")
            calibration_result = expr_value
    return calibration_result

def main():
    with open("input/day07-test-input.txt", "r") as file:
        equation_list = list()
        for line in file:
            elem = list(filter(lambda s: len(s) > 0, re.split('\s+|:', line.strip())))
            equation_list.append(elem)

    all_calibration_results = [ gen_expressions(equation, "+*") for equation in equation_list ]
    print(f"total calibration result: {sum(all_calibration_results)}")

    # part 2
    all_calibration_results = [ gen_expressions(equation, "+*|") for equation in equation_list ]
    print(f"total calibration result - with concatenation: {sum(all_calibration_results)}")

if __name__ == "__main__":
    main()