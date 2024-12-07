import time
import platform
import os

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
    state = dict()
    step_count = 0

    def __init__(self, pos_row, pos_col, direction='^'):
        self.state["pos_row"] = pos_row
        self.state["pos_col"] = pos_col
        self.state["direction"] = direction
        self.step_count = 0

    def __str__(self):
        return f"Guard {self.state['direction']} in position: row={self.state['pos_row']}, rol={self.state['pos_col']}"

    def turn(self):
        idx = self.direction_list.index(self.state["direction"])
        idx = (idx + 1) % len(self.direction_list)
        self.state["direction"] = self.direction_list[idx]

    def step(self):
        if self.state["direction"] == '^':
            self.state["pos_row"] -=1
        elif self.state["direction"] == 'V':
            self.state["pos_row"] +=1
        elif self.state["direction"] == '<':
            self.state["pos_col"] -=1
        elif self.state["direction"] == '>':
            self.state["pos_col"] += 1
        self.step_count += 1

    def get_next_step(self):
        next_step_row = int(self.state["pos_row"])
        next_step_col = int(self.state["pos_col"])
        if self.state["direction"] == '^':
            next_step_row -=1
        elif self.state["direction"] == 'V':
            next_step_row +=1
        elif self.state["direction"] == '<':
            next_step_col -=1
        elif self.state["direction"] == '>':
            next_step_col += 1
        return {"row": next_step_row, "col": next_step_col}

""" Does the guard left the map? """
def is_gone(guard: Guard, map_width: int, map_height: int):
    next_step = guard.get_next_step()
    if next_step["row"] < 0 or next_step["col"] < 0:
        return True
    if next_step["row"] >= map_width or next_step["col"] >= map_height:
        return True
    return False

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

""" Demo for visual debugging """
def print_map_with_guard(guard: Guard, map_width: int, map_height: int, obstacle_list: list):
    for i in range(map_width):
        for j in range(map_height):
            if guard.pos_row == i and guard.pos_col == j:
                print(guard.direction, end=" ")
            elif {"row": i, "col": j} in obstacle_list:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print("")

""" Main routine - run guard from a given start position """
def run(start_pos, map_width, map_height, obstacle_list, demo=False):
    guard = Guard(start_pos["row"], start_pos["col"])
    path = [str(start_pos)] # including the guard's starting position
    while not is_gone(guard, map_width, map_height):
        if guard.get_next_step() not in obstacle_list:
            path.append(str(guard.get_next_step()))
            guard.step()
        else:
            guard.turn()
        if demo:
            time.sleep(0.1)
            clear_console()
            print_map_with_guard(guard, map_width, map_height, obstacle_list)
        if guard.step_count > (map_width * map_height): # not really optimal...
            return -1 # avoid infinite loop
    return path

if __name__ == "__main__":

    with open("input/day06-input.txt", "r") as file:
        map_table= file.read().split("\n")

    map_width  = len(map_table)
    map_height = len(map_table[0])
    obstacle_list, start_pos = find_obstacles_and_guard(map_table)
    path = run(start_pos, map_width, map_height, obstacle_list, demo=False)
    print(f"Guard visit {len(set(path))} distinct positions before leave")

    # Part 2

    count = 0
    for i in range(map_width):
        for j in range(map_height):
            new_obs = {"row": i, "col": j}
            if new_obs not in obstacle_list:
                extended_obstacles = obstacle_list.copy() 
                extended_obstacles.append(new_obs)
               # print(f"Start with new obstacle: {new_obs}")
                path = run(start_pos, map_width, map_height, extended_obstacles, demo=False)
                if path == -1:
                    print(f"Infinite partoling detected with {new_obs}")
                    count += 1
    print(f"Infinite patroling with {count} different positions")
