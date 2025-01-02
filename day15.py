import platform
import os
import time

class Robot:
    def __init__(self, row: int, col: int, warehouse_map: list):
        self.row = row
        self.col = col
        self.warehouse_map = warehouse_map
    def __str__(self) -> str:
        return f"Robot in ({self.row},{self.col})"
    def move(self, direction):
        r = self.row
        c = self.col
        if r < 0 or r >= len(self.warehouse_map[0]) or c < 0 or c >= len(self.warehouse_map):
            return
        if direction == "^" and self.warehouse_map[r-1][c] != "#":
            if self.warehouse_map[r-1][c] == "O": # there is a box in front of the robot
                idx = r-1
                while self.warehouse_map[idx][c] == "O":
                    idx-=1
                if self.warehouse_map[idx][c] == "#": # can not step
                    return
                else: # step - throw all the boxes
                    self.warehouse_map[idx][c] = "O"
            self.warehouse_map[r][c] = "."
            self.row -= 1
            self.warehouse_map[r-1][c] = "@"
        elif direction == "v" and self.warehouse_map[r+1][c] != "#":
            if self.warehouse_map[r+1][c] == "O": # there is a box in front of the robot
                idx = r+1
                while self.warehouse_map[idx][c] == "O":
                    idx+=1
                if self.warehouse_map[idx][c] == "#": # can not step
                    return
                else: # step - throw all the boxes
                    self.warehouse_map[idx][c] = "O"
            self.warehouse_map[r][c] = "."
            self.row += 1
            self.warehouse_map[r+1][c] = "@"
        elif direction == "<" and self.warehouse_map[r][c-1] != "#":
            if self.warehouse_map[r][c-1] == "O": # there is a box in front of the robot
                idx = c-1
                while self.warehouse_map[r][idx] == "O":
                    idx-=1
                if self.warehouse_map[r][idx] == "#": # can not step
                    return
                else: # step - throw all the boxes
                    self.warehouse_map[r][idx] = "O"
            self.warehouse_map[r][c] = "."
            self.col -= 1
            self.warehouse_map[r][c-1] = "@"
        elif direction == ">" and self.warehouse_map[r][c+1] != "#":
            if self.warehouse_map[r][c+1] == "O": # there is a box in front of the robot
                idx = c+1
                while self.warehouse_map[r][idx] == "O":
                    idx+=1
                if self.warehouse_map[r][idx] == "#": # can not step
                    return
                else: # step - throw all the boxes
                    self.warehouse_map[r][idx] = "O"
            self.warehouse_map[r][c] = "."
            self.col += 1
            self.warehouse_map[r][c+1] = "@"

def read_input(filename):
    warehouse_map = list()
    with open(filename) as file:
        # read warehouse map
        line = list(file.readline().strip("\n"))
        while line:
            warehouse_map.append(line)
            line = list(file.readline().strip("\n"))
        # read commands
        line = file.readline().strip("\n")
        commands = ""
        while line:
            commands += line
            line = file.readline().strip("\n")
    return warehouse_map, commands

def print_map(warehouse_map):
    for line in warehouse_map:
        print(" ".join(line))

def find_robot_pos(warehouse_map):
    for row_idx, row in enumerate(warehouse_map):
        col_idx = "".join(row).find("@")
        if col_idx != -1:
            return row_idx, col_idx
    return None

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    warehouse_map, commands = read_input("input/day15-input.txt")

    row, col = find_robot_pos(warehouse_map)
    robot = Robot(row, col, warehouse_map)
    print(commands)

    for command in commands:
        robot.move(command)
        #print(command)
        #print(robot)
        #print_map(robot.warehouse_map)
        #time.sleep(0.2)
        #clear_console()

    print_map(robot.warehouse_map)
    sum_gps = 0
    for r in range(len(robot.warehouse_map)):
        for c in range(len(robot.warehouse_map[r])):
            if robot.warehouse_map[r][c] == "O":
                sum_gps += (100 * r + c)
    print(f"sum of all GPS coordinates: {sum_gps}")

if __name__ == "__main__":
    main()

