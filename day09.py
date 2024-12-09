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
def move_block(disk_map_arr: list):
    while disk_map_arr[-1] == ".":   # "trim" clean spaces from the end
        disk_map_arr.pop()

    if disk_map_arr.count(".") > 0:
        idx = disk_map_arr.index(".")
        disk_map_arr[idx] = disk_map_arr.pop()

    return disk_map_arr

def calc_checksum(disk_map_arr: list):
    product_list = [ idx * int(ch) for idx, ch in enumerate(disk_map_arr) ]
    return sum(product_list)

def print_disk_map(disk_map: list):
    print(" ".join(disk_map))

def main():
    #disk_map_dense = "2333133121414131402"
    with open("input/day09-input.txt", "r") as file:
        disk_map_dense = file.read().strip()

    disk_map_str = to_long_format(disk_map_dense)
    disk_map_arr = disk_map_str.split()

    while disk_map_arr.count(".") > 0:
        disk_map_arr = move_block(disk_map_arr)
        #print_disk_map(disk_map_arr)
    print(f"The filesystem checksum: {calc_checksum(disk_map_arr)}")

if __name__ == "__main__":
    main()

