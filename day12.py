def get_region_area_perimeter(plant, garden):

    # result variables
    garden_region = set()
    area = 0
    perimeter = 0

    def increase_perimeter(orig_perim: int, row: int, col: int):
        perim = orig_perim + 4
        print(f"increase  {row},{col} - current: {orig_perim}")
        if (row, col-1) in garden_region and (row-1, col) in garden_region:
            print("inc v1")
            if (row-1, col-1) in garden_region:
                perim -= 4
            else:
                perim -= 2
        elif (row, col+1) in garden_region and (row-1, col) in garden_region:
            print("inc v2")
            if (row-1, col+1) in garden_region:
                perim -= 4
            else:
                perim -= 2
        elif (row, col-1) in garden_region and (row+1, col) in garden_region:
            print("inc v3")
            if (row+1, col-1) in garden_region:
                perim -= 4
            else:
                perim -= 2
        elif (row, col+1) in garden_region and (row+1, col) in garden_region:
            print("inc v4")
            if (row+1, col+1) in garden_region:
                perim -= 4
            else:
                perim -= 2
   #     elif (row, col-1) in garden_region and (row+1, col-1) in garden_region  \
   #     or   (row, col-1) in garden_region and (row-1, col-1) in garden_region  \
   #     or   (row, col+1) in garden_region and (row+1, col+1) in garden_region  \
  #      or   (row, col+1) in garden_region and (row-1, col+1) in garden_region:
  #          print("inc v4.5")
  #          perim -= 1
        elif (row, col-1) in garden_region or (row, col+1) in garden_region:
            print("inc v5")
            perim -= 2
            if (row-1, col) in garden_region:
                perim -= 1
            if (row+1, col) in garden_region:
                perim -= 1
            print("inc v6")
        elif (row-1, col) in garden_region or (row+1, col) in garden_region:
            print("inc v7")
            perim -= 2
            if (row, col-1) in garden_region:
                perim -= 1
            if (row, col+1) in garden_region:
                perim -= 1
        return perim

    """ recursive inner function """
    def extend_area(row, col, plant):
        HEIGHT = len(garden)
        WIDTH  = len(garden[0])
        if row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH: # outside the garden
            return
        if garden[row][col] != plant: # current position is not 
            return
        if (row, col) in garden_region: # previously detected
            return
        garden_region.add((row, col)) # save the plot position to region
        nonlocal area
        area += 1
        nonlocal perimeter
        perimeter = increase_perimeter(perimeter, row, col)
        # extend area to neighbours
        extend_area(row+1, col, plant)
        extend_area(row-1, col, plant)
        extend_area(row, col+1, plant)
        extend_area(row, col-1, plant)

    # main function logic
    for i, row in enumerate(garden):
        for j, p in enumerate(row):
            if p == plant:
                start_pos = (i, j)
                break
    if start_pos:
        # recursive function call start in here
        extend_area(start_pos[0], start_pos[1], plant)

    return garden_region, area, perimeter

def read_input(filename):
    with open(filename, "r") as file:
        print(filename)
        return file.read().split("\n")

def main():
    garden = ["AAAA"
            ,"BBCD"
            ,"BBCC"
            ,"EEEC"]
    garden = read_input("input/day12-test-input.txt")

    plants = set("".join(garden))
    total_price = 0
    #for plant in plants:
    plant = "E"
    region, area, perimeter = get_region_area_perimeter(plant, garden)
    print(f" {plant} region: {region} area: {area} perimeter: {perimeter} multiply {area * perimeter}")
    total_price += (area * perimeter)
    print(f"Total price: {total_price}")

if __name__ == "__main__":
    main()