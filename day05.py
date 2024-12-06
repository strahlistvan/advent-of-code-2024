with open("input/day05-input.txt", "r") as file:
    rules = []
    updates = []
    for line in file:
        if line.find("|") != -1:
            rules.append(line.strip().split('|'))
        elif line.strip() != "":
            updates.append(line.strip().split(','))

def check_page(page, page_idx, update):
    for rule in rules:
        if rule[1] == page and rule[0] in update[page_idx:]:
            return False
        if rule[0] == page and rule[1] in update[:page_idx]:
            return False
    return True

def get_middle(list):
    return int(list[len(list)//2])

sum_middle = 0
bad_updates = [] # prepare for part 2
for update in updates:
    update_ok = True
    for i in range(len(update)):
        if not check_page(update[i], i, update):
            update_ok = False
    if update_ok:
        sum_middle += get_middle(update)
    else:
        bad_updates.append(update)

print(f"Sum of the good updates middle pages: {sum_middle}")

# part 2 - something like bubble sort :)

def correct(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            for rule in rules:
                if rule[0] == update[j] and rule[1] == update[i]:
                    update[i], update[j] = update[j], update[i]
                    # print(f"swapped: {update[i]} - {update[j]}")

sum_middle = 0
for update in bad_updates:
    for i in range(len(update)):
        while not check_page(update[i], i, update):
            correct(update)
    sum_middle += get_middle(update)

print(f"Sum of the good updates middle pages after corrections: {sum_middle}")
