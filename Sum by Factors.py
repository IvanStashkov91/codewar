'''
Given an array of positive or negative integers
I= [i1,..,in]
you have to produce a sorted array P of the form
[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
P will be sorted by increasing order of the prime numbers. T
he final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:
It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result,
the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain
any redundant trailing whitespace: you can use dynamically allocated character strings.
'''

def sum_for_list(lst):
    prime_dict = {}
    for j in lst:
        if valid_prime(abs(j)):
            if prime_dict.get(abs(j)) == None:
                prime_dict[abs(j)] = j
            else:
                prime_dict[abs(j)] = prime_dict[abs(j)] + j
        for i in range(2, int((abs(j) + 2) / 2)):
            if j % i == 0 and valid_prime(i):
                if prime_dict.get(i) == None:
                    prime_dict[i] = j
                else:
                    prime_dict[i] = prime_dict[i] + j
    return sorted(dict_to_list(prime_dict))

def dict_to_list(prime_dict):
    res_list = []
    for i, j in prime_dict.items():
        res_list.append([i, j])
    return res_list

def valid_prime(n):
    for i in range(2, int((n + 2) / 2)):
        if n % i == 0:
            return False
    return True

print(sum_for_list([12, 15]))


def sum_for_list(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]

# a = [12, 15]
# test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])


