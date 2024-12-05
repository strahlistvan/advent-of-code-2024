with open("input/day05-input.txt", "r") as file:
    rules = []
    updates = []
    for line in file:
        if line.find("|") != -1:
            rules.append(line.strip().split('|'))
        elif line.strip() != "":
            updates.append(line.strip().split(','))
print(rules)
print(updates)


def check_page(page, page_idx, update):
    for rule in rules:
        if rule[1] == page and rule[0] in update[page_idx:]:
            print(f'Talált ilyet, hogy {rule[1]} megelőzi {rule[0]}-t')
            return False
        if rule[0] == page and rule[1] in update[:page_idx]:
            return False
    return True

def get_middle(list):
    return int(list[len(list)//2])

sum_middle = 0
for update in updates:
    update_ok = True
    for i in range(len(update)):
        if not check_page(update[i], i, update):
            update_ok = False
    print(str(update) + ' is ok: ' + str(update_ok))
    if update_ok:
        print(f"A középső: {get_middle(update)}")
        sum_middle += get_middle(update)

print(f"Sum of the good updates middle pages: {sum_middle}")