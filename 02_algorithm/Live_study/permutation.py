from itertools import permutations, combinations
arr = range(1, 10)
perm = list(permutations(arr, 3))
print(perm)

comb = list(combinations(arr, 3))
print(comb)