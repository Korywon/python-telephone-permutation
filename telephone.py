#!/usr/bin/python3

num_char_matrix = { \
    '2': ['a','b','c'], '3': ['d','e','f'], \
    '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'],
    '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z'] \
}

def permutate_number(number:str, idx:int=0, word:str=''):
    if idx == len(number):
        print(word)
    else:
        digit = number[idx]
        for letter in num_char_matrix[digit]:
            permutate_number(number, idx+1, word+letter)

def valid_number(number:str):
    for digit in number:
        if digit not in num_char_matrix:
            return False
    return True

if __name__ == '__main__':
    number = str(input('Enter number: '))

    if not valid_number(number):
        print('Invalid number for word.')
    else:
        permutate_number(number)
