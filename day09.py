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

def print_disk_map(disk_map: list):
    print(" ".join(disk_map))

""" convert diskmap block format to file format (lists-in-list) """
def to_disk_map_files(disk_map_blocks: list):
    disk_map_files = list()
    file = list()
    for block in disk_map_blocks:
        if file and block != file[0]:
            disk_map_files.append(file)
            file = [ block ]
        else:
            file.append(block)
    disk_map_files.append(file)
    return disk_map_files

""" Find the first free space  """
def find_space(disk_map_files: list, space_size: int):
    for i, file in enumerate(disk_map_files):
        if len(file) >= space_size and file[0] == ".":
            return i
    return None

def trim_empty_files(disk_map_files: list):
    while disk_map_files[-1][0] == ".":
        disk_map_files.pop()

def find_file_by_id(disk_map_files: list, file_id: str):
    for idx, file in enumerate(disk_map_files):
        if file[0] == file_id:
            return idx, file

""" Flat list from list of lists. Thanks for https://stackoverflow.com/a/952946 """
def to_disk_map_arr(disk_map_files: list):
    return sum(disk_map_files, [])

def to_str_disk_map_files(disk_map_files: list):
    return " ".join(to_disk_map_arr(disk_map_files))

def size_with_spaces(disk_map_files: list, idx: int):
    size = len(disk_map_files[idx])

    i = int(idx)-1
    while i >= 0 and disk_map_files[i][0] == ".":
        size += len(disk_map_files[i])
        i -= 1
    i = int(idx) +1

    while i < len(disk_map_files) and disk_map_files[i][0] == ".":
        size += len(disk_map_files[i])
        i += 1
    #print(f"Méret: {size}")
 
    return size

def move_file(disk_map_files: list, from_pos: int, to_pos: int):
    len_diff = len(disk_map_files[to_pos]) - len(disk_map_files[from_pos])
    if len_diff == 0 or size_with_spaces(disk_map_files, from_pos) >= len(disk_map_files[to_pos]): # just swap
        disk_map_files[to_pos], disk_map_files[from_pos] = disk_map_files[from_pos], disk_map_files[to_pos]
    else:
        tmp = disk_map_files[to_pos]
        disk_map_files[to_pos] = disk_map_files[from_pos]
        disk_map_files.insert(to_pos+1, list("."*len_diff))
        disk_map_files[from_pos + 1] = tmp
    trim_empty_files(disk_map_files)

def main():
 #   disk_map_dense = "2333133121414131402"
    with open("input/day09-input.txt", "r") as file:
        disk_map_dense = file.read().strip()

    disk_map_blocks = to_long_format(disk_map_dense).split()
    disk_map_files  = to_disk_map_files(disk_map_blocks)
    print(disk_map_blocks)
    while disk_map_blocks.count(".") > 0:
        disk_map_blocks = move_block(disk_map_blocks)
        #print_disk_map(disk_map_blocks)
    print(f"The filesystem checksum: {calc_checksum(disk_map_blocks)}")

    # PART 2
 
    idx = len(disk_map_files) - 1
    file_id_list = [f[0] for f in disk_map_files if f[0] != '.']
    file_id_list.reverse()

    for file_id in file_id_list:
        #print(f" {file} átmozgatható")
        idx, file = find_file_by_id(disk_map_files, file_id)
        space_pos = find_space(disk_map_files, len(file))
        #print(f"{len(file)} hosszú hely itt: {space_pos} ennek {file}")
        if space_pos and space_pos < idx:
            move_file(disk_map_files, idx, space_pos)
        #print(to_str_disk_map_files(disk_map_files))

    print(to_str_disk_map_files(disk_map_files))
    arr = to_disk_map_arr(disk_map_files)
    print(f"The filesystem checksum: {calc_checksum(arr)} - without file fragmentation")

if __name__ == "__main__":
    main()

