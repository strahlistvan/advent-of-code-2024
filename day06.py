import time
import platform
import os

map_table = []

with open("input/day06-input.txt", "r") as file:
    map_table= file.read().split("\n")

""" Find coordinates of obstacles and the guard from the input """
def find_obstacles_and_guard(map_table):
    obstacle_list = []
    for row_idx, row in enumerate(map_table):
        col_indexes = [j for j, elem in enumerate(row) if elem == "#"]
        for col_idx in col_indexes:
            obstacle_list.append({"row": row_idx, "col": col_idx} )
        if row.find("^") != -1:
            guard_pos = {"row": row_idx, "col": row.find("^"),}
    return obstacle_list, guard_pos

"""
 Simulates a guard patroling:
  - If there is something directly in front of you, turn right 90 degrees.
  - Otherwise, take a step forward.
"""
class Guard:

    direction_list = ['^', '>', 'V', '<']
    step_count = 0

    def __init__(self, pos_row, pos_col, direction='^'):
        self.pos_row = pos_row
        self.pos_col = pos_col
        self.direction = direction
        self.step_count = 0

    def __str__(self):
        return f"Guard {self.direction} in position: row={self.pos_row}, rol={self.pos_col}"

    def turn(self):
        idx = self.direction_list.index(self.direction)
        idx = (idx + 1) % len(self.direction_list)
        self.direction = self.direction_list[idx]

    def step(self):
        if self.direction == '^':
            self.pos_row -=1
        elif self.direction == 'V':
            self.pos_row +=1
        elif self.direction == '<':
            self.pos_col -=1
        elif self.direction == '>':
            self.pos_col += 1
        self.step_count += 1

    def get_next_step(self):
        next_step_row = int(self.pos_row)
        next_step_col = int(self.pos_col)
        if self.direction == '^':
            next_step_row -=1
        elif self.direction == 'V':
            next_step_row +=1
        elif self.direction == '<':
            next_step_col -=1
        elif self.direction == '>':
            next_step_col += 1
        return {"row": next_step_row, "col": next_step_col}

""" Does the guard left the map? """
def is_gone(guard: Guard, map_table: list):
    next_step = guard.get_next_step()
    if next_step["row"] < 0 or next_step["col"] < 0:
        return True
    if next_step["row"] >= len(map_table) or next_step["col"] >= len(map_table[0]):
        return True
    return False

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

""" Demo for visual debugging """
def print_map_with_guard(guard: Guard, map_table: list, obstacle_list):
    for i in range(len(map_table)):
        for j in range(len(map_table[i])):
            if guard.pos_row == i and guard.pos_col == j:
                print(guard.direction, end=" ")
            elif {"row": i, "col": j} in obstacle_list: # for part 2
                print("X", end=" ")
            else:
                print(".", end=" ")
        print("")

""" Main routine - run guard from a given start position """
def run(start_pos, map_table, obstacle_list, demo=False):
    guard = Guard(start_pos["row"], start_pos["col"])
    path = [str(start_pos)] # including the guard's starting position
    while not is_gone(guard, map_table):
        if guard.get_next_step() not in obstacle_list:
            path.append(str(guard.get_next_step()))
            guard.step()
        else:
            guard.turn()
        if demo:
            time.sleep(0.1)
            clear_console()
            print_map_with_guard(guard, map_table, obstacle_list)
        if guard.step_count > (4 * len(map_table) * len(map_table[0])): # not really optimal...
            return -1 # avoid infinite loop
    return path

if __name__ == "__main__":

    obstacle_list, start_pos = find_obstacles_and_guard(map_table)
    path = run(start_pos, map_table, obstacle_list, demo=False)
    print(f"Guard visit {len(set(path))} distinct positions before leave")

    # Part 2

    count = 0
    for i in range(len(map_table)):
        for j in range(len(map_table[0])):
            new_obs = {"row": i, "col": j}
            if new_obs not in obstacle_list:
                extended_obstacles = obstacle_list.copy() 
                extended_obstacles.append(new_obs)
               # print(f"Start with new obstacle: {new_obs}")
                path = run(start_pos, map_table, extended_obstacles, demo=False)
                if path == -1:
                    print(f"Infinite partoling detected with {new_obs}")
                    count += 1
    print(f"Infinite patroling with {count} different positions")
