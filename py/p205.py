from __future__ import division

def prob(list):
    return dict([(key, list.count(key) / len(list)) for key in set(list)])

pyramidal = [(a, b, c, d, e, f, g, h, i)
            for a in range(1, 5) for b in range(1, 5) for c in range(1, 5)
            for d in range(1, 5) for e in range(1, 5) for f in range(1, 5)
            for g in range(1, 5) for h in range(1, 5) for i in range(1, 5)]

four = map(sum, pyramidal)

cubic = [(a, b, c, d, e, f) for a in range(1, 7) for b in range(1, 7)
                            for c in range(1, 7) for d in range(1, 7)
                            for e in range(1, 7) for f in range(1, 7)]
six = map(sum, cubic)

peter = prob(four)
colin = prob(six)

probability = 0
for four_total, four_prob in peter.items():
    for six_total, six_prob in colin.items():
        if four_total > six_total:
            probability += four_prob * six_prob

round(probability, 7)