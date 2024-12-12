import re
import time
import platform
import os

with open("input/day10-test-input-3.txt", "r") as file:
    topographic_map = file.read().strip().split("\n")

ROW_COUNT = len(topographic_map)
COL_COUNT  = len(topographic_map[0])
hiking_trail_set = set()

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def print_map(topographic_map: list, trail: str):
    time.sleep(1)
    clear_console()
    trail_list = [ re.findall("\d+", str) for str in trail.split() ]
    for i, row in enumerate(topographic_map):
        for j, char in enumerate(list(row)):
            if [str(i), str(j)] in trail_list:
                print(f"\033[1;33m {char}", end="")
            else:
                print(f"\033[1;37m {char}", end="")
        print("")

def search_next_height(height: int, row: int, col:int, trail=""):
    if height > 9:
        hiking_trail_set.add(trail)
        return

    if topographic_map[row][col] == str(height):
        trail += f" [{row},{col}]"
        print_map(topographic_map, trail)

        #print(f"{height+1} keresése innen indulva {row}, {col}, eddigi út {trail}")
        if row+1 < ROW_COUNT:
            search_next_height(height+1, row+1, col, trail)
        if row-1 >= 0:
            search_next_height(height+1, row-1, col, trail)
        if col+1 < COL_COUNT:
            search_next_height(height+1, row, col+1, trail)
        if col-1 >= 0:
            search_next_height(height+1, row, col-1, trail)

def main():
    score_sum = 0
    for i, row in enumerate(topographic_map):
        for j, pos in enumerate(row):
            if pos == "0":
               # hiking_trail_set = set() # new empty set
                print(f"{i},{j} helyen hiking trail keresése")
                search_next_height(0, i, j, trail="")
                score_sum += len(hiking_trail_set)
                print(f"\033[1;33m Score after ({i},{j}) trailhead: {score_sum}")

if __name__ == "__main__":
    main()