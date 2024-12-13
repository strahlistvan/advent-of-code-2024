def blink(stones: list):
    i = 0
    while i < len(stones):  # stone count could be increased in the loop
        stone = stones[i]
        if int(stone) == 0:
            stones[i] = "1"
        elif len(stone) % 2 == 0: # even number of digits
            first = stone[:len(stone)//2]
            second = str(int(stone[len(stone)//2:])) # eliminate leading zeroes
            stones.insert(i, first)
            i += 1
            stones[i] = second
        else:
            stones[i] = str(2024 * int(stone))
        i += 1
    return stones


def main():
    input = "6563348 67 395 0 6 4425 89567 739318" # "125 17" # "0 1 10 99 999"
    stones = input.split()
    print(stones)
    for k in range(75): # PART 1 and PART 2 ?
        stones = blink(stones)
        if (k+1) % 5 == 0: # less output
            print(f"Stones count after {k+1} blink: {len(stones)}")

if __name__ == "__main__":
    main()