
from operator import invert


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizz Buzz!')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# fizz_buzz()

def is_anagram(first_word: str, second_word: str):
    if first_word.lower() == second_word.lower():
        return print('No pueden ser palabras iguales')
            
    if len(first_word) != len(second_word):
        return print('No es un anagrama')

    if sorted(first_word.lower()) != sorted(second_word.lower()):
        return print('No es un anagrama')

    print(f'{first_word} y {second_word} son anagramas')

# is_anagram('limbo', 'mobil')

def fibonacci_sucession():    
    list = []
    for i in range(50):
        if i == 0:
            list.append(0)
        elif i == 1:
            list.append( list[-1] + i )
        else:
            list.append( list[-1] + list[-2] )

    print(list)

# fibonacci_sucession()

def is_prime():
    for number in range(2, 101):
        is_prime = True

        for number_2 in range(2, number):
            if number % number_2 == 0:
                is_prime = False
                break

        if is_prime:
            print(number)

# is_prime()

def reverse_string(text: str):
    # reversed_text = text[::-1]
    text_len = len(text)
    reversed_text = ''

    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]

    print(reversed_text)

    # reversed_text = []
    # for l in text:
    #     reversed_text.insert(0, l)

    # print(''.join(reversed_text))

reverse_string("Hola mundo")
