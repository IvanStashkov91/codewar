def reverse(text):
    return text[::-1]

def is_palindrome(text):
    #text = ''.join(text)
    for i in forbidden:
        text = text.replace(i, '')
    return text == reverse(text)

something = input('Введите текст: ')#.split()
forbidden = ('!', '?', ',', '.', ':', ';', '-', ' ')
print(something)

if is_palindrome(something):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")


###### или через генератор
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = ''.join(i for i in something if not i in forbidden)
    return text == reverse(text)

something = input('Введите текст: ')
forbidden = ('!', '?', ',', '.', ':', ';', '-', ' ')
print(something)

if is_palindrome(something):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")