from itertools import combinations #,groupby

""" Find antenna positions from the input """
def find_antennas(map_table):
    antenna_list = []
    for row_idx, row in enumerate(map_table):
        for col_idx, elem in enumerate(row):
            if elem not in [".", "#"]:
                antenna_list.append( {"freq": elem, "row": row_idx, "col": col_idx} )
    return antenna_list

def get_distance(pair: tuple):
    #if pair[0]["row"] > pair[1]["row"]:  # be sure if pair[0] is upper
    #    pair = (pair[1], pair[0])
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

""" Antinodes based on part 1 definition """
def get_antinodes(pair: tuple):
    dist = get_distance(pair)
    antinode1 = { "row": pair[0]["row"] - dist["diff_row"], "col": pair[0]["col"] - dist["diff_col"] }
    antinode2 = { "row": pair[1]["row"] + dist["diff_row"], "col": pair[1]["col"] + dist["diff_col"] }
    return antinode1, antinode2

""" Antinodes based on part 2 definition """
def get_all_distance_antinodes(pair: tuple, map_width: int, map_height: int):
    antinodes = list()
    dist = get_distance(pair)

    # steps in negative direction
    node = dict(pair[0]) #if pair[0]["row"] < pair[1]["row"] else pair[1]
  #  if node["row"] >= 0 and node["col"] >= 0 and node["col"] < map_width:
  #      antinodes.append(str(node))
  #      print(f"Újabb antinode a listán: {node}")

    while node["row"] >= 0:
        node["col"] -= dist["diff_col"]
        node["row"] -= dist["diff_row"]
        if node["row"] >= 0 and node["col"] >= 0 and node["col"] < map_width:
            antinodes.append(str(node))
            #print(f"Újabb antinode a listán: {node}")

    # steps in positive direction
    node = dict(pair[1]) # if pair[1]["row"] > pair[0]["row"] else pair[0]
  #  if node["row"] < map_height and node["col"] >= 0 and node["col"] < map_width:
  #       antinodes.append(str(node))
      #  print(f"Újabb antinode a listán: {node}")

    while node["row"] < map_height:
        node["col"] += dist["diff_col"]
        node["row"] += dist["diff_row"]
        if node["row"] < map_height and node["col"] >= 0 and node["col"] < map_width:
            antinodes.append(str(node))
        #    print(f"Újabb antinode a listán: {node}")

    return antinodes

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

    print(f"Different antinodes count: {len(antinodes)} - equal distance")

    # Part 2
    #get_all_distance_antinodes( ({"row": 2, "col": 5},  {"row": 3, "col": 7}), map_width, map_height )
    #print( get_all_distance_antinodes( ({"row": 8, "col": 8},  {"row": 9, "col": 9}), map_width, map_height ) )

    antinodes = list()
    all_combinations_test = [ ( {"freq": "T", "row": 0, "col": 0}, {"freq": "T", "row": 2, "col": 1})
                             ,( {"freq": "T", "row": 0, "col": 0}, {"freq": "T", "row": 1, "col": 3} )
                             ,( {"freq": "T", "row": 1, "col": 3}, {"freq": "T", "row": 2, "col": 1} ) ] 
    for pair in all_combinations:
      #  print(f"Vizsgált pár: {pair}")
        antinodes.extend( get_all_distance_antinodes(pair, map_width, map_height) )
     #   print(f"A listánk ezzel {len(antinodes)} méretűre bővült")

    print(len(set(antinodes)))

if __name__ == "__main__":
    main()