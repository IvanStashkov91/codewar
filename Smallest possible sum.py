'''
Given an array X of positive integers, its elements are to be transformed
by running the following operation on them as many times as required:

if X[i] > X[j] then X[i] = X[i] - X[j]
When no more transformations are possible, return its sum ("smallest possible sum").

For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:
X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
The returning output is the sum of the final transformation (here 9).

Example
solution([6, 9, 21]) #-> 9

Solution steps:
[6, 9, 12] #-> X[2] = 21 - 9
[6, 9, 6] #-> X[2] = 12 - 6
[6, 3, 6] #-> X[1] = 9 - 6
[6, 3, 3] #-> X[2] = 6 - 3
[3, 3, 3] #-> X[1] = 6 - 3
'''

def solution(a):
    N = len(a)
    end = False
    while not end:
        a = sorted(a, reverse=True)
        small = min(a)
        end = True
        for i in range(1, N):
            if a[i-1] > small:
                a[i-1] = a[i-1]%small if a[i-1]%small !=0 else small
                end = False
    return sum(a)

print(solution([200704, 51076, 142884, 117649, 4096, 32400, 85849, 14884, 226576, 14161, 38025, 225625, 48841, 174724, 28900, 17424, 12544, 19044, 168100, 183184, 180625, 27556, 179776, 34969, 51984, 160000, 19881, 55696, 127449, 178084, 3969, 212521, 90000, 87025, 95481, 236196, 215296]))

def solution(a):
    if len(a) == 1:
        return a[0]
    while 1:
        a.sort()
        if a[-1] == a[0]:
            return a[0]*len(a)
        if a[0] == 1:
            return len(a)
        for i,j in enumerate(a):
            y = j % a[0]
            if y != 0:
                a[i] = y
            else:
                a[i] = a[0]

print(solution([200704, 51076, 142884, 117649, 4096, 32400, 85849, 14884, 226576, 14161, 38025, 225625, 48841, 174724, 28900, 17424, 12544, 19044, 168100, 183184, 180625, 27556, 179776, 34969, 51984, 160000, 19881, 55696, 127449, 178084, 3969, 212521, 90000, 87025, 95481, 236196, 215296]))
