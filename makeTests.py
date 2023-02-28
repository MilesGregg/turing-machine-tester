import itertools
import numpy as np
import random
random.seed(1)

def p1(input):
    prev = input[0]
    for c in input[1:]:
        if c == prev:
            return False
        prev = c
    return True

def p2(input):
    return input[0] == input[-1]

def p3(input):
    n = len(input)
    if n % 2 != 0:
        return False
    left_half = input[:n//2]
    right_half = input[n//2:]
    return left_half == "0"*(n//2) and right_half == "1"*(n//2)

def p4(input):
    return input.count('0') != input.count('1')

def p5(input):
    l = 0
    r = len(input)-1
    while l <= r:
        if input[l] == input[r]:
            return False
        l += 1
        r -= 1
    return True

def p7(input):
    for i in range(3):
        l = [input[i], input[i+3], input[i+6]]
        if any(l.count(x) > 1 for x in l):
            return False
    for i in range(0, 9, 3):
        l = [input[i], input[i+1], input[i+2]]
        if any(l.count(x) > 1 for x in l):
            return False
    return True

def p6(s):
    if len(s) % 4 != 0: return False

    n = len(s) // 4

    l = [*s[:n]]
    if l.count('1') > 0: return False

    l = [*s[n:3*n]]
    if l.count('0') > 0: return False

    l = [*s[3*n:]]
    if l.count('1') > 0: return False
    return True


funcs = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5} 
N = 6

for problem in [1, 2, 3, 4, 5]:
    f = open('problem' + str(problem) + 'Tests.txt', 'w')
    for i in range(N):
        lst = list(itertools.product(['0', '1'], repeat=i+1))

        for var in lst:
            str_rep = ''.join(var)
            curr_line = str_rep + ',' + str(funcs[problem](str_rep))
            #print(curr_line)
            f.write(curr_line + '\n')
    if problem != 5: f.write(',True\n')
    if problem == 5: f.write(',False\n')
    f.close()
    print('Wrote to file: ' + 'problem' + str(problem) + 'Tests.txt')

# FOR PROBLEM 7 (DIFFERENT)
lst = list(itertools.product(['A', 'B', 'C'], repeat=9))
random.shuffle(lst)
trues = list()
falses = list()

for combination in lst:
    if p7(''.join(combination)):
        trues.append(combination)
    else:
        falses.append(combination)

f = open("problem7Tests.txt", "w")

falses = random.sample(falses, 300)
for var in falses:
    str_rep = ''.join(var)
    curr_line = str_rep + ',' + str(p7(str_rep))
    f.write(curr_line + '\n')

for var in trues:
    str_rep = ''.join(var)
    curr_line = str_rep + ',' + str(p7(str_rep))
    f.write(curr_line + '\n')

f.write(',True\n')
f.close()


# Question 6: Decide on language {0^n 1^2n 0^n | n >= 0}

# Generate valid combinations 0<=n<=20
combinations = []
for n in range(21):
    combinations.append(str('0'*n) + str('1'*n*2) + str('0'*n))

# Generate random combinations
for i in range(100):
    n = (i % 20) + 1
    nums = np.ones(n, dtype=int)
    nums[:(n // 2)] = 0
    random.shuffle(nums)
    nums = ''.join(str(v) for v in nums)
    combinations.append(''.join(nums))

f = open("problem6Tests.txt", "w")

for c in combinations:
    curr_line = c + ',' + str(p6(c))
    f.write(curr_line + '\n')

f.close()
