#https://www.youtube.com/watch?v=487mr-e_Z74&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

import random

word = ['apple', 'banana', 'orange']

word_choice = random.choice(word)
word_choice_list = list(word_choice)
answer_list = ['_' * len(word_choice_list)]

print(word_choice_list)
print(answer_list)

if input('Input letter > ') in word_choice_list:
    print('Correct')
else: print('Wrong')