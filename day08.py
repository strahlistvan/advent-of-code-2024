from itertools import combinations #,groupby

""" Find antenna positions from the input """
def find_antennas(map_table):
    antenna_list = []
    for row_idx, row in enumerate(map_table):
        for col_idx, elem in enumerate(row):
            if elem not in [".", "#"]:
                antenna_list.append({"freq": elem, "row": row_idx, "col": col_idx} )
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

#def to_str_a(antenna: dict):
#    return f"{antenna['freq']},{antenna['row']}|{antenna['col']}"

""" For some mystical reason I could not use itertools.groupby properly... :( """
def groupby_impl(antenna_list, key = lambda elem: elem["freq"]):
    antenna_list = sorted(antenna_list, key = key) # sort list by key
    group_by_freq = list()

    previous_freq = antenna_list[0]["freq"]
    group_list = list()
    for antenna in antenna_list:
        if antenna["freq"] == previous_freq:
            group_list.append( antenna )
        else:
            group_by_freq.append(group_list)
            group_list = list() 
            group_list.append( antenna )
        previous_freq = antenna["freq"]
    
    group_by_freq.append(group_list)
    return group_by_freq

def main():
    with open("input/day08-input.txt", "r") as file:
        map_table= file.read().split("\n")
        map_width  = len(map_table)
        map_height = len(map_table[0])
        print(f"Read map successfull: width: {map_width} height: {map_height}")

    antennas = find_antennas(map_table)

    # Group antennas by signal, and find all 2-element subsets (combinations)
    all_combinations = list()
    for positions in groupby_impl(antennas, key = lambda elem: elem["freq"]):
        all_combinations.extend( list(combinations(positions, 2)) )

    antinodes = set()
    for pair in all_combinations:
        a1, a2 = get_antinodes(pair)
        if is_on_map(a1, map_width, map_height):
            antinodes.add(str(a1))
        if is_on_map(a2, map_width, map_height):
            antinodes.add(str(a2))

    #print("All antinodes: ")
    #print(antinodes)
    print(f"Different antinodes count: {len(antinodes)}")

if __name__ == "__main__":
    main()