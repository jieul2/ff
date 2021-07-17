number = int(input())
count = 0
number_list = [int(a) for a in str(number)]
answer_list = [int(a) for a in str(number)]

if len(number_list) == 1:
    number_list.append(0)
    answer_list.append(0)
while True:
    resultNum = sum(number_list)
    resultNum_list = [int(a) for a in str(resultNum)]

    number_list[0] = number_list[1]
    number_list[1] = resultNum_list[-1]
    count +=1
    if number_list == answer_list:
        print(count)
        break
