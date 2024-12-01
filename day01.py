from collections import Counter

list1 = []
list2 = []
with open("input/day01-input.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        list1.append(int(data[0]))
        list2.append(int(data[1]))

if len(list1) != len(list2):
    print("Hiba történt")
    exit

# part 1

list1.sort()
list2.sort()
diffs = [ abs(list2[i] - list1[i]) for i in range(len(list1)) ]

print(f"A különbségek összege: {sum(diffs)}")

# part 2

appereances = Counter(list2)
similarity_score = [ n * appereances.get(n, 0) for n in list1 ]

print(f"A hasonlósági pontszámok összege: {sum(similarity_score)}")