from itertools import combinations

result = 0

DIGITS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
SQUARES = {1, 4, 9, 16, 25, 36, 49, 64, 81}

combs = []

for c1 in combinations(DIGITS, 6):
    for c2 in combinations(DIGITS, 6):
        s1 = set(c1)
        s2 = set(c2)
        s1_extend = s1
        s2_extend = s2
        if 6 in s1 or 9 in s1:
            s1_extend = s1.union([6, 9])
        if 6 in s2 or 9 in s2:
            s2_extend = s2.union([6, 9])

        all_comb = set([d1*10 + d2 for d1 in s1_extend for d2 in s2_extend])
        all_comb = all_comb.union([d2*10 + d1 for d1 in s1_extend for d2 in s2_extend])

        check = True
        for sq in SQUARES:
            if sq not in all_comb:
                check = False
                break

        if check and [s1, s2] not in combs and [s2, s1] not in combs:
            combs.append([s1, s2])

print len(combs)

