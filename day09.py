""" convert dense format to long format """
def to_long_format(disk_map_dense: str):
    long_disk_map = ""
    id_number = 0
    for idx, ch in enumerate(disk_map_dense):
        if idx % 2 == 0:
           long_disk_map += str(int(ch) * f"{id_number} ")
           id_number += 1
        else:
            long_disk_map += int(ch) * ". "
    return long_disk_map

""" move one file block from the end to the leftmost free space block """
def move_block(disk_map_blocks: list):
    while disk_map_blocks[-1] == ".":   # "trim" clean spaces from the end
        disk_map_blocks.pop()

    if disk_map_blocks.count(".") > 0:
        idx = disk_map_blocks.index(".")
        disk_map_blocks[idx] = disk_map_blocks.pop()

    return disk_map_blocks

def calc_checksum(disk_map_arr: list):
    product_list = [ idx * int(ch) for idx, ch in enumerate(disk_map_arr) if ch != '.' ]
    return sum(product_list)

""" Find the first free space with a given size"""
def find_space(disk_map_blocks: list, space_size: int):
    finded_space_size = 0
    finded_space_pos = -1
    for i, block in enumerate(disk_map_blocks):
        if block == ".": # while empty
            finded_space_size += 1
            if finded_space_pos == -1: # first position
                finded_space_pos = i
            if finded_space_size == space_size: # just found a matching empty space!
                return finded_space_pos
        else: # not empty
            finded_space_pos = -1
            finded_space_size = 0
    return None

""" Get the first block position of the file ID """
def find_file_by_id(disk_map: list, file_id: str):
    for idx, block in enumerate(disk_map):
        if block == file_id:
            return idx

""" Calculate file length from first block position - PART 2, no fragmentation! """
def find_len_by_start(disk_map: list, file_start: int):
    idx = file_start
    lenght = 0
    while idx < len(disk_map) and disk_map[idx] == disk_map[file_start]:
        lenght += 1
        idx += 1
    return lenght

""" Move a whole file block by block - PART 2, no fragmentation! """
def move_file(disk_map_blocks: list, file_start: int, file_len: int, to_pos: int):
    # Put file to empty space position
    for i in range(to_pos, to_pos + file_len):
        disk_map_blocks[i] = disk_map_blocks[file_start]
    # Empty spaces to file position
    for i in range(file_start, file_start + file_len):
        disk_map_blocks[i] = "."
    # "trim" clean spaces from the end
    while disk_map_blocks[-1] == ".":
        disk_map_blocks.pop()

def main():
   # disk_map_dense = "2333133121414131402"
    with open("input/day09-input.txt", "r") as file:
        disk_map_dense = file.read().strip()

    disk_map_blocks = to_long_format(disk_map_dense).split()
    disk_map_files  = disk_map_blocks.copy()

    while disk_map_blocks.count(".") > 0:
        disk_map_blocks = move_block(disk_map_blocks)

    print(f"The filesystem checksum: {calc_checksum(disk_map_blocks)}")

    # PART 2
 
    file_id_list = [f for f in disk_map_files if f != '.']
    file_id_list.reverse()

    for file_id in file_id_list:
        file_start = find_file_by_id(disk_map_files, file_id)
        file_len   = find_len_by_start(disk_map_files, file_start)
        space_pos  = find_space(disk_map_files, file_len)
        if space_pos and space_pos < file_start:
            move_file(disk_map_files, file_start, file_len, space_pos)

    print(f"The filesystem checksum: {calc_checksum(disk_map_files)} - without file fragmentation")

if __name__ == "__main__":
    main()

