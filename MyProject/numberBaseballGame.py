"""
============================
====Number Baseball Game====
============================
"""
import random


def nbg(player):
    number_length = int(input('자릿수를 입력하세요. :'))
    numberRandom_list = []
    num = random.randrange(0, 10)
    # 랜덤숫자 생성
    for i in range(number_length):
        while num in numberRandom_list:
            num = random.randrange(0, 10)
        numberRandom_list.append(num)
    # 맞추기
    print(numberRandom_list)
    answerNumber_list = [x for x in input('입력하세요 :').split()]
    while answerNumber_list in numberRandom_list:
        answerNumber_list = [x for x in input('입력하세요 :').split()]

        
        
    print('성공')
    