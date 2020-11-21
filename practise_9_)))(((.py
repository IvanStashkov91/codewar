'''
The goal of this exercise is to convert a string to a new string
where each character in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
'''

def duplicate_encode(word):
    result = []
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)


duplicate_encode('din')
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")
print('#' * 50)


def duplicate_encode(word):
    word = word.lower()

    dict = {}
    for char in word:
        dict[char] = ')' if char in dict else '('

    return ''.join(dict[char] for char in word)

duplicate_encode('din')
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")
print('#' * 50)



def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

duplicate_encode('din')
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")
print('#' * 50)




    # Test.assert_equals(duplicate_encode("din"), "(((")
    # Test.assert_equals(duplicate_encode("recede"), "()()()")
    # Test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
    # Test.assert_equals(duplicate_encode("(( @"), "))((")