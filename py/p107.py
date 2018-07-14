from urllib import urlopen
from time import time

def to_int(s):
    return int(s) if s is not '-' else 0

url = "http://projecteuler.net/project/resources/p107_network.txt"
data = urlopen(url).read().strip()

start = time()

matrix_str = [line.split(',') for line in data.split()]
matrix = [map(to_int, line) for line in matrix_str]

size = len(matrix)
max_total = sum([matrix[a][b] for a in range(size) for b in range(a, size)])

visited = [0]
min_total = 0
while len(visited) != size:
    min_e = 10 ** 10
    min_v = -1
    for v_curr in visited:
        for v_next in range(size):
            edge = matrix[v_curr][v_next]
            if edge > 0 and v_next not in visited:
                if edge < min_e:
                    min_e = edge
                    min_v = v_next
    visited.append(min_v)
    min_total += min_e
    print min_total, time() - start

saving = max_total - min_total

print saving, time() - start