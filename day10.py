import re
import time
import platform
import os

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

""" Visual debugging """
def print_map(topographic_map: list, trail: str):
    time.sleep(0.3)
    clear_console()
    trail_list = [ re.findall("\d+", str) for str in trail.split() ]
    for i, row in enumerate(topographic_map):
        for j, char in enumerate(list(row)):
            if [str(i), str(j)] in trail_list:
                print(f"\033[1;33m {char}", end="")
            else:
                print(f"\033[1;37m {char}", end="")
        print("")

""" Hiking trails from a given start position """
def search_hiking_trails(row: int, col: int, topographic_map: list):

    ROW_COUNT = len(topographic_map)
    COL_COUNT  = len(topographic_map[0])

    hiking_trailhead_set = set() # only start and end positions
    hiking_trail_set = set() # full path

    """ recursive inner function """
    def search_next_height(height: int, row: int, col:int, trail=""):
        if height > 9:
            hiking_trail_set.add(trail)
            trail = trail.split()[0] + ' ' + trail.split()[-1] # only start and end position
            hiking_trailhead_set.add(trail)
            return
        if topographic_map[row][col] == str(height):
            trail += f" [{row},{col}]"
            if row+1 < ROW_COUNT:
                search_next_height(height+1, row+1, col, trail)
            if row-1 >= 0:
                search_next_height(height+1, row-1, col, trail)
            if col+1 < COL_COUNT:
                search_next_height(height+1, row, col+1, trail)
            if col-1 >= 0:
                search_next_height(height+1, row, col-1, trail)

    search_next_height(0, row, col, trail="")

    return hiking_trailhead_set, hiking_trail_set

def main():

    with open("input/day10-input.txt", "r") as file:
        topographic_map = file.read().strip().split("\n")

    score_sum = 0
    score_all_sum = 0
    for i, row in enumerate(topographic_map):
        for j, pos in enumerate(row):
            if pos == "0":
                hth_set, ht_set = search_hiking_trails(i, j, topographic_map)
                # print(f"\033[1;37m Score of the ({i},{j}) trailhead: {len(hth_set)}")
                # print(f"\033[1;37m Score of the ({i},{j}) trail with full path: {len(ht_set)}")
                score_sum += len(hth_set)
                score_all_sum += len(ht_set)
    print(f"\033[1;37m Score after ({i},{j}) trailhead: {score_sum}")
    print(f"\033[1;37m Score all path after ({i},{j}) trailhead: {score_all_sum} - part 2")

if __name__ == "__main__":
    main()