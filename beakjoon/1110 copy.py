number = 26

number_list = [int(a) for a in str(number)]
answer_list = [int(a) for a in str(number)]
count = 0

if len(number_list) == 1:
    number_list.append(0)


while True:
    resultNum = sum(number_list)
    resultNum_list = [int(a) for a in str(resultNum)]

    number_list[0] = number_list[1]
    number_list[1] = resultNum_list[-1]
    print(f'first {number_list[0]} second {number_list[1]}')
    count +=1
    if number_list in answer_list or count == 5:
        print(count)
        break
