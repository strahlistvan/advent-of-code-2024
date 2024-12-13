import re

def read_input_file(filename: str):
    test_cases = list()
    with open(filename, "r") as file:
        test_case = dict()
        for line in file:
            arr = re.findall("\d+", line)
            if line.startswith("Button A"):
                test_case['button_A_x'] = int(arr[0])
                test_case['button_A_y'] = int(arr[1])
            elif line.startswith("Button B"):
                test_case['button_B_x'] = int(arr[0])
                test_case['button_B_y'] = int(arr[1])
            elif line.startswith("Prize"):
                test_case['prize_x'] = int(arr[0])
                test_case['prize_y'] = int(arr[1])
            else: # new line
                test_cases.append(dict(test_case))
        test_cases.append(dict(test_case))
    return test_cases

def get_min_cost(test_case: dict):
    min_cost = -1
    for count_A_press in range(101):
        for count_B_press in range(101):
            claw_x = 0
            claw_y = 0
            claw_x += (count_A_press * test_case['button_A_x']) + (count_B_press * test_case['button_B_x'])
            claw_y += (count_A_press * test_case['button_A_y']) + (count_B_press * test_case['button_B_y'])
            if claw_x == test_case['prize_x'] and claw_y == test_case['prize_y']:
                cost = 3 * count_A_press + count_B_press
                if min_cost < 0 or cost < min_cost:
                    min_cost = cost
    return min_cost

def main():
    sum_tokens = 0
    test_cases = read_input_file("input/day13-input.txt")
    for test_case in test_cases:
        min_cost = get_min_cost(test_case)
        if min_cost > -1: # -1 means no solution
            sum_tokens += min_cost
    print(f"Fewest tokens to win all prizes: {sum_tokens}")

if __name__ == "__main__":
    main()