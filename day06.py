import time
import platform
import os

map_table = []

with open("input/day06-test-input.txt", "r") as file:
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

    def __init__(self, position, direction='^'):
        self.position  = position
        self.direction = direction

    def __str__(self):
        return f"Guard {self.direction} in position: {self.position}"

    def turn(self):
        idx = self.direction_list.index(self.direction)
        idx = (idx + 1) % len(self.direction_list)
        self.direction = self.direction_list[idx]

    def step(self):
        if self.direction == '^':
            self.position["row"] -=1
        elif self.direction == 'V':
            self.position["row"] +=1
        elif self.direction == '<':
            self.position["col"] -=1
        elif self.direction == '>':
            self.position["col"] += 1
        else:
            print("Cannot step")

    def get_next_step(self):
        next_step = dict(self.position)
        if self.direction == '^':
            next_step["row"] -=1
        elif self.direction == 'V':
            next_step["row"] +=1
        elif self.direction == '<':
            next_step["col"] -=1
        elif self.direction == '>':
            next_step["col"] += 1
        return next_step

""" Does the guard left the map? """
def is_gone(guard: Guard, map_table: list):
    next_step = guard.get_next_step()
    if next_step["row"] < 0 or next_step["col"] < 0:
        return True
    if next_step["row"] >= len(map_table) or next_step["col"] >= len(map_table[0]):
        return True
    return False

obstacle_list, guard_pos = find_obstacles_and_guard(map_table)
print(obstacle_list)

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

""" Demo for visual debugging """
def print_map_with_guard(guard: Guard, map_table: list):
    for i in range(len(map_table)):
        for j in range(len(map_table[i])):
            if guard.position["row"] == i and guard.position["col"] == j:
                print(guard.direction, end=" ")
            elif map_table[i][j] == "^": # do not show initial guard position all the time
                print(".", end=" ")
            else:
                print(map_table[i][j], end=" ")
        print("")

guard = Guard(guard_pos)
path = [str(guard_pos)] # including the guard's starting position

while not is_gone(guard, map_table):
    if guard.get_next_step() not in obstacle_list:
        path.append(str(guard.get_next_step()))
        guard.step()
    else:
        guard.turn()
    # Visual demo
    time.sleep(0.5)
    clear_console()
    print_map_with_guard(guard, map_table)

print(path)
print(f"Guard visit {len(set(path))} distinct positions before leave")