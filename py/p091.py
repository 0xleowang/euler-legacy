from math import *
from time import time

start = time()

limit = 51

def distance(A, B):
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

def side_lengths(A, B):
    O = (0, 0)
    return sorted([distance(A, O), distance(B, O), distance(A, B)])

def check_right_triangle(lengths):
    a = lengths[0]
    b = lengths[1]
    c = lengths[2]
    return abs(a ** 2 + b ** 2 - c ** 2) < 0.1 / 10 ** 10

coordinates = [(x, y) for y in range(limit) for x in range(limit)]

num = 0
for a in range(1, len(coordinates)):
    for b in range(a + 1, len(coordinates)):
        lengths = side_lengths(coordinates[a], coordinates[b])
        if check_right_triangle(lengths):
            num += 1

end = time()

print num, end - start