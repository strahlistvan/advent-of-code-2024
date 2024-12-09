from itertools import groupby, combinations

""" Find antenna positions from the input """
def find_antennas(map_table):
    antenna_list = []
    for row_idx, row in enumerate(map_table):
        for col_idx, elem in enumerate(row):
            if elem not in [".", "#"]:
                antenna_list.append({"freq": elem, "row": row_idx, "col": col_idx} )
    # antenna_list = sorted(antenna_list, key = lambda elem: elem["freq"]) # sort list by frequency
    return antenna_list

def get_distance(pair: tuple):
    diff_row = pair[1]["row"] - pair[0]["row"]
    diff_col = pair[1]["col"] - pair[0]["col"]
    return {"diff_row": diff_row, "diff_col": diff_col}

""" Does the object is on the the map? """
def is_on_map(obj: dict, map_width: int, map_height: int):
    if obj["row"] < 0 or obj["col"] < 0:
        return False
    if obj["row"] >= map_width or obj["col"] >= map_height:
        return False
    return True

def get_antinodes(pair: tuple):
    dist = get_distance(pair)
    antinode1 = { "row": pair[0]["row"] - dist["diff_row"], "col": pair[0]["col"] - dist["diff_col"] }
    antinode2 = { "row": pair[1]["row"] + dist["diff_row"], "col": pair[1]["col"] + dist["diff_col"] }
    return antinode1, antinode2

if __name__ == "__main__":
    with open("input/day08-input.txt", "r") as file:
        map_table= file.read().split("\n")
        map_width  = len(map_table)
        map_height = len(map_table[0])
        print(f"Read map successfull: width: {map_width} height: {map_height}")

    antennas = find_antennas(map_table)
    print("All antenna position:")
    print(len(antennas))

    all_combinations = list()
    for freq, positions in groupby(antennas, key = lambda elem: elem["freq"]):
        position_list = list(positions)
        print(position_list)
        print(f"{freq} positions: {position_list}")
        all_combinations.extend( list(combinations(position_list, 2)) )

    print(f"2 elemű kombinációk: {all_combinations}")
    antinode_list = list()
    for pair in all_combinations:
        a1, a2 = get_antinodes(pair)
        if is_on_map(a1, map_width, map_height):
            antinode_list.append(str(a1))
        if is_on_map(a2, map_width, map_height):
            antinode_list.append(str(a2))
print("All antinodes: ")
antinode_list.sort()
print(antinode_list)
print(f"Different antinodes count: {len(set(antinode_list))}")