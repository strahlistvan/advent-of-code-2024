def get_region_area_perimeter(plant, garden):

    HEIGHT = len(garden)
    WIDTH  = len(garden[0])

    # result variables
    garden_region = set()
    area = 0
    perimeter = 0

    def extend_area(row, col, plant):
        if row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH:
            return
        if garden[row][col] != plant: # current position is not 
            return
        if (row, col) in garden_region: # previously detected
            return

        garden_region.add((row, col)) # save the plot position to region

        # TODO: ugly perimeter calculation... maybe new function?
        nonlocal area
        area += 1
        nonlocal perimeter
        perimeter += 4
        if (row, col-1) in garden_region and (row-1, col) in garden_region:
            perimeter -= 4
        elif (row, col+1) in garden_region and (row-1, col) in garden_region:
            perimeter -= 4
        elif (row, col-1) in garden_region and (row+1, col) in garden_region:
            perimeter -= 4
        elif (row, col+1) in garden_region and (row+1, col) in garden_region:
            perimeter -= 4
        elif (row, col-1) in garden_region or (row, col+1) in garden_region:
            perimeter -= 2
            if (row-1, col) in garden_region:
                perimeter -= 1
            if (row+1, col) in garden_region:
                perimeter -= 1
        elif (row-1, col) in garden_region or (row+1, col) in garden_region:
            perimeter -= 2
            if (row, col-1) in garden_region:
                perimeter -= 1
            if (row, col+1) in garden_region:
                perimeter -= 1

        if row+1 < len(garden):
            extend_area(row+1, col, plant)
        if row-1 >= 0:
            extend_area(row-1, col, plant)
        if col+1 < 4:
            extend_area(row, col+1, plant)
        if col-1 >= 0:
            extend_area(row, col-1, plant)

    for i, row in enumerate(garden):
        for j, p in enumerate(row):
            if p == plant:
                start_pos = (i, j)
                break
    if start_pos:
        # recursive function call
        extend_area(start_pos[0], start_pos[1], plant)

    return garden_region, area, perimeter

def main():
    garden = ["AAAA"
            ,"BBCD"
            ,"BBCC"
            ,"EEEC"]
    plants = set("".join(garden))
    total_price = 0
    for plant in plants:
        region, area, perimeter = get_region_area_perimeter(plant, garden)
        print(f" {plant} region: {region} area: {area} perimeter: {perimeter}")
        total_price += (area * perimeter)
    print(f"Total price: {total_price}")

if __name__ == "__main__":
    main()