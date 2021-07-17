a = 26

if a < 10:
    a = int(str(a) + '0')

answer = a
count = 0

print(f'first  {str(a)[:1]}')
print(f'second  {a%10}')

while True:
    firstNum = int(a/10)
    secondNum = a % 10
    tem = firstNum + secondNum
    print(tem)
    if tem > 10:
        secondNum = tem % 10

    a = int(str(secondNum) + str(tem))
    print(f'{answer} === {a} first : {firstNum} second : {secondNum}')
    count += 1
    if a == answer or count == 5:
        print(count)
        break

# while True:

#     tem = int(str(a)[:-1]) + int(str(a)[-1:])
#     if tem > 10:
#         tem = int(str(tem)[-1:])
#     a = int(str(a)[-1:] + str(tem))
#     count += 1
#     if a == answer:
#         print(count)
#         break

