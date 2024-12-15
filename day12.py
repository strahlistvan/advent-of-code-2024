def get_region_area_perimeter(garden, row_idx, col_idx):
    # result variables
    garden_region = set()
    area = 0
    perimeter = 0

    def increase_perimeter(orig_perim: int, row: int, col: int):
        perim = int(orig_perim)
        if (row-1, col) in garden_region and (row-1, col+1) in garden_region and (row, col+1) in garden_region \
        and (row+1, col+1) in garden_region and (row+1, col) in garden_region \
        and (row+1, col-1) in garden_region and (row, col-1) in garden_region and (row-1, col-1) in garden_region:
            perim -= 4 # Doughnut-shape - lost 4 perimeters!
        elif (row-1, col) in garden_region and (row-1, col+1) in garden_region and (row, col+1) in garden_region \
        and (row+1, col+1) in garden_region and (row+1, col) in garden_region:
            perim -= 2 # U-shape - decrease perimeter
        elif (row, col-1) in garden_region and (row-1, col-1) in garden_region and (row-1, col) in garden_region \
        and (row-1, col+1) in garden_region and (row, col+1) in garden_region:
            perim -= 2 # U-shape - decrease perimeter
        elif (row+1, col) in garden_region and (row+1, col-1) in garden_region and (row, col-1) in garden_region \
        and (row-1, col-1) in garden_region and (row-1, col) in garden_region:
            perim -= 2 # U-shape - decrease perimeter
        elif (row, col-1) in garden_region and (row+1, col-1) in garden_region and (row+1, col) in garden_region \
        and (row+1, col+1) in garden_region and (row, col+1) in garden_region:
            perim -= 2 # U-shape - decrease perimeter
        elif (row, col-1) in garden_region and (row-1, col) in garden_region:
            if (row-1, col-1) in garden_region: # L-shape to rectangle - perimeter not change
                perim += 0
            else:
                perim += 2
        elif (row, col+1) in garden_region and (row-1, col) in garden_region:
            if (row-1, col+1) in garden_region: # L-shape to rectangle - perimeter not change
                perim += 0
            else:
                perim += 2
        elif (row, col-1) in garden_region and (row+1, col) in garden_region:
            if (row+1, col-1) in garden_region: # L-shape to rectangle - perimeter not change
                perim += 0
            else:
                perim += 2
        elif (row, col+1) in garden_region and (row+1, col) in garden_region:
            if (row+1, col+1) in garden_region: # L-shape to rectangle - perimeter not change
                perim += 0
            else:
                perim += 2
        elif (row, col-1) in garden_region or (row, col+1) in garden_region: # has left or right neighbours
            perim += 2
        elif (row-1, col) in garden_region or (row+1, col) in garden_region: # has upper or lower neighbours
            perim += 2
        else: # no neighbours at all
            perim += 4

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
    plantname = garden[row_idx][col_idx] 
    extend_area(row_idx, col_idx, plantname)
    return garden_region, area, perimeter

def read_input(filename):
    with open(filename, "r") as file:
        print(filename)
        return file.read().strip().split("\n")

def main():
    garden = read_input("input/day12-input.txt")

    total_price = 0
    all_regions = set()

    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if (i, j) not in all_regions: # field not processed yet
                region, area, perimeter = get_region_area_perimeter(garden, row_idx=i, col_idx=j)
                all_regions = all_regions.union(set(region))
             #   print(f" {plant} area: {area} perimeter: {perimeter} multiply {area * perimeter}")
                total_price += (area * perimeter)
    print(f"Total price: {total_price}")

if __name__ == "__main__":
    main()