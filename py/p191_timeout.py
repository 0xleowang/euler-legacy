def prizeCheck(string):
    return string.count('L') <= 1 and 'AAA' not in string

def stringReplace(string, i, char):
    l = list(string)
    l[i] = char
    return ''.join(l)

def prizeRecursive(string, i):
    global n
    if i == 0:
        n += 1
    else:
        for status in ['L', 'A', 'O']:
            nextString = stringReplace(string, -i, status)
            if(prizeCheck(nextString)):
                prizeRecursive(nextString, i-1)

n = 0
string = '-' * 30
prizeRecursive(string, len(string))
print n
    