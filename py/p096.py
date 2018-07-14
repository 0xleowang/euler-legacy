import urllib
from time import time

data = urllib.urlopen("http://projecteuler.net/project/resources/p096_sudoku.txt").readlines()

sudoku_dict = {}

for line in data:
    if line[0] == 'G':
        index = int(line[5:7])
        sudoku_dict[index] = []
    else:
        sudoku_dict[index].append(map(int, line.strip()))

def copy_s(sudoku):
    return map(list, sudoku)

def sub_s(sudoku, x, y, c):
    s = copy_s(sudoku)
    s[y][x] = c
    return s

def has_zero(sudoku):
    entries = set()
    for row in sudoku:
        entries = entries.union(row)
    return 0 in entries

def is_sudoku(l):
    try:
        if len(l) == 9 and type(l[0][0]).__name__ == 'int':
            return True
    except:
        None
    return False

def find_choices(s, x, y):
    row = s[y][:]
    line = [s[i][x] for i in range(9)]
    square = [s[y/3*3+m][x/3*3+n] for m in range(3) for n in range(3)]
    choices = list(set(range(1, 10)).difference(row, line, square))
    return choices

def fill_unique(sudoku):
    s = copy_s(sudoku)
    filled = True
    while filled:
        filled = False
        for y in range(9):
            for x in range(9):
                if s[y][x] == 0:
                    choices = find_choices(s, x, y)
                    num_choices = len(choices)
                    if num_choices == 1:
                        s[y][x] = choices[0]
                        filled = True
                    if num_choices < 1:
                        return False
    return s

def solve(sudoku):
    s = copy_s(sudoku)
    l = []
    while has_zero(s):
        new_s = fill_unique(s)
        if new_s == False:
            return False
        elif new_s != s:
            s = new_s
        else:
            for y in range(9):
                if 0 in new_s[y]:
                    x = new_s[y].index(0)
                    break
            choices = find_choices(new_s, x, y)
            if len(choices) < 1:
                return False
            for c in choices:
                try_s = solve(sub_s(new_s, x, y, c))
                l.append(try_s)
        if len(l) > 0:
            return l
    return s

def find_sol(l):
    if is_sudoku(l):
        return l
    if l != False:
        for i in l:
            sol = find_sol(i)
            if is_sudoku(sol):
                return sol

start = time()
sum = 0
for i in range(1, 51):
    sol = find_sol(solve(sudoku_dict[i]))
    sum += int(''.join(map(str,sol[0][:3])))
print sum, time() - start