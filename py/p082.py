from urllib import urlopen
from time import time

data = urlopen("http://projecteuler.net/project/resources/p082_matrix.txt").read()

str_matrix = data.rstrip().split('\n')
matrix = []
for line in str_matrix:
    matrix.append(map(int, line.split(',')))

def run(matrix):
    size = len(matrix)
    result = [matrix[i][-1] for i in range(size)]
    for x in range(-2, -(size+1), -1):
        new_result = []
        column = [matrix[y][x] for y in range(size)]
        for y in range(size):
            minimum = column[y] + result[y]
            for up in range(1, size):
                if y - up >= 0:
                    num = sum(column[p] for p in range(y, y-up-1, -1))
                    num += result[y-up]
                    minimum = num if minimum > num else minimum
                else:
                    break
            for down in range(1, size):
                if y + down < size:
                    num = sum(column[p] for p in range(y, y+down+1))
                    num += result[y+down]
                    minimum = num if minimum > num else minimum
                else:
                    break
            new_result.append(minimum)
        result = new_result
    return min(result)

start = time()
sol = run(matrix)
end = time()

print sol, end - start