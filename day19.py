from itertools import combinations_with_replacement, permutations

patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]

max_size = max([len(d) for d in designs])

print(max_size)

all_possible_patterns = set()
for pattern_size in range(1, max_size+1):
    print(f"all permutations with size = {pattern_size}")
    all_comb_iter = combinations_with_replacement(patterns, r=pattern_size)
    for comb in all_comb_iter:
        all_perm_iter = permutations(comb, len(comb))
        all_perm_set = set([ "".join(elem) for elem in all_perm_iter if len("".join(elem)) <= max_size])
        all_possible_patterns = all_possible_patterns.union(all_perm_set)

print(all_possible_patterns)

count = 0
for design in designs:
    if design in all_possible_patterns:
        count += 1
    else:
        print(f"Design {design} is impossible")

print(f"Possible design count: {count}")

