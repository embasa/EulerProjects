import itertools

print sorted(list(map("".join,itertools.permutations('0123456789'))))[999999]
