#https://www.youtube.com/watch?v=487mr-e_Z74&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

import random

word = ['apple', 'banana', 'orange']

word_choice = random.choice(word)
word_choice_list = list(word_choice)
answer_list = ['_'] * len(word_choice_list)

print(f'answer : {word_choice}')
print(answer_list)

while '_' in answer_list:
    input_word = input('Input letter > ')
    if input_word in word_choice_list:
        print('Correct')
        word_index = list(filter(lambda e:word_choice_list[e] == input_word, range(len(word_choice_list))))
        for i in word_index: answer_list[i] = input_word
        print(answer_list)
    else: print('Wrong')

print('Success')