'''
You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.
Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption

'''

# def longest_consec(strarr, k):
#     result = []
#     for el in strarr:
#         if len(result) <= k:
#             x = max(strarr, key=len)
#             result.append(x)
#     print(result)


def longest_consec(strarr, k):
    result = ""
    if 0 < k <= len(strarr):
        for i in range(len(strarr)):
            line = ''.join(strarr[i:i + k])
            if len(line) > len(result):
                result = line
    return result

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)
longest_consec([], 3)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)


def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)
longest_consec([], 3)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)

def testing(actual, expected):
    testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
    testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
    testing(longest_consec([], 3), "")
    testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
    testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
    testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
    testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
    testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
