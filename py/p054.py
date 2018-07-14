from urllib import urlopen
from time import time

ALL_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def deal(cards_str):
    player1 = cards_str[:14].split()
    player2 = cards_str[15:].split()
    return (player1, player2)

def stats(l):
    return dict([(i, l.count(i)) for i in set(l)])

def values_suits(player):
    return ([c[0] for c in player], [c[1] for c in player])

def n_same_suit(suits, n):
    return n in stats(suits).values()

def values_index(values):
    return sorted(map(ALL_VALUES.index, values))

def consecutive(values):
    values = values_index(values)
    if values[1] - values[0] ==\
       values[2] - values[1] ==\
       values[3] - values[2] ==\
       values[4] - values[3] == 1:
       return True
    return False

def royal_flush(player):
    values, suits = values_suits(player)
    if not n_same_suit(suits, 5):
        return (False, None)
    if 'T' not in values or 'J' not in values\
        or 'Q' not in values or 'K' not in values\
        or 'A' not in values:
        return (False, None)
    return True

def straight_flush(player):
    values, suits = values_suits(player)
    if not n_same_suit(suits, 5) or not consecutive(values):
        return (False, None)
    values_index = values_index(values)
    return (True, values_index[-1])

def four_of_a_kind(player):
    values, suits = values_suits(player)
    v = stats(values)
    if 4 not in v.values():
        return (False, None)
    values_indexes = values_index(values)
    main_index = values_indexes[2]
    second_index = [i for i in set(values_indexes) if i != main_index][0]
    return (True, (main_index, second_index))

def full_house(player):
    values, suits = values_suits(player)
    v = stats(values)
    if 2 not in v.values() or 3 not in v.values():
        return (False, None)
    values_indexes = values_index(values)
    main_index = values_indexes[2]
    second_index = [i for i in set(values_indexes) if i != main_index][0]
    return (True, (main_index, second_index))

def flush(player):
    values, suits = values_suits(player)
    if suits.count(suits[0]) != 5:
        return (False, None)
    values_indexes = values_index(values)
    return (True, (values_indexes[-1], values_indexes[-2], values_indexes[-3],\
            values_indexes[-4], values_indexes[-5]))

def straight(player):
    values, suits = values_suits(player)
    if not consecutive(values):
        return (False, None)
    values_indexes = values_index(values)
    return (True, (values_indexes[-1]))

def three_of_a_kind(player):
    values, suits = values_suits(player)
    v = stats(values)
    if 3 not in v.values():
        return (False, None)
    values_indexes = values_index(values)
    main_index = values_indexes[2]
    second_index = max([i for i in set(values_indexes) if i != main_index])
    third_index = min([i for i in set(values_indexes) if i != main_index])
    return (True, (main_index, second_index, third_index))

def two_pairs(player):
    values, suits = values_suits(player)
    v = stats(values)
    v2 = stats(v.values())
    if 2 not in v2.keys() or v2[2] != 2:
        return (False, None)
    values_indexes = values_index(values)
    main_index = values_indexes[-2]
    second_index = values_indexes[1]
    third_index = [i for i in set(values_indexes) if i not in [main_index, second_index]][0]
    return (True, (main_index, second_index, third_index))

def one_pair(player):
    values, suits = values_suits(player)
    v = stats(values)
    if len(set(values)) != 4:
        return (False, None)
    values_indexes = values_index(values)
    main_index = ALL_VALUES.index([k for k in v.keys() if v[k] == 2][0])
    other_indexes = sorted([i for i in set(values_indexes) if i != main_index])
    return (True, (main_index, other_indexes[-1], other_indexes[-2], other_indexes[-3]))

def high_card(player):
    values, suits = values_suits(player)
    values_indexes = values_index(values)
    values_indexes.reverse()
    return values_indexes

def rank(player):
    result = (0, high_card(player))
    check, v = one_pair(player)
    result = (1, v) if check else result
    check, v = two_pairs(player)
    result = (2, v) if check else result
    check, v = three_of_a_kind(player)
    result = (3, v) if check else result
    check, v = straight(player)
    result = (4, v) if check else result
    check, v = flush(player)
    result = (5, v) if check else result
    check, v = full_house(player)
    result = (6, v) if check else result
    check, v = four_of_a_kind(player)
    result = (7, v) if check else result
    check, v = straight_flush(player)
    result = (8, v) if check else result
    check, v = royal_flush(player)
    result = (9, None) if check else result
    return result

def play(cards):
    player1, player2 = deal(cards)
    return 1 if rank(player1) > rank(player2) else 2

####################################################################################

url = "http://projecteuler.net/project/resources/p054_poker.txt"
data = urlopen(url).read()
games = data.strip().split('\n')

start = time()

score = 0

for game in games:
    score += 1 if play(game) == 1 else 0

end = time()

print score, end - start
